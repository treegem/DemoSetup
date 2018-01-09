import ctypes
import numpy
from camera import Camera
from ueye_constants import *
import time

#Loading drivers
dll = ctypes.cdll.LoadLibrary('ueye_api.dll')


class IS_RECT(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_int),
        ("y", ctypes.c_int),
        ("w", ctypes.c_int),
        ("h", ctypes.c_int)
        ]


class IO_GPIO_CONFIGURATION(ctypes.Structure):
    _fields_ = [
        ("u32Gpio", ctypes.c_uint),
        ("u32Caps", ctypes.c_uint),
        ("u32Configuration", ctypes.c_uint),
        ("u32State", ctypes.c_uint),
        ("u32Reserved0", ctypes.c_uint),
        ("u32Reserved1", ctypes.c_uint),
        ("u32Reserved2", ctypes.c_uint),
        ("u32Reserved3", ctypes.c_uint),
        ("u32Reserved4", ctypes.c_uint),
        ("u32Reserved5", ctypes.c_uint),
        ("u32Reserved6", ctypes.c_uint),
        ("u32Reserved7", ctypes.c_uint),
        ("u32Reserved8", ctypes.c_uint),
        ("u32Reserved9", ctypes.c_uint),
        ("u32Reserved10", ctypes.c_uint),
        ("u32Reserved11", ctypes.c_uint)
        ]


class IO_FLASH_PARAMS(ctypes.Structure):
    _fields_ = [
        ("s32Delay", ctypes.c_int),
        ("u32Duration", ctypes.c_uint)
        ]


def get_number_of_devices():
    return dll.is_GetNumberOfDevices()


class UEyeCamera (Camera):
    """
    UEyeCamera - class representing an IDS UEye Camera
    philosophy: get, set functions call IDS dll to retrieve or store data from/on the camera
                class variables are always kept up to date such as to mirror the parameters on the camera
    """

    hwnd = ctypes.c_void_p(0)
    fpix = 0
    aoi = (0, 0, 1280, 1024)  # area of interest, format x,y,w,h, defines the image section to be captured
    dt = 0.0  # exposure time in ms
    fps = 0.0  # framerate in frames per second

    #Mounts a ueye camera
    def __init__(self, cam=0, fpix=10):
        Camera.__init__(self)

        #Converting parameters
        fpix = ctypes.c_uint(0)
        self.cam = ctypes.c_uint16(cam)

        #Mounting camera via the driver
        if dll.is_InitCamera(ctypes.byref(self.cam), self.hwnd) != IS_SUCCESS:
            print "UEyeCamera warning: could not initialize camera"

        #configure camera into a scientifically useful mode, switch off all fancy corrections
        #16bit raw data format
        err = dll.is_SetColorMode(self.cam, IS_CM_SENSOR_RAW16)
        if err != IS_SUCCESS:
            print "UEyeCamera Warning: failed to set 16bit data format, err code " + str(err)

        #no auto blacklevel
        blacklevel_mode = ctypes.c_int(IS_AUTO_BLACKLEVEL_OFF)
        blacklevel_offset = ctypes.c_int(10)
        err = dll.is_Blacklevel(self.cam, IS_BLACKLEVEL_CMD_SET_MODE, ctypes.byref(blacklevel_mode), ctypes.sizeof(blacklevel_mode))
        if err != IS_SUCCESS:
            print "UEyeCamera Warning: failed to switch off auto blacklevel, err code " + str(err)

        #Blacklevel offset= 0
        err = dll.is_Blacklevel(self.cam, IS_BLACKLEVEL_CMD_SET_OFFSET, ctypes.byref(blacklevel_offset), ctypes.sizeof(blacklevel_offset))
        if err != IS_SUCCESS:
            print "UEyeCamera Warning: failed to set blacklevel to zero, err code " + str(err)

        #no auto gain
        pval1 = ctypes.c_double(0)
        pval2 = ctypes.c_double(0)
        err = dll.is_SetAutoParameter(self.cam, IS_SET_ENABLE_AUTO_GAIN, ctypes.byref(pval1), ctypes.byref(pval2))
        if err != IS_SUCCESS:
            print "UEyeCamera Warning: failed to switch off automatic gain, err code " + str(err)

        #err = dll.is_SetHWGainFactor(self.cam, IS_SET_MASTER_GAIN_FACTOR, 0)
        #if err != IS_SUCCESS:
        #    print "UEyeCamera Warning: failed to switch off hardware gain, err code " + str(err)

        #keep internal variables up to date
        err = dll.is_PixelClock(self.cam, IS_PIXELCLOCK_CMD_GET, ctypes.byref(fpix), ctypes.sizeof(fpix))
        if err == IS_SUCCESS:
            self.fpix = fpix
        else:
            self.fpix = 0
            print "UEyeCamera warning: could not retrieve pixel clock"

        #Define
        self.aoi = self._get_aoi()

    #Unmount the camera on .close()
    def __del__(self):
        dll.is_ExitCamera(self.cam)

    #Set the "pixel clock"
    def set_pixel_clock(self, fpix):
        fpix = ctypes.c_uint(fpix)
        err = dll.is_PixelClock(self.cam, IS_PIXELCLOCK_CMD_SET, ctypes.byref(fpix), ctypes.sizeof(fpix))
        if err != IS_SUCCESS:
            print "UEyeCamera Warning: failed to set pixel clock, err code " + str(err)

        #get actual value of pixel clock
        err = dll.is_PixelClock(self.cam, IS_PIXELCLOCK_CMD_GET, ctypes.byref(fpix), ctypes.sizeof(fpix))
        if err == IS_SUCCESS:
            self.fpix = fpix
        else:
            self.fpix = 0
            print "UEyeCamera warning: could not retrieve pixel clock"

    #Set exposure time in ms. Change only in steps of 100 and set value twice in order to work properly
    def set_exposure(self, dt):
        if dt > self.dt:
            texp = ctypes.c_double(dt)
            fps = ctypes.c_double(1.0 / dt / 1e-3)
            newfps = ctypes.c_double(1.0 / dt / 1e-3)
            err = dll.is_SetFrameRate(self.cam, fps, ctypes.byref(newfps))
            if err != IS_SUCCESS:
                print "UEyeCamera Warning: failed to set framerate, err code " + str(err)
            err = dll.is_Exposure(self.cam, IS_EXPOSURE_CMD_SET_EXPOSURE, ctypes.byref(texp), ctypes.sizeof(texp))
            if err != IS_SUCCESS:
                print "UEyeCamera Warning: failed to set exposure, err code " + str(err)
            self.acquire_image()  # acquire dummy image to make changed exposure time effective
            self.dt = self._get_exposure()
            self.fps = newfps.value
        else:
            for t in numpy.arange(dt, self.dt, 100)[::-1]:
                texp = ctypes.c_double(t)
                fps = ctypes.c_double(1.0 / t / 1e-3)
                newfps = ctypes.c_double(1.0 / t / 1e-3)
                err = dll.is_SetFrameRate(self.cam, fps, ctypes.byref(newfps))
                if err != IS_SUCCESS:
                    print "UEyeCamera Warning: failed to set framerate, err code " + str(err)
                err = dll.is_Exposure(self.cam, IS_EXPOSURE_CMD_SET_EXPOSURE, ctypes.byref(texp), ctypes.sizeof(texp))
                if err != IS_SUCCESS:
                    print "UEyeCamera Warning: failed to set exposure, err code " + str(err)
                self.acquire_image()  # acquire dummy image to make changed exposure time effective
                self.dt = self._get_exposure()
                self.fps = newfps.value

    #Get exposure time
    def _get_exposure(self):
        texp = ctypes.c_double(self.dt)
        err = dll.is_Exposure(self.cam, IS_EXPOSURE_CMD_GET_EXPOSURE, ctypes.byref(texp), ctypes.sizeof(texp))
        if err != IS_SUCCESS:
            print "UEyeCamera Warning: failed to get exposure, err code " + str(err)
        return texp.value

    #Get framerate
    def _get_framerate(self):
        return self.fps

    def _get_ext_trig(self):
        return dll.is_SetExternalTrigger(self.cam, IS_GET_EXTERNALTRIGGER)

    def _get_ext_trig_status(self):
        return dll.is_SetExternalTrigger(self.cam, IS_GET_TRIGGER_STATUS)

    #Set/get area of Interest
    def _get_aoi(self):
        aoi = IS_RECT(*self.aoi)
        err = dll.is_AOI(self.cam, IS_AOI_IMAGE_GET_AOI, ctypes.byref(aoi), ctypes.sizeof(aoi))
        if err != IS_SUCCESS:
            print "UEyeCamera Warning: failed to retrieve aoi, err code " + str(err)
        return (aoi.x, aoi.y, aoi.w, aoi.h)

    def set_aoi(self, aoi):
        aoi = IS_RECT(*aoi)
        err = dll.is_AOI(self.cam, IS_AOI_IMAGE_SET_AOI, ctypes.byref(aoi), ctypes.sizeof(aoi))
        if err != IS_SUCCESS:
            print "UEyeCamera Warning: failed to set aoi, err code " + str(err)
        self.aoi = self._get_aoi()

    #Make a photo
    def acquire_image(self):
        #images are of the dimension of the area of interest and have 16bit colours
        image = numpy.zeros((self.aoi[3], self.aoi[2]), dtype=numpy.uint16)
        pid = ctypes.c_int(0)
        #Prepare memory
        err = dll.is_SetAllocatedImageMem(self.cam, self.aoi[2], self.aoi[3], 16, image.ctypes.data, ctypes.byref(pid))
        if err != IS_SUCCESS:
            print "UEyeCamera Warning: failed to link acquisition memory, err code " + str(err)
        err = dll.is_SetImageMem(self.cam, image.ctypes.data, pid)
        if err != IS_SUCCESS:
            print "UEyeCamera Warning: failed to register acquisition memory, err code " + str(err)
        #Stop the running video
        err = dll.is_FreezeVideo(self.cam, IS_WAIT)
        if err != IS_SUCCESS:
            print "UEyeCamera Warning: failed to acquire image, err code " + str(err)
        #Get the image from the memory
        dll.is_FreeImageMem(self.cam, image.ctypes.data, pid)
        return image

    #Start a video over a number of frames
    def arm_video(self, nframes, timeout=30.0):
        self.timeout = timeout
        #a video is a number of images in a list
        self.result = [numpy.zeros((self.aoi[3], self.aoi[2]), dtype=numpy.uint16) for i in range(nframes)]
        self.pids = numpy.zeros(len(self.result))

        #prepare video aquisition
        ioConfiguration = IO_GPIO_CONFIGURATION(IO_GPIO_2, 0, IS_GPIO_TRIGGER, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        err = dll.is_IO(self.cam, IS_IO_CMD_GPIOS_SET_CONFIGURATION, ctypes.byref(ioConfiguration), ctypes.sizeof(ioConfiguration))
        if err != IS_SUCCESS:
            print "UEyeCamera Warning: failed to set gpio trigger input, err code " + str(err)
        err = dll.is_SetExternalTrigger(self.cam, IS_SET_TRIGGER_LO_HI)
        if err != IS_SUCCESS:
            print "UEyeCamera Warning: failed to set hardware trigger, err code " + str(err)

        #Prepare the memory for each frame after each other
        for fi, frame in enumerate(self.result):
            pid = ctypes.c_int(0)
            err = dll.is_SetAllocatedImageMem(self.cam, self.aoi[2], self.aoi[3], 16, frame.ctypes.data, ctypes.byref(pid))
            self.pids[fi] = pid.value
            if err != IS_SUCCESS:
                print "UEyeCamera Warning: failed to link acquisition memory, err code " + str(err)
            err = dll.is_AddToSequence(self.cam, frame.ctypes.data, pid)
            if err != IS_SUCCESS:
                print "UEyeCamera Warning: failed to add frame " + str(fi) + " to sequence, err code " + str(err)

        pc_mem = ctypes.c_char_p()
        pc_mem_last = ctypes.c_char_p()
        nNum = ctypes.c_int(0)

        #Set the capture time
        self.et = time.time() + nframes * self.dt * 1e-3

        #Start the video
        err = dll.is_CaptureVideo(self.cam, IS_DONT_WAIT)
        if err != IS_SUCCESS:
            print "UEyeCamera Warning: failed to start video capture, err code " + str(err)

    #Read the recorded video
    def get_video(self):
        pc_mem = ctypes.c_char_p()
        pc_mem_last = ctypes.c_char_p()
        nNum = ctypes.c_int(0)
        #wait for ring buffer to loop over, i.e. wait for acquisition of last frame
        #wait at least for nominal acquisition time of nframes. wait at most this time plus timeout
        while (nNum.value != 1 or time.time() < self.et) and time.time() < self.et + self.timeout:
            #print "nNum is " +str(nNum.value)
            dll.is_GetActSeqBuf(self.cam, ctypes.byref(nNum), ctypes.byref(pc_mem), ctypes.byref(pc_mem_last))

        #Stop the video when its done
        err = dll.is_StopLiveVideo(self.cam, IS_WAIT)
        if err != IS_SUCCESS:
            print "UEyeCamera Warning: failed to stop video capture" + str(err)

        #Clear the memory links
        err = dll.is_ClearSequence(self.cam)
        if err != IS_SUCCESS:
            print "UEyeCamera Warning: failed to clear sequence, err code " + str(err)

        #Get each frame from the memory
        for fi, frame in enumerate(self.result):
            err = dll.is_FreeImageMem(self.cam, frame.ctypes.data, ctypes.c_int(int(self.pids[fi])))
            if err != IS_SUCCESS:
                print "UEyeCamera Warning: failed to remove frame " + str(fi) + " from sequence, err code " + str(err)

        #Reset the camera trigger and return the video
        dll.is_SetExternalTrigger(self.cam, IS_SET_TRIGGER_SOFTWARE)
        return self.result

    #Aquire a video in one method
    def acquire_video(self, nframes, timeout=30.0):
        """
        acquire_video - acquire nframes (>=2) frames of video with previously configured exposure time and aoi
        """
        result = [numpy.zeros((self.aoi[3], self.aoi[2]), dtype=numpy.uint16) for i in range(nframes)]
        pids = numpy.zeros(len(result))

        #prepare memory
        for fi, frame in enumerate(result):
            pid = ctypes.c_int(0)
            err = dll.is_SetAllocatedImageMem(self.cam, self.aoi[2], self.aoi[3], 16, frame.ctypes.data, ctypes.byref(pid))
            pids[fi] = pid.value
            if err != IS_SUCCESS:
                print "UEyeCamera Warning: failed to link acquisition memory, err code " + str(err)
            err = dll.is_AddToSequence(self.cam, frame.ctypes.data, pid)
            if err != IS_SUCCESS:
                print "UEyeCamera Warning: failed to add frame " + str(fi) + " to sequence, err code " + str(err)

        #err = dll.is_SetExternalTrigger(self.cam, IS_SET_TRIGGER_SOFTWARE)
        #err = dll.is_SetGlobalShutter(self.cam, IS_SET_GLOBAL_SHUTTER_ON)
        #if err != IS_SUCCESS:
        #    print "UEyeCamera Warning: failed to set global shutter, err code " + str(err)

        #More preperation
        burstsize = ctypes.c_uint(1)
        err = dll.is_Trigger(self.cam, IS_TRIGGER_CMD_SET_BURST_SIZE, ctypes.byref(burstsize), ctypes.sizeof(burstsize))
        if err != IS_SUCCESS:
            print "UEyeCamera Warning: failed to set trigger burst size, err code " + str(err)
        err = dll.is_SetExternalTrigger(self.cam, IS_SET_TRIGGER_OFF)
        if err != IS_SUCCESS:
            print "UEyeCamera Warning: failed to switch off trigger, err code " + str(err)
        flash_conf = IO_FLASH_PARAMS(0, 1000)
        err = dll.is_IO(self.cam, IS_IO_CMD_FLASH_SET_PARAMS, ctypes.byref(flash_conf), ctypes.sizeof(flash_conf))
        if err != IS_SUCCESS:
            print "UEyeCamera Warning: failed to set flash timing , err code " + str(err)
        cmd = ctypes.c_uint(IO_FLASH_MODE_FREERUN_HI_ACTIVE)
        err = dll.is_IO(self.cam, IS_IO_CMD_FLASH_SET_MODE, ctypes.byref(cmd), ctypes.sizeof(cmd))
        if err != IS_SUCCESS:
            print "UEyeCamera Warning: failed to activate flash, err code " + str(err)
        err = dll.is_IO(self.cam, IS_IO_CMD_FLASH_GET_MODE, ctypes.byref(cmd), ctypes.sizeof(cmd))

        ioConfiguration = IO_GPIO_CONFIGURATION(IO_GPIO_1, 0, IS_GPIO_FLASH, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        err = dll.is_IO(self.cam, IS_IO_CMD_GPIOS_SET_CONFIGURATION, ctypes.byref(ioConfiguration), ctypes.sizeof(ioConfiguration))
        if err != IS_SUCCESS:
            print "UEyeCamera Warning: failed to set gpio 1 as flash output, err code " + str(err)
        #err=dll.is_IO(self.cam, IS_IO_CMD_GPIOS_GET_CONFIGURATION, ctypes.byref(ioConfiguration), ctypes.sizeof(ioConfiguration))
        #if err != IS_SUCCESS:
        #    print "UEyeCamera Warning: failed to get gpio conf, err code " + str(err)
        #print "gpio conf get: configuration %d state %d "%(ioConfiguration.u32Configuration, ioConfiguration.u32State)

        #Calculate video time
        st = time.time()

        #Start video
        err = dll.is_CaptureVideo(self.cam, IS_WAIT)
        if err != IS_SUCCESS:
            print "UEyeCamera Warning: failed to start video capture" + str(err)

        pc_mem = ctypes.c_char_p()
        pc_mem_last = ctypes.c_char_p()
        nNum = ctypes.c_int(0)
        #wait for nframes-1 frames to be acquired
        while nNum.value < nframes and time.time() < st + timeout:
            dll.is_GetActSeqBuf(self.cam, ctypes.byref(nNum), ctypes.byref(pc_mem), ctypes.byref(pc_mem_last))
            #print "acquiring frame " + str(nNum.value) + "\r"

        #wait for ring buffer to loop over, i.e. wait for acquisition of last frame
        while nNum.value != 1 and time.time() < st + timeout:
            dll.is_GetActSeqBuf(self.cam, ctypes.byref(nNum), ctypes.byref(pc_mem), ctypes.byref(pc_mem_last))

        if time.time() >= (st + timeout):
            print "UEyeCamera Warning: acquisition exceeded timeout"

        #Stop video
        dll.is_StopLiveVideo(self.cam, IS_WAIT)
        if err != IS_SUCCESS:
            print "UEyeCamera Warning: failed to stop video capture" + str(err)

        #Unlink memory
        err = dll.is_ClearSequence(self.cam)
        if err != IS_SUCCESS:
            print "UEyeCamera Warning: failed to clear sequence, err code " + str(err)

        #Get the video
        for fi, frame in enumerate(result):
            err = dll.is_FreeImageMem(self.cam, frame.ctypes.data, ctypes.c_int(int(pids[fi])))
            if err != IS_SUCCESS:
                print "UEyeCamera Warning: failed to remove frame " + str(fi) + " from sequence, err code " + str(err)

        err = dll.is_SetExternalTrigger(self.cam, IS_SET_TRIGGER_SOFTWARE)
        #err = dll.is_SetExternalTrigger(self.cam, IS_SET_TRIGGER_OFF)
        if err != IS_SUCCESS:
            print "UEyeCamera Warning: failed to set software trigger, err code " + str(err)

        #Return the video
        return result
