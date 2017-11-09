WM_USER = 0x400
# ----------------------------------------------------------------------------
# Color modes
# ----------------------------------------------------------------------------
IS_COLORMODE_INVALID = 0
IS_COLORMODE_MONOCHROME = 1
IS_COLORMODE_BAYER = 2
IS_COLORMODE_CBYCRY = 4
IS_COLORMODE_JPEG = 8
# ----------------------------------------------------------------------------
#  Sensor Types
# ----------------------------------------------------------------------------
IS_SENSOR_INVALID = 0x0000
# CMOS Sensors
IS_SENSOR_UI141X_M = 0x0001      # VGA rolling shutter, monochrome
IS_SENSOR_UI141X_C = 0x0002      # VGA rolling shutter, color
IS_SENSOR_UI144X_M = 0x0003      # SXGA rolling shutter, monochrome
IS_SENSOR_UI144X_C = 0x0004      # SXGA rolling shutter, SXGA color
IS_SENSOR_UI154X_M = 0x0030      # SXGA rolling shutter, monochrome
IS_SENSOR_UI154X_C = 0x0031      # SXGA rolling shutter, color
IS_SENSOR_UI145X_C = 0x0008      # UXGA rolling shutter, color
IS_SENSOR_UI146X_C = 0x000a      # QXGA rolling shutter, color
IS_SENSOR_UI148X_M = 0x000b      # 5MP rolling shutter, monochrome
IS_SENSOR_UI148X_C = 0x000c      # 5MP rolling shutter, color
IS_SENSOR_UI121X_M = 0x0010      # VGA global shutter, monochrome
IS_SENSOR_UI121X_C = 0x0011      # VGA global shutter, VGA color
IS_SENSOR_UI122X_M = 0x0012      # WVGA global shutter, monochrome
IS_SENSOR_UI122X_C = 0x0013      # WVGA global shutter, color
IS_SENSOR_UI164X_C = 0x0015      # SXGA rolling shutter, color
IS_SENSOR_UI155X_C = 0x0017      # UXGA rolling shutter, color
IS_SENSOR_UI1223_M = 0x0018      # WVGA global shutter, monochrome
IS_SENSOR_UI1223_C = 0x0019      # WVGA global shutter, color
IS_SENSOR_UI149X_M = 0x003E      # 10MP rolling shutter, monochrome
IS_SENSOR_UI149X_C = 0x003F      # 10MP rolling shutter, color
IS_SENSOR_UI1225_M = 0x0022      # WVGA global shutter, monochrome, LE model
IS_SENSOR_UI1225_C = 0x0023      # WVGA global shutter, color, LE model
IS_SENSOR_UI1645_C = 0x0025      # SXGA rolling shutter, color, LE model
IS_SENSOR_UI1555_C = 0x0027      # UXGA rolling shutter, color, LE model
IS_SENSOR_UI1545_M = 0x0028      # SXGA rolling shutter, monochrome, LE model
IS_SENSOR_UI1545_C = 0x0029      # SXGA rolling shutter, color, LE model
IS_SENSOR_UI1455_C = 0x002B      # UXGA rolling shutter, color, LE model
IS_SENSOR_UI1465_C = 0x002D      # QXGA rolling shutter, color, LE model
IS_SENSOR_UI1485_M = 0x002E      # 5MP rolling shutter, monochrome, LE model
IS_SENSOR_UI1485_C = 0x002F      # 5MP rolling shutter, color, LE model
IS_SENSOR_UI1495_M = 0x0040      # 10MP rolling shutter, monochrome, LE model
IS_SENSOR_UI1495_C = 0x0041      # 10MP rolling shutter, color, LE model
IS_SENSOR_UI112X_M = 0x004A      # 0768x576, HDR sensor, monochrome
IS_SENSOR_UI112X_C = 0x004B      # 0768x576, HDR sensor, color
IS_SENSOR_UI1008_M = 0x004C
IS_SENSOR_UI1008_C = 0x004D
IS_SENSOR_UIF005_M = 0x0076 
IS_SENSOR_UIF005_C = 0x0077 
IS_SENSOR_UI1005_M = 0x020A 
IS_SENSOR_UI1005_C = 0x020B
IS_SENSOR_UI1240_M = 0x0050      # SXGA global shutter, monochrome
IS_SENSOR_UI1240_C = 0x0051      # SXGA global shutter, color
IS_SENSOR_UI1240_NIR = 0x0062      # SXGA global shutter, NIR
IS_SENSOR_UI1240LE_M = 0x0054      # SXGA global shutter, monochrome, single board
IS_SENSOR_UI1240LE_C = 0x0055      # SXGA global shutter, color, single board
IS_SENSOR_UI1240LE_NIR = 0x0064      # SXGA global shutter, NIR, single board
IS_SENSOR_UI1240ML_M = 0x0066      # SXGA global shutter, monochrome, single board
IS_SENSOR_UI1240ML_C = 0x0067      # SXGA global shutter, color, single board
IS_SENSOR_UI1240ML_NIR = 0x0200      # SXGA global shutter, NIR, single board
IS_SENSOR_UI1243_M_SMI = 0x0078
IS_SENSOR_UI1243_C_SMI = 0x0079
IS_SENSOR_UI1543_M = 0x0032      # SXGA rolling shutter, monochrome, single board
IS_SENSOR_UI1543_C = 0x0033      # SXGA rolling shutter, color, single board
IS_SENSOR_UI1544_M = 0x003A      # SXGA rolling shutter, monochrome, single board
IS_SENSOR_UI1544_C = 0x003B      # SXGA rolling shutter, color, single board
IS_SENSOR_UI1543_M_WO = 0x003C      # SXGA rolling shutter, monochrome, single board
IS_SENSOR_UI1543_C_WO = 0x003D      # SXGA rolling shutter, color, single board
IS_SENSOR_UI1453_C = 0x0035      # UXGA rolling shutter, color, single board
IS_SENSOR_UI1463_C = 0x0037      # QXGA rolling shutter, color, single board
IS_SENSOR_UI1483_M = 0x0038      # QSXG rolling shutter, monochrome, single board
IS_SENSOR_UI1483_C = 0x0039      # QSXG rolling shutter, color, single board
IS_SENSOR_UI1493_M = 0x004E      # 10Mp rolling shutter, monochrome, single board
IS_SENSOR_UI1493_C = 0x004F      # 10MP rolling shutter, color, single board
IS_SENSOR_UI1463_M_WO = 0x0044      # QXGA rolling shutter, monochrome, single board
IS_SENSOR_UI1463_C_WO = 0x0045      # QXGA rolling shutter, color, single board
IS_SENSOR_UI1553_C_WN = 0x0047      # UXGA rolling shutter, color, single board
IS_SENSOR_UI1483_M_WO = 0x0048      # QSXGA rolling shutter, monochrome, single board
IS_SENSOR_UI1483_C_WO = 0x0049      # QSXGA rolling shutter, color, single board
IS_SENSOR_UI1580_M = 0x005A      # 5MP rolling shutter, monochrome
IS_SENSOR_UI1580_C = 0x005B      # 5MP rolling shutter, color
IS_SENSOR_UI1580LE_M = 0x0060      # 5MP rolling shutter, monochrome, single board
IS_SENSOR_UI1580LE_C = 0x0061      # 5MP rolling shutter, color, single board
IS_SENSOR_UI1360M = 0x0068      # 2.2MP global shutter, monochrome
IS_SENSOR_UI1360C = 0x0069      # 2.2MP global shutter, color
IS_SENSOR_UI1360NIR = 0x0212      # 2.2MP global shutter, NIR
IS_SENSOR_UI1370M = 0x006A      # 4.2MP global shutter, monochrome
IS_SENSOR_UI1370C = 0x006B      # 4.2MP global shutter, color
IS_SENSOR_UI1370NIR = 0x0214      # 4.2MP global shutter, NIR
IS_SENSOR_UI1250_M = 0x006C      # 2MP global shutter, monochrome
IS_SENSOR_UI1250_C = 0x006D      # 2MP global shutter, color
IS_SENSOR_UI1250_NIR = 0x006E      # 2MP global shutter, NIR
IS_SENSOR_UI1250LE_M = 0x0070      # 2MP global shutter, monochrome, single board
IS_SENSOR_UI1250LE_C = 0x0071      # 2MP global shutter, color, single board
IS_SENSOR_UI1250LE_NIR = 0x0072      # 2MP global shutter, NIR, single board
IS_SENSOR_UI1250ML_M = 0x0074      # 2MP global shutter, monochrome, single board
IS_SENSOR_UI1250ML_C = 0x0075      # 2MP global shutter, color, single board
IS_SENSOR_UI1250ML_NIR = 0x0202      # 2MP global shutter, NIR, single board
IS_SENSOR_XS = 0x020B      # 5MP rolling shutter, color
IS_SENSOR_UI1493_M_AR = 0x0204
IS_SENSOR_UI1493_C_AR = 0x0205
# CCD Sensors
IS_SENSOR_UI223X_M = 0x0080      # Sony CCD sensor - XGA monochrome
IS_SENSOR_UI223X_C = 0x0081      # Sony CCD sensor - XGA color
IS_SENSOR_UI241X_M = 0x0082      # Sony CCD sensor - VGA monochrome
IS_SENSOR_UI241X_C = 0x0083      # Sony CCD sensor - VGA color
IS_SENSOR_UI234X_M = 0x0084      # Sony CCD sensor - SXGA monochrome
IS_SENSOR_UI234X_C = 0x0085      # Sony CCD sensor - SXGA color
IS_SENSOR_UI221X_M = 0x0088      # Sony CCD sensor - VGA monochrome
IS_SENSOR_UI221X_C = 0x0089      # Sony CCD sensor - VGA color
IS_SENSOR_UI231X_M = 0x0090      # Sony CCD sensor - VGA monochrome
IS_SENSOR_UI231X_C = 0x0091      # Sony CCD sensor - VGA color
IS_SENSOR_UI222X_M = 0x0092      # Sony CCD sensor - CCIR / PAL monochrome
IS_SENSOR_UI222X_C = 0x0093      # Sony CCD sensor - CCIR / PAL color
IS_SENSOR_UI224X_M = 0x0096      # Sony CCD sensor - SXGA monochrome
IS_SENSOR_UI224X_C = 0x0097      # Sony CCD sensor - SXGA color
IS_SENSOR_UI225X_M = 0x0098      # Sony CCD sensor - UXGA monochrome
IS_SENSOR_UI225X_C = 0x0099      # Sony CCD sensor - UXGA color
IS_SENSOR_UI214X_M = 0x009A      # Sony CCD sensor - SXGA monochrome
IS_SENSOR_UI214X_C = 0x009B      # Sony CCD sensor - SXGA color
IS_SENSOR_UI228X_M = 0x009C      # Sony CCD sensor - QXGA monochrome
IS_SENSOR_UI228X_C = 0x009D      # Sony CCD sensor - QXGA color
IS_SENSOR_UI241X_M_R2 = 0x0182      # Sony CCD sensor - VGA monochrome
IS_SENSOR_UI251X_M = 0x0182      # Sony CCD sensor - VGA monochrome
IS_SENSOR_UI241X_C_R2 = 0x0183      # Sony CCD sensor - VGA color
IS_SENSOR_UI251X_C = 0x0183      # Sony CCD sensor - VGA color
IS_SENSOR_UI2130_M = 0x019E      # Sony CCD sensor - WXGA monochrome
IS_SENSOR_UI2130_C = 0x019F      # Sony CCD sensor - WXGA color
IS_SENSOR_PASSIVE_MULTICAST = 0x0F00
# ----------------------------------------------------------------------------
# Error codes
# ----------------------------------------------------------------------------
IS_NO_SUCCESS = -1   # function call failed
IS_SUCCESS = 0   # function call succeeded
IS_INVALID_CAMERA_HANDLE = 1   # camera handle is not valid or zero
IS_INVALID_HANDLE = 1   # a handle other than the camera handle is invalid
IS_IO_REQUEST_FAILED = 2   # an io request to the driver failed
IS_CANT_OPEN_DEVICE = 3   # returned by is_InitCamera
IS_CANT_CLOSE_DEVICE = 4
IS_CANT_SETUP_MEMORY = 5
IS_NO_HWND_FOR_ERROR_REPORT = 6
IS_ERROR_MESSAGE_NOT_CREATED = 7
IS_ERROR_STRING_NOT_FOUND = 8
IS_HOOK_NOT_CREATED = 9
IS_TIMER_NOT_CREATED = 10
IS_CANT_OPEN_REGISTRY = 11
IS_CANT_READ_REGISTRY = 12
IS_CANT_VALIDATE_BOARD = 13
IS_CANT_GIVE_BOARD_ACCESS = 14
IS_NO_IMAGE_MEM_ALLOCATED = 15
IS_CANT_CLEANUP_MEMORY = 16
IS_CANT_COMMUNICATE_WITH_DRIVER = 17
IS_FUNCTION_NOT_SUPPORTED_YET = 18
IS_OPERATING_SYSTEM_NOT_SUPPORTED = 19
IS_INVALID_VIDEO_IN = 20
IS_INVALID_IMG_SIZE = 21
IS_INVALID_ADDRESS = 22
IS_INVALID_VIDEO_MODE = 23
IS_INVALID_AGC_MODE = 24
IS_INVALID_GAMMA_MODE = 25
IS_INVALID_SYNC_LEVEL = 26
IS_INVALID_CBARS_MODE = 27
IS_INVALID_COLOR_MODE = 28
IS_INVALID_SCALE_FACTOR = 29
IS_INVALID_IMAGE_SIZE = 30
IS_INVALID_IMAGE_POS = 31
IS_INVALID_CAPTURE_MODE = 32
IS_INVALID_RISC_PROGRAM = 33
IS_INVALID_BRIGHTNESS = 34
IS_INVALID_CONTRAST = 35
IS_INVALID_SATURATION_U = 36
IS_INVALID_SATURATION_V = 37
IS_INVALID_HUE = 38
IS_INVALID_HOR_FILTER_STEP = 39
IS_INVALID_VERT_FILTER_STEP = 40
IS_INVALID_EEPROM_READ_ADDRESS = 41
IS_INVALID_EEPROM_WRITE_ADDRESS = 42
IS_INVALID_EEPROM_READ_LENGTH = 43
IS_INVALID_EEPROM_WRITE_LENGTH = 44
IS_INVALID_BOARD_INFO_POINTER = 45
IS_INVALID_DISPLAY_MODE = 46
IS_INVALID_ERR_REP_MODE = 47
IS_INVALID_BITS_PIXEL = 48
IS_INVALID_MEMORY_POINTER = 49
IS_FILE_WRITE_OPEN_ERROR = 50
IS_FILE_READ_OPEN_ERROR = 51
IS_FILE_READ_INVALID_BMP_ID = 52
IS_FILE_READ_INVALID_BMP_SIZE = 53
IS_FILE_READ_INVALID_BIT_COUNT = 54
IS_WRONG_KERNEL_VERSION = 55
IS_RISC_INVALID_XLENGTH = 60
IS_RISC_INVALID_YLENGTH = 61
IS_RISC_EXCEED_IMG_SIZE = 62
# DirectDraw Mode errors
IS_DD_MAIN_FAILED = 70
IS_DD_PRIMSURFACE_FAILED = 71
IS_DD_SCRN_SIZE_NOT_SUPPORTED = 72
IS_DD_CLIPPER_FAILED = 73
IS_DD_CLIPPER_HWND_FAILED = 74
IS_DD_CLIPPER_CONNECT_FAILED = 75
IS_DD_BACKSURFACE_FAILED = 76
IS_DD_BACKSURFACE_IN_SYSMEM = 77
IS_DD_MDL_MALLOC_ERR = 78
IS_DD_MDL_SIZE_ERR = 79
IS_DD_CLIP_NO_CHANGE = 80
IS_DD_PRIMMEM_NULL = 81
IS_DD_BACKMEM_NULL = 82
IS_DD_BACKOVLMEM_NULL = 83
IS_DD_OVERLAYSURFACE_FAILED = 84
IS_DD_OVERLAYSURFACE_IN_SYSMEM = 85
IS_DD_OVERLAY_NOT_ALLOWED = 86
IS_DD_OVERLAY_COLKEY_ERR = 87
IS_DD_OVERLAY_NOT_ENABLED = 88
IS_DD_GET_DC_ERROR = 89
IS_DD_DDRAW_DLL_NOT_LOADED = 90
IS_DD_THREAD_NOT_CREATED = 91
IS_DD_CANT_GET_CAPS = 92
IS_DD_NO_OVERLAYSURFACE = 93
IS_DD_NO_OVERLAYSTRETCH = 94
IS_DD_CANT_CREATE_OVERLAYSURFACE = 95
IS_DD_CANT_UPDATE_OVERLAYSURFACE = 96
IS_DD_INVALID_STRETCH = 97
IS_EV_INVALID_EVENT_NUMBER = 100
IS_INVALID_MODE = 101
IS_CANT_FIND_FALCHOOK = 102
IS_CANT_FIND_HOOK = 102
IS_CANT_GET_HOOK_PROC_ADDR = 103
IS_CANT_CHAIN_HOOK_PROC = 104
IS_CANT_SETUP_WND_PROC = 105
IS_HWND_NULL = 106
IS_INVALID_UPDATE_MODE = 107
IS_NO_ACTIVE_IMG_MEM = 108
IS_CANT_INIT_EVENT = 109
IS_FUNC_NOT_AVAIL_IN_OS = 110
IS_CAMERA_NOT_CONNECTED = 111
IS_SEQUENCE_LIST_EMPTY = 112
IS_CANT_ADD_TO_SEQUENCE = 113
IS_LOW_OF_SEQUENCE_RISC_MEM = 114
IS_IMGMEM2FREE_USED_IN_SEQ = 115
IS_IMGMEM_NOT_IN_SEQUENCE_LIST = 116
IS_SEQUENCE_BUF_ALREADY_LOCKED = 117
IS_INVALID_DEVICE_ID = 118
IS_INVALID_BOARD_ID = 119
IS_ALL_DEVICES_BUSY = 120
IS_HOOK_BUSY = 121
IS_TIMED_OUT = 122
IS_NULL_POINTER = 123
IS_WRONG_HOOK_VERSION = 124
IS_INVALID_PARAMETER = 125   # a parameter specified was invalid
IS_NOT_ALLOWED = 126
IS_OUT_OF_MEMORY = 127
IS_INVALID_WHILE_LIVE = 128
IS_ACCESS_VIOLATION = 129   # an internal exception occurred
IS_UNKNOWN_ROP_EFFECT = 130
IS_INVALID_RENDER_MODE = 131
IS_INVALID_THREAD_CONTEXT = 132
IS_NO_HARDWARE_INSTALLED = 133
IS_INVALID_WATCHDOG_TIME = 134
IS_INVALID_WATCHDOG_MODE = 135
IS_INVALID_PASSTHROUGH_IN = 136
IS_ERROR_SETTING_PASSTHROUGH_IN = 137
IS_FAILURE_ON_SETTING_WATCHDOG = 138
IS_NO_USB20 = 139   # the usb port doesnt support usb 2.0
IS_CAPTURE_RUNNING = 140   # there is already a capture running
IS_MEMORY_BOARD_ACTIVATED = 141   # operation could not execute while mboard is enabled
IS_MEMORY_BOARD_DEACTIVATED = 142   # operation could not execute while mboard is disabled
IS_NO_MEMORY_BOARD_CONNECTED = 143   # no memory board connected
IS_TOO_LESS_MEMORY = 144   # image size is above memory capacity
IS_IMAGE_NOT_PRESENT = 145   # requested image is no longer present in the camera
IS_MEMORY_MODE_RUNNING = 146
IS_MEMORYBOARD_DISABLED = 147
IS_TRIGGER_ACTIVATED = 148   # operation could not execute while trigger is enabled
IS_WRONG_KEY = 150
IS_CRC_ERROR = 151
IS_NOT_YET_RELEASED = 152   # this feature is not available yet
IS_NOT_CALIBRATED = 153   # the camera is not calibrated
IS_WAITING_FOR_KERNEL = 154   # a request to the kernel exceeded
IS_NOT_SUPPORTED = 155   # operation mode is not supported
IS_TRIGGER_NOT_ACTIVATED = 156   # operation could not execute while trigger is disabled
IS_OPERATION_ABORTED = 157
IS_BAD_STRUCTURE_SIZE = 158
IS_INVALID_BUFFER_SIZE = 159
IS_INVALID_PIXEL_CLOCK = 160
IS_INVALID_EXPOSURE_TIME = 161
IS_AUTO_EXPOSURE_RUNNING = 162
IS_CANNOT_CREATE_BB_SURF = 163   # error creating backbuffer surface  
IS_CANNOT_CREATE_BB_MIX = 164   # backbuffer mixer surfaces can not be created
IS_BB_OVLMEM_NULL = 165   # backbuffer overlay mem could not be locked  
IS_CANNOT_CREATE_BB_OVL = 166   # backbuffer overlay mem could not be created  
IS_NOT_SUPP_IN_OVL_SURF_MODE = 167   # function not supported in overlay surface mode  
IS_INVALID_SURFACE = 168   # surface invalid
IS_SURFACE_LOST = 169   # surface has been lost  
IS_RELEASE_BB_OVL_DC = 170   # error releasing backbuffer overlay DC  
IS_BB_TIMER_NOT_CREATED = 171   # backbuffer timer could not be created  
IS_BB_OVL_NOT_EN = 172   # backbuffer overlay has not been enabled  
IS_ONLY_IN_BB_MODE = 173   # only possible in backbuffer mode 
IS_INVALID_COLOR_FORMAT = 174   # invalid color format
IS_INVALID_WB_BINNING_MODE = 175   # invalid binning mode for AWB 
IS_INVALID_I2C_DEVICE_ADDRESS = 176   # invalid I2C device address
IS_COULD_NOT_CONVERT = 177   # current image couldn't be converted
IS_TRANSFER_ERROR = 178   # transfer failed
IS_PARAMETER_SET_NOT_PRESENT = 179   # the parameter set is not present
IS_INVALID_CAMERA_TYPE = 180   # the camera type in the ini file doesn't match
IS_INVALID_HOST_IP_HIBYTE = 181   # HIBYTE of host address is invalid
IS_CM_NOT_SUPP_IN_CURR_DISPLAYMODE = 182   # color mode is not supported in the current display mode
IS_NO_IR_FILTER = 183
IS_STARTER_FW_UPLOAD_NEEDED = 184   # device starter firmware is not compatible    
IS_DR_LIBRARY_NOT_FOUND = 185   # the DirectRender library could not be found
IS_DR_DEVICE_OUT_OF_MEMORY = 186   # insufficient graphics adapter video memory
IS_DR_CANNOT_CREATE_SURFACE = 187   # the image or overlay surface could not be created
IS_DR_CANNOT_CREATE_VERTEX_BUFFER = 188   # the vertex buffer could not be created
IS_DR_CANNOT_CREATE_TEXTURE = 189   # the texture could not be created  
IS_DR_CANNOT_LOCK_OVERLAY_SURFACE = 190   # the overlay surface could not be locked
IS_DR_CANNOT_UNLOCK_OVERLAY_SURFACE = 191   # the overlay surface could not be unlocked
IS_DR_CANNOT_GET_OVERLAY_DC = 192   # cannot get the overlay surface DC 
IS_DR_CANNOT_RELEASE_OVERLAY_DC = 193   # cannot release the overlay surface DC
IS_DR_DEVICE_CAPS_INSUFFICIENT = 194   # insufficient graphics adapter capabilities
IS_INCOMPATIBLE_SETTING = 195   # Operation is not possible because of another incompatible setting
IS_DR_NOT_ALLOWED_WHILE_DC_IS_ACTIVE = 196   # user App still has DC handle.
IS_DEVICE_ALREADY_PAIRED = 197   # The device is already paired
IS_SUBNETMASK_MISMATCH = 198   # The subnetmasks of the device and the adapter differ
IS_SUBNET_MISMATCH = 199   # The subnets of the device and the adapter differ
IS_INVALID_IP_CONFIGURATION = 200   # The IP configuation of the device is invalid
IS_DEVICE_NOT_COMPATIBLE = 201   # The device is incompatible to the driver
IS_NETWORK_FRAME_SIZE_INCOMPATIBLE = 202   # The frame size settings of the device and the network adapter are incompatible
IS_NETWORK_CONFIGURATION_INVALID = 203   # The network adapter configuration is invalid
IS_ERROR_CPU_IDLE_STATES_CONFIGURATION = 204   # The setting of the CPU idle state configuration failed
IS_DEVICE_BUSY = 205   # The device is busy. The operation must be executed again later.
IS_SENSOR_INITIALIZATION_FAILED = 206   # The sensor initialization failed
# ----------------------------------------------------------------------------
# common definitions
# ----------------------------------------------------------------------------
IS_OFF = 0
IS_ON = 1
IS_IGNORE_PARAMETER = -1
# ----------------------------------------------------------------------------
#  device enumeration
# ----------------------------------------------------------------------------
IS_USE_DEVICE_ID = 0x8000L
IS_ALLOW_STARTER_FW_UPLOAD = 0x10000L
# ----------------------------------------------------------------------------
# AutoExit enable/disable
# ----------------------------------------------------------------------------
IS_GET_AUTO_EXIT_ENABLED = 0x8000
IS_DISABLE_AUTO_EXIT = 0
IS_ENABLE_AUTO_EXIT = 1
# ----------------------------------------------------------------------------
# live/freeze parameters
# ----------------------------------------------------------------------------
IS_GET_LIVE = 0x8000
IS_WAIT = 0x0001
IS_DONT_WAIT = 0x0000
IS_FORCE_VIDEO_STOP = 0x4000
IS_FORCE_VIDEO_START = 0x4000
IS_USE_NEXT_MEM = 0x8000
# ----------------------------------------------------------------------------
# video finish constants
# ----------------------------------------------------------------------------
IS_VIDEO_NOT_FINISH = 0
IS_VIDEO_FINISH = 1
# ----------------------------------------------------------------------------
# bitmap render modes
# ----------------------------------------------------------------------------
IS_GET_RENDER_MODE = 0x8000
IS_RENDER_DISABLED = 0x0000
IS_RENDER_NORMAL = 0x0001
IS_RENDER_FIT_TO_WINDOW = 0x0002
IS_RENDER_DOWNSCALE_1_2 = 0x0004
IS_RENDER_MIRROR_UPDOWN = 0x0010
IS_RENDER_PLANAR_COLOR_RED = 0x0080
IS_RENDER_PLANAR_COLOR_GREEN = 0x0100
IS_RENDER_PLANAR_COLOR_BLUE = 0x0200
IS_RENDER_PLANAR_MONO_RED = 0x0400
IS_RENDER_PLANAR_MONO_GREEN = 0x0800
IS_RENDER_PLANAR_MONO_BLUE = 0x1000
IS_RENDER_ROTATE_90 = 0x0020
IS_RENDER_ROTATE_180 = 0x0040
IS_RENDER_ROTATE_270 = 0x2000
IS_USE_AS_DC_STRUCTURE = 0x4000
IS_USE_AS_DC_HANDLE = 0x8000
# ----------------------------------------------------------------------------
# Trigger modes
# ----------------------------------------------------------------------------
IS_GET_EXTERNALTRIGGER = 0x8000
IS_GET_TRIGGER_STATUS = 0x8001
IS_GET_TRIGGER_MASK = 0x8002
IS_GET_TRIGGER_INPUTS = 0x8003
IS_GET_SUPPORTED_TRIGGER_MODE = 0x8004
IS_GET_TRIGGER_COUNTER = 0x8000
IS_SET_TRIGGER_MASK = 0x0100
IS_SET_TRIGGER_CONTINUOUS = 0x1000
IS_SET_TRIGGER_OFF = 0x0000
IS_SET_TRIGGER_HI_LO = (IS_SET_TRIGGER_CONTINUOUS | 0x0001) 
IS_SET_TRIGGER_LO_HI = (IS_SET_TRIGGER_CONTINUOUS | 0x0002) 
IS_SET_TRIGGER_SOFTWARE = (IS_SET_TRIGGER_CONTINUOUS | 0x0008) 
IS_SET_TRIGGER_HI_LO_SYNC = 0x0010
IS_SET_TRIGGER_LO_HI_SYNC = 0x0020
IS_SET_TRIGGER_PRE_HI_LO = (IS_SET_TRIGGER_CONTINUOUS | 0x0040)
IS_SET_TRIGGER_PRE_LO_HI = (IS_SET_TRIGGER_CONTINUOUS | 0x0080)
IS_GET_TRIGGER_DELAY = 0x8000
IS_GET_MIN_TRIGGER_DELAY = 0x8001
IS_GET_MAX_TRIGGER_DELAY = 0x8002
IS_GET_TRIGGER_DELAY_GRANULARITY = 0x8003
# ----------------------------------------------------------------------------
# Timing
# ----------------------------------------------------------------------------
# Pixelclock
IS_GET_PIXEL_CLOCK = 0x8000
IS_GET_DEFAULT_PIXEL_CLK = 0x8001
IS_GET_PIXEL_CLOCK_INC = 0x8005
# Frame rate
IS_GET_FRAMERATE = 0x8000
IS_GET_DEFAULT_FRAMERATE = 0x8001
# ----------------------------------------------------------------------------
# Gain definitions
# ----------------------------------------------------------------------------
IS_GET_MASTER_GAIN = 0x8000
IS_GET_RED_GAIN = 0x8001
IS_GET_GREEN_GAIN = 0x8002
IS_GET_BLUE_GAIN = 0x8003
IS_GET_DEFAULT_MASTER = 0x8004
IS_GET_DEFAULT_RED = 0x8005
IS_GET_DEFAULT_GREEN = 0x8006
IS_GET_DEFAULT_BLUE = 0x8007
IS_GET_GAINBOOST = 0x8008
IS_SET_GAINBOOST_ON = 0x0001
IS_SET_GAINBOOST_OFF = 0x0000
IS_GET_SUPPORTED_GAINBOOST = 0x0002
IS_MIN_GAIN = 0
IS_MAX_GAIN = 100
# ----------------------------------------------------------------------------
# Gain factor definitions
# ----------------------------------------------------------------------------
IS_GET_MASTER_GAIN_FACTOR = 0x8000
IS_GET_RED_GAIN_FACTOR = 0x8001
IS_GET_GREEN_GAIN_FACTOR = 0x8002
IS_GET_BLUE_GAIN_FACTOR = 0x8003
IS_SET_MASTER_GAIN_FACTOR = 0x8004
IS_SET_RED_GAIN_FACTOR = 0x8005
IS_SET_GREEN_GAIN_FACTOR = 0x8006
IS_SET_BLUE_GAIN_FACTOR = 0x8007
IS_GET_DEFAULT_MASTER_GAIN_FACTOR = 0x8008
IS_GET_DEFAULT_RED_GAIN_FACTOR = 0x8009
IS_GET_DEFAULT_GREEN_GAIN_FACTOR = 0x800a
IS_GET_DEFAULT_BLUE_GAIN_FACTOR = 0x800b
IS_INQUIRE_MASTER_GAIN_FACTOR = 0x800c
IS_INQUIRE_RED_GAIN_FACTOR = 0x800d
IS_INQUIRE_GREEN_GAIN_FACTOR = 0x800e
IS_INQUIRE_BLUE_GAIN_FACTOR = 0x800f
# ----------------------------------------------------------------------------
# Global Shutter definitions
# ----------------------------------------------------------------------------
IS_SET_GLOBAL_SHUTTER_ON = 0x0001
IS_SET_GLOBAL_SHUTTER_OFF = 0x0000
IS_GET_GLOBAL_SHUTTER = 0x0010
IS_GET_SUPPORTED_GLOBAL_SHUTTER = 0x0020
# ----------------------------------------------------------------------------
# Black level definitions
# ----------------------------------------------------------------------------
IS_GET_BL_COMPENSATION = 0x8000
IS_GET_BL_OFFSET = 0x8001
IS_GET_BL_DEFAULT_MODE = 0x8002
IS_GET_BL_DEFAULT_OFFSET = 0x8003
IS_GET_BL_SUPPORTED_MODE = 0x8004
IS_BL_COMPENSATION_DISABLE = 0
IS_BL_COMPENSATION_ENABLE = 1
IS_BL_COMPENSATION_OFFSET = 32
IS_MIN_BL_OFFSET = 0
IS_MAX_BL_OFFSET = 255
# ----------------------------------------------------------------------------
# Hardware gamma definitions
# ----------------------------------------------------------------------------
IS_GET_HW_GAMMA = 0x8000
IS_GET_HW_SUPPORTED_GAMMA = 0x8001
IS_SET_HW_GAMMA_OFF = 0x0000
IS_SET_HW_GAMMA_ON = 0x0001
# ----------------------------------------------------------------------------
# Image parameters
# ----------------------------------------------------------------------------
# Saturation
IS_GET_SATURATION_U = 0x8000
IS_MIN_SATURATION_U = 0
IS_MAX_SATURATION_U = 200
IS_DEFAULT_SATURATION_U = 100
IS_GET_SATURATION_V = 0x8001
IS_MIN_SATURATION_V = 0
IS_MAX_SATURATION_V = 200
IS_DEFAULT_SATURATION_V = 100
# ----------------------------------------------------------------------------
# Image position and size
# ----------------------------------------------------------------------------
IS_AOI_IMAGE_SET_AOI = 0x0001
IS_AOI_IMAGE_GET_AOI = 0x0002
IS_AOI_IMAGE_SET_POS = 0x0003
IS_AOI_IMAGE_GET_POS = 0x0004
IS_AOI_IMAGE_SET_SIZE = 0x0005
IS_AOI_IMAGE_GET_SIZE = 0x0006
IS_AOI_IMAGE_GET_POS_MIN = 0x0007
IS_AOI_IMAGE_GET_SIZE_MIN = 0x0008
IS_AOI_IMAGE_GET_POS_MAX = 0x0009
IS_AOI_IMAGE_GET_SIZE_MAX = 0x0010
IS_AOI_IMAGE_GET_POS_INC = 0x0011
IS_AOI_IMAGE_GET_SIZE_INC = 0x0012
IS_AOI_IMAGE_GET_POS_X_ABS = 0x0013
IS_AOI_IMAGE_GET_POS_Y_ABS = 0x0014
IS_AOI_IMAGE_GET_ORIGINAL_AOI = 0x0015
IS_AOI_IMAGE_POS_ABSOLUTE = 0x10000000
IS_AOI_IMAGE_SET_POS_FAST = 0x0020
IS_AOI_IMAGE_GET_POS_FAST_SUPPORTED = 0x0021
IS_AOI_AUTO_BRIGHTNESS_SET_AOI = 0x0030
IS_AOI_AUTO_BRIGHTNESS_GET_AOI = 0x0031
IS_AOI_AUTO_WHITEBALANCE_SET_AOI = 0x0032
IS_AOI_AUTO_WHITEBALANCE_GET_AOI = 0x0033
IS_AOI_MULTI_GET_SUPPORTED_MODES = 0x0100
IS_AOI_MULTI_SET_AOI = 0x0200
IS_AOI_MULTI_GET_AOI = 0x0400
IS_AOI_MULTI_DISABLE_AOI = 0x0800
IS_AOI_MULTI_MODE_X_Y_AXES = 0x0001
IS_AOI_MULTI_MODE_Y_AXES = 0x0002
IS_AOI_SEQUENCE_GET_SUPPORTED = 0x0050
IS_AOI_SEQUENCE_SET_PARAMS = 0x0051
IS_AOI_SEQUENCE_GET_PARAMS = 0x0052
IS_AOI_SEQUENCE_SET_ENABLE = 0x0053
IS_AOI_SEQUENCE_GET_ENABLE = 0x0054
IS_AOI_SEQUENCE_INDEX_AOI_1 = 0
IS_AOI_SEQUENCE_INDEX_AOI_2 = 1
IS_AOI_SEQUENCE_INDEX_AOI_3 = 2
IS_AOI_SEQUENCE_INDEX_AOI_4 = 4
# ----------------------------------------------------------------------------
# ROP effect constants
# ----------------------------------------------------------------------------
IS_GET_ROP_EFFECT = 0x8000
IS_GET_SUPPORTED_ROP_EFFECT = 0x8001
IS_SET_ROP_NONE = 0
IS_SET_ROP_MIRROR_UPDOWN = 8
IS_SET_ROP_MIRROR_UPDOWN_ODD = 16
IS_SET_ROP_MIRROR_UPDOWN_EVEN = 32
IS_SET_ROP_MIRROR_LEFTRIGHT = 64
# ----------------------------------------------------------------------------
# Subsampling
# ----------------------------------------------------------------------------
IS_GET_SUBSAMPLING = 0x8000
IS_GET_SUPPORTED_SUBSAMPLING = 0x8001
IS_GET_SUBSAMPLING_TYPE = 0x8002
IS_GET_SUBSAMPLING_FACTOR_HORIZONTAL = 0x8004
IS_GET_SUBSAMPLING_FACTOR_VERTICAL = 0x8008
IS_SUBSAMPLING_DISABLE = 0x00
IS_SUBSAMPLING_2X_VERTICAL = 0x0001
IS_SUBSAMPLING_2X_HORIZONTAL = 0x0002
IS_SUBSAMPLING_4X_VERTICAL = 0x0004
IS_SUBSAMPLING_4X_HORIZONTAL = 0x0008
IS_SUBSAMPLING_3X_VERTICAL = 0x0010
IS_SUBSAMPLING_3X_HORIZONTAL = 0x0020
IS_SUBSAMPLING_5X_VERTICAL = 0x0040
IS_SUBSAMPLING_5X_HORIZONTAL = 0x0080
IS_SUBSAMPLING_6X_VERTICAL = 0x0100
IS_SUBSAMPLING_6X_HORIZONTAL = 0x0200
IS_SUBSAMPLING_8X_VERTICAL = 0x0400
IS_SUBSAMPLING_8X_HORIZONTAL = 0x0800
IS_SUBSAMPLING_16X_VERTICAL = 0x1000
IS_SUBSAMPLING_16X_HORIZONTAL = 0x2000
IS_SUBSAMPLING_COLOR = 0x01
IS_SUBSAMPLING_MONO = 0x02
IS_SUBSAMPLING_MASK_VERTICAL = (IS_SUBSAMPLING_2X_VERTICAL | IS_SUBSAMPLING_4X_VERTICAL | IS_SUBSAMPLING_3X_VERTICAL | IS_SUBSAMPLING_5X_VERTICAL | IS_SUBSAMPLING_6X_VERTICAL | IS_SUBSAMPLING_8X_VERTICAL | IS_SUBSAMPLING_16X_VERTICAL)
IS_SUBSAMPLING_MASK_HORIZONTAL = (IS_SUBSAMPLING_2X_HORIZONTAL | IS_SUBSAMPLING_4X_HORIZONTAL | IS_SUBSAMPLING_3X_HORIZONTAL | IS_SUBSAMPLING_5X_HORIZONTAL | IS_SUBSAMPLING_6X_HORIZONTAL | IS_SUBSAMPLING_8X_HORIZONTAL | IS_SUBSAMPLING_16X_HORIZONTAL)
# ----------------------------------------------------------------------------
# Binning
# ----------------------------------------------------------------------------
IS_GET_BINNING = 0x8000
IS_GET_SUPPORTED_BINNING = 0x8001
IS_GET_BINNING_TYPE = 0x8002
IS_GET_BINNING_FACTOR_HORIZONTAL = 0x8004
IS_GET_BINNING_FACTOR_VERTICAL = 0x8008
IS_BINNING_DISABLE = 0x00
IS_BINNING_2X_VERTICAL = 0x0001
IS_BINNING_2X_HORIZONTAL = 0x0002
IS_BINNING_4X_VERTICAL = 0x0004
IS_BINNING_4X_HORIZONTAL = 0x0008
IS_BINNING_3X_VERTICAL = 0x0010
IS_BINNING_3X_HORIZONTAL = 0x0020
IS_BINNING_5X_VERTICAL = 0x0040
IS_BINNING_5X_HORIZONTAL = 0x0080
IS_BINNING_6X_VERTICAL = 0x0100
IS_BINNING_6X_HORIZONTAL = 0x0200
IS_BINNING_8X_VERTICAL = 0x0400
IS_BINNING_8X_HORIZONTAL = 0x0800
IS_BINNING_16X_VERTICAL = 0x1000
IS_BINNING_16X_HORIZONTAL = 0x2000
IS_BINNING_COLOR = 0x01
IS_BINNING_MONO = 0x02
IS_BINNING_MASK_VERTICAL = (IS_BINNING_2X_VERTICAL | IS_BINNING_3X_VERTICAL | IS_BINNING_4X_VERTICAL | IS_BINNING_5X_VERTICAL | IS_BINNING_6X_VERTICAL | IS_BINNING_8X_VERTICAL | IS_BINNING_16X_VERTICAL)
IS_BINNING_MASK_HORIZONTAL = (IS_BINNING_2X_HORIZONTAL | IS_BINNING_3X_HORIZONTAL | IS_BINNING_4X_HORIZONTAL | IS_BINNING_5X_HORIZONTAL | IS_BINNING_6X_HORIZONTAL | IS_BINNING_8X_HORIZONTAL | IS_BINNING_16X_HORIZONTAL)
# ----------------------------------------------------------------------------
# Auto Control Parameter
# ----------------------------------------------------------------------------
IS_SET_ENABLE_AUTO_GAIN = 0x8800
IS_GET_ENABLE_AUTO_GAIN = 0x8801
IS_SET_ENABLE_AUTO_SHUTTER = 0x8802
IS_GET_ENABLE_AUTO_SHUTTER = 0x8803
IS_SET_ENABLE_AUTO_WHITEBALANCE = 0x8804
IS_GET_ENABLE_AUTO_WHITEBALANCE = 0x8805
IS_SET_ENABLE_AUTO_FRAMERATE = 0x8806
IS_GET_ENABLE_AUTO_FRAMERATE = 0x8807
IS_SET_ENABLE_AUTO_SENSOR_GAIN = 0x8808
IS_GET_ENABLE_AUTO_SENSOR_GAIN = 0x8809
IS_SET_ENABLE_AUTO_SENSOR_SHUTTER = 0x8810
IS_GET_ENABLE_AUTO_SENSOR_SHUTTER = 0x8811
IS_SET_ENABLE_AUTO_SENSOR_GAIN_SHUTTER = 0x8812
IS_GET_ENABLE_AUTO_SENSOR_GAIN_SHUTTER = 0x8813
IS_SET_ENABLE_AUTO_SENSOR_FRAMERATE = 0x8814
IS_GET_ENABLE_AUTO_SENSOR_FRAMERATE = 0x8815
IS_SET_ENABLE_AUTO_SENSOR_WHITEBALANCE = 0x8816
IS_GET_ENABLE_AUTO_SENSOR_WHITEBALANCE = 0x8817
IS_SET_AUTO_REFERENCE = 0x8000
IS_GET_AUTO_REFERENCE = 0x8001
IS_SET_AUTO_GAIN_MAX = 0x8002
IS_GET_AUTO_GAIN_MAX = 0x8003
IS_SET_AUTO_SHUTTER_MAX = 0x8004
IS_GET_AUTO_SHUTTER_MAX = 0x8005
IS_SET_AUTO_SPEED = 0x8006
IS_GET_AUTO_SPEED = 0x8007
IS_SET_AUTO_WB_OFFSET = 0x8008
IS_GET_AUTO_WB_OFFSET = 0x8009
IS_SET_AUTO_WB_GAIN_RANGE = 0x800A
IS_GET_AUTO_WB_GAIN_RANGE = 0x800B
IS_SET_AUTO_WB_SPEED = 0x800C
IS_GET_AUTO_WB_SPEED = 0x800D
IS_SET_AUTO_WB_ONCE = 0x800E
IS_GET_AUTO_WB_ONCE = 0x800F
IS_SET_AUTO_BRIGHTNESS_ONCE = 0x8010
IS_GET_AUTO_BRIGHTNESS_ONCE = 0x8011
IS_SET_AUTO_HYSTERESIS = 0x8012
IS_GET_AUTO_HYSTERESIS = 0x8013
IS_GET_AUTO_HYSTERESIS_RANGE = 0x8014
IS_SET_AUTO_WB_HYSTERESIS = 0x8015
IS_GET_AUTO_WB_HYSTERESIS = 0x8016
IS_GET_AUTO_WB_HYSTERESIS_RANGE = 0x8017
IS_SET_AUTO_SKIPFRAMES = 0x8018
IS_GET_AUTO_SKIPFRAMES = 0x8019
IS_GET_AUTO_SKIPFRAMES_RANGE = 0x801A
IS_SET_AUTO_WB_SKIPFRAMES = 0x801B
IS_GET_AUTO_WB_SKIPFRAMES = 0x801C
IS_GET_AUTO_WB_SKIPFRAMES_RANGE = 0x801D
IS_SET_SENS_AUTO_SHUTTER_PHOTOM = 0x801E
IS_SET_SENS_AUTO_GAIN_PHOTOM = 0x801F
IS_GET_SENS_AUTO_SHUTTER_PHOTOM = 0x8020
IS_GET_SENS_AUTO_GAIN_PHOTOM = 0x8021
IS_GET_SENS_AUTO_SHUTTER_PHOTOM_DEF = 0x8022
IS_GET_SENS_AUTO_GAIN_PHOTOM_DEF = 0x8023
IS_SET_SENS_AUTO_CONTRAST_CORRECTION = 0x8024
IS_GET_SENS_AUTO_CONTRAST_CORRECTION = 0x8025
IS_GET_SENS_AUTO_CONTRAST_CORRECTION_RANGE = 0x8026
IS_GET_SENS_AUTO_CONTRAST_CORRECTION_INC = 0x8027
IS_GET_SENS_AUTO_CONTRAST_CORRECTION_DEF = 0x8028
IS_SET_SENS_AUTO_CONTRAST_FDT_AOI_ENABLE = 0x8029
IS_GET_SENS_AUTO_CONTRAST_FDT_AOI_ENABLE = 0x8030
IS_SET_SENS_AUTO_BACKLIGHT_COMP = 0x8031
IS_GET_SENS_AUTO_BACKLIGHT_COMP = 0x8032
IS_GET_SENS_AUTO_BACKLIGHT_COMP_RANGE = 0x8033
IS_GET_SENS_AUTO_BACKLIGHT_COMP_INC = 0x8034
IS_GET_SENS_AUTO_BACKLIGHT_COMP_DEF = 0x8035
IS_SET_ANTI_FLICKER_MODE = 0x8036
IS_GET_ANTI_FLICKER_MODE = 0x8037
IS_GET_ANTI_FLICKER_MODE_DEF = 0x8038
IS_GET_AUTO_REFERENCE_DEF = 0x8039
IS_GET_AUTO_WB_OFFSET_DEF = 0x803A
IS_GET_AUTO_WB_OFFSET_MIN = 0x803B
IS_GET_AUTO_WB_OFFSET_MAX = 0x803C
# ----------------------------------------------------------------------------
# Auto Control definitions
# ----------------------------------------------------------------------------
IS_MIN_AUTO_BRIGHT_REFERENCE = 0
IS_MAX_AUTO_BRIGHT_REFERENCE = 255
IS_DEFAULT_AUTO_BRIGHT_REFERENCE = 128
IS_MIN_AUTO_SPEED = 0
IS_MAX_AUTO_SPEED = 100
IS_DEFAULT_AUTO_SPEED = 50
IS_DEFAULT_AUTO_WB_OFFSET = 0
IS_MIN_AUTO_WB_OFFSET = -50
IS_MAX_AUTO_WB_OFFSET = 50
IS_DEFAULT_AUTO_WB_SPEED = 50
IS_MIN_AUTO_WB_SPEED = 0
IS_MAX_AUTO_WB_SPEED = 100
IS_MIN_AUTO_WB_REFERENCE = 0
IS_MAX_AUTO_WB_REFERENCE = 255
# ----------------------------------------------------------------------------
# AOI types to set/get
# ----------------------------------------------------------------------------
IS_SET_AUTO_BRIGHT_AOI = 0x8000
IS_GET_AUTO_BRIGHT_AOI = 0x8001
IS_SET_IMAGE_AOI = 0x8002
IS_GET_IMAGE_AOI = 0x8003
IS_SET_AUTO_WB_AOI = 0x8004
IS_GET_AUTO_WB_AOI = 0x8005
# ----------------------------------------------------------------------------
# pixel formats
# ----------------------------------------------------------------------------
IS_GET_COLOR_MODE = 0x8000
IS_CM_FORMAT_PLANAR = 0x2000
IS_CM_FORMAT_MASK = 0x2000
#! \brief BGR vs. RGB order 
IS_CM_ORDER_BGR = 0x0000
IS_CM_ORDER_RGB = 0x0080
IS_CM_ORDER_MASK = 0x0080 
#! \brief This flag indicates whether a packed source pixelformat should be used (also for the debayered pixel formats) 
IS_CM_PREFER_PACKED_SOURCE_FORMAT = 0x4000
#! \brief Raw sensor data, occupies 8 bits 
IS_CM_SENSOR_RAW8 = 11
#! \brief Raw sensor data, occupies 16 bits 
IS_CM_SENSOR_RAW10 = 33
#! \brief Raw sensor data, occupies 16 bits 
IS_CM_SENSOR_RAW12 = 27
#! \brief Raw sensor data, occupies 16 bits 
IS_CM_SENSOR_RAW16 = 29
#! \brief Mono, occupies 8 bits 
IS_CM_MONO8 = 6
#! \brief Mono, occupies 16 bits 
IS_CM_MONO10 = 34
#! \brief Mono, occupies 16 bits 
IS_CM_MONO12 = 26
#! \brief Mono, occupies 16 bits 
IS_CM_MONO16 = 28
#! \brief BGR (5 5 5 1), 1 bit not used, occupies 16 bits 
IS_CM_BGR5_PACKED = (3  | IS_CM_ORDER_BGR)
#! \brief BGR (5 6 5), occupies 16 bits 
IS_CM_BGR565_PACKED = (2  | IS_CM_ORDER_BGR)
#! \brief BGR and RGB (8 8 8), occupies 24 bits 
IS_CM_RGB8_PACKED = (1  | IS_CM_ORDER_RGB)
IS_CM_BGR8_PACKED = (1  | IS_CM_ORDER_BGR)
#! \brief BGRA and RGBA (8 8 8 8), alpha not used, occupies 32 bits 
IS_CM_RGBA8_PACKED = (0  | IS_CM_ORDER_RGB)
IS_CM_BGRA8_PACKED = (0  | IS_CM_ORDER_BGR)
#! \brief BGRY and RGBY (8 8 8 8), occupies 32 bits 
IS_CM_RGBY8_PACKED = (24 | IS_CM_ORDER_RGB)
IS_CM_BGRY8_PACKED = (24 | IS_CM_ORDER_BGR)
#! \brief BGR and RGB (10 10 10 2), 2 bits not used, occupies 32 bits, debayering is done from 12 bit raw  
IS_CM_RGB10_PACKED = (25 | IS_CM_ORDER_RGB)
IS_CM_BGR10_PACKED = (25 | IS_CM_ORDER_BGR)
#! \brief BGR and RGB (10(16) 10(16) 10(16)), 6 MSB bits not used respectively, occupies 48 bits 
IS_CM_RGB10_UNPACKED = (35 | IS_CM_ORDER_RGB)
IS_CM_BGR10_UNPACKED = (35 | IS_CM_ORDER_BGR)
#! \brief BGR and RGB (12(16) 12(16) 12(16)), 4 MSB bits not used respectively, occupies 48 bits 
IS_CM_RGB12_UNPACKED = (30 | IS_CM_ORDER_RGB)
IS_CM_BGR12_UNPACKED = (30 | IS_CM_ORDER_BGR)
#! \brief BGRA and RGBA (12(16) 12(16) 12(16) 16), 4 MSB bits not used respectively, alpha not used, occupies 64 bits 
IS_CM_RGBA12_UNPACKED = (31 | IS_CM_ORDER_RGB)
IS_CM_BGRA12_UNPACKED = (31 | IS_CM_ORDER_BGR)
IS_CM_JPEG = 32
#! \brief YUV422 (8 8), occupies 16 bits 
IS_CM_UYVY_PACKED = 12
IS_CM_UYVY_MONO_PACKED = 13
IS_CM_UYVY_BAYER_PACKED = 14
#! \brief YCbCr422 (8 8), occupies 16 bits 
IS_CM_CBYCRY_PACKED = 23
#! \brief RGB planar (8 8 8), occupies 24 bits 
IS_CM_RGB8_PLANAR = (1 | IS_CM_ORDER_RGB | IS_CM_FORMAT_PLANAR)
IS_CM_ALL_POSSIBLE = 0xFFFF
IS_CM_MODE_MASK = 0x007F
# ----------------------------------------------------------------------------
# Hotpixel correction
# ----------------------------------------------------------------------------
IS_HOTPIXEL_DISABLE_CORRECTION = 0x0000
IS_HOTPIXEL_ENABLE_SENSOR_CORRECTION = 0x0001
IS_HOTPIXEL_ENABLE_CAMERA_CORRECTION = 0x0002
IS_HOTPIXEL_ENABLE_SOFTWARE_USER_CORRECTION = 0x0004
IS_HOTPIXEL_DISABLE_SENSOR_CORRECTION = 0x0008
IS_HOTPIXEL_GET_CORRECTION_MODE = 0x8000
IS_HOTPIXEL_GET_SUPPORTED_CORRECTION_MODES = 0x8001
IS_HOTPIXEL_GET_SOFTWARE_USER_LIST_EXISTS = 0x8100
IS_HOTPIXEL_GET_SOFTWARE_USER_LIST_NUMBER = 0x8101
IS_HOTPIXEL_GET_SOFTWARE_USER_LIST = 0x8102
IS_HOTPIXEL_SET_SOFTWARE_USER_LIST = 0x8103
IS_HOTPIXEL_SAVE_SOFTWARE_USER_LIST = 0x8104
IS_HOTPIXEL_LOAD_SOFTWARE_USER_LIST = 0x8105
IS_HOTPIXEL_GET_CAMERA_FACTORY_LIST_EXISTS = 0x8106
IS_HOTPIXEL_GET_CAMERA_FACTORY_LIST_NUMBER = 0x8107
IS_HOTPIXEL_GET_CAMERA_FACTORY_LIST = 0x8108
IS_HOTPIXEL_GET_CAMERA_USER_LIST_EXISTS = 0x8109
IS_HOTPIXEL_GET_CAMERA_USER_LIST_NUMBER = 0x810A
IS_HOTPIXEL_GET_CAMERA_USER_LIST = 0x810B
IS_HOTPIXEL_SET_CAMERA_USER_LIST = 0x810C
IS_HOTPIXEL_GET_CAMERA_USER_LIST_MAX_NUMBER = 0x810D
IS_HOTPIXEL_DELETE_CAMERA_USER_LIST = 0x810E
IS_HOTPIXEL_GET_MERGED_CAMERA_LIST_NUMBER = 0x810F
IS_HOTPIXEL_GET_MERGED_CAMERA_LIST = 0x8110
IS_HOTPIXEL_SAVE_SOFTWARE_USER_LIST_UNICODE = 0x8111
IS_HOTPIXEL_LOAD_SOFTWARE_USER_LIST_UNICODE = 0x8112
# ----------------------------------------------------------------------------
# color correction definitions
# ----------------------------------------------------------------------------
IS_GET_CCOR_MODE = 0x8000
IS_GET_SUPPORTED_CCOR_MODE = 0x8001
IS_GET_DEFAULT_CCOR_MODE = 0x8002
IS_GET_CCOR_FACTOR = 0x8003
IS_GET_CCOR_FACTOR_MIN = 0x8004
IS_GET_CCOR_FACTOR_MAX = 0x8005
IS_GET_CCOR_FACTOR_DEFAULT = 0x8006
IS_CCOR_DISABLE = 0x0000
IS_CCOR_ENABLE = 0x0001
IS_CCOR_ENABLE_NORMAL = IS_CCOR_ENABLE
IS_CCOR_ENABLE_BG40_ENHANCED = 0x0002
IS_CCOR_ENABLE_HQ_ENHANCED = 0x0004
IS_CCOR_SET_IR_AUTOMATIC = 0x0080
IS_CCOR_FACTOR = 0x0100
IS_CCOR_ENABLE_MASK = (IS_CCOR_ENABLE_NORMAL | IS_CCOR_ENABLE_BG40_ENHANCED | IS_CCOR_ENABLE_HQ_ENHANCED)
# ----------------------------------------------------------------------------
# bayer algorithm modes
# ----------------------------------------------------------------------------
IS_GET_BAYER_CV_MODE = 0x8000
IS_SET_BAYER_CV_NORMAL = 0x0000
IS_SET_BAYER_CV_BETTER = 0x0001
IS_SET_BAYER_CV_BEST = 0x0002
# ----------------------------------------------------------------------------
# color converter modes
# ----------------------------------------------------------------------------
IS_CONV_MODE_NONE = 0x0000
IS_CONV_MODE_SOFTWARE = 0x0001
IS_CONV_MODE_SOFTWARE_3X3 = 0x0002
IS_CONV_MODE_SOFTWARE_5X5 = 0x0004
IS_CONV_MODE_HARDWARE_3X3 = 0x0008
IS_CONV_MODE_OPENCL_3X3 = 0x0020
IS_CONV_MODE_OPENCL_5X5 = 0x0040
IS_CONV_MODE_JPEG = 0x0100
# ----------------------------------------------------------------------------
# Edge enhancement
# ----------------------------------------------------------------------------
IS_GET_EDGE_ENHANCEMENT = 0x8000
IS_EDGE_EN_DISABLE = 0
IS_EDGE_EN_STRONG = 1
IS_EDGE_EN_WEAK = 2
# ----------------------------------------------------------------------------
# white balance modes
# ----------------------------------------------------------------------------
IS_GET_WB_MODE = 0x8000
IS_SET_WB_DISABLE = 0x0000
IS_SET_WB_USER = 0x0001
IS_SET_WB_AUTO_ENABLE = 0x0002
IS_SET_WB_AUTO_ENABLE_ONCE = 0x0004
IS_SET_WB_DAYLIGHT_65 = 0x0101
IS_SET_WB_COOL_WHITE = 0x0102
IS_SET_WB_U30 = 0x0103
IS_SET_WB_ILLUMINANT_A = 0x0104
IS_SET_WB_HORIZON = 0x0105
# ----------------------------------------------------------------------------
# EEPROM defines
# ----------------------------------------------------------------------------
IS_EEPROM_MIN_USER_ADDRESS = 0
IS_EEPROM_MAX_USER_ADDRESS = 63
IS_EEPROM_MAX_USER_SPACE = 64
# ----------------------------------------------------------------------------
# Error report modes
# ----------------------------------------------------------------------------
IS_GET_ERR_REP_MODE = 0x8000
IS_ENABLE_ERR_REP = 1
IS_DISABLE_ERR_REP = 0
# ----------------------------------------------------------------------------
# Display mode selectors
# ----------------------------------------------------------------------------
IS_GET_DISPLAY_MODE = 0x8000
IS_SET_DM_DIB = 1
IS_SET_DM_DIRECT3D = 4
IS_SET_DM_OPENGL = 8
IS_SET_DM_MONO = 0x800
IS_SET_DM_BAYER = 0x1000
IS_SET_DM_YCBCR = 0x4000
# ----------------------------------------------------------------------------
# DirectRenderer commands
# ----------------------------------------------------------------------------
DR_GET_OVERLAY_DC = 1
DR_GET_MAX_OVERLAY_SIZE = 2
DR_GET_OVERLAY_KEY_COLOR = 3
DR_RELEASE_OVERLAY_DC = 4
DR_SHOW_OVERLAY = 5
DR_HIDE_OVERLAY = 6
DR_SET_OVERLAY_SIZE = 7
DR_SET_OVERLAY_POSITION = 8
DR_SET_OVERLAY_KEY_COLOR = 9
DR_SET_HWND = 10
DR_ENABLE_SCALING = 11
DR_DISABLE_SCALING = 12
DR_CLEAR_OVERLAY = 13
DR_ENABLE_SEMI_TRANSPARENT_OVERLAY = 14
DR_DISABLE_SEMI_TRANSPARENT_OVERLAY = 15
DR_CHECK_COMPATIBILITY = 16
DR_SET_VSYNC_OFF = 17
DR_SET_VSYNC_AUTO = 18
DR_SET_USER_SYNC = 19
DR_GET_USER_SYNC_POSITION_RANGE = 20
DR_LOAD_OVERLAY_FROM_FILE = 21
DR_STEAL_NEXT_FRAME = 22
DR_SET_STEAL_FORMAT = 23
DR_GET_STEAL_FORMAT = 24
DR_ENABLE_IMAGE_SCALING = 25
DR_GET_OVERLAY_SIZE = 26
DR_CHECK_COLOR_MODE_SUPPORT = 27
DR_GET_OVERLAY_DATA = 28
DR_UPDATE_OVERLAY_DATA = 29
DR_GET_SUPPORTED = 30
# ----------------------------------------------------------------------------
# save options
# ----------------------------------------------------------------------------
IS_SAVE_USE_ACTUAL_IMAGE_SIZE = 0x00010000
# ----------------------------------------------------------------------------
# renumeration modes
# ----------------------------------------------------------------------------
IS_RENUM_BY_CAMERA = 0
IS_RENUM_BY_HOST = 1
# ----------------------------------------------------------------------------
# event constants
# ----------------------------------------------------------------------------
IS_SET_EVENT_ODD = 0
IS_SET_EVENT_EVEN = 1
IS_SET_EVENT_FRAME = 2
IS_SET_EVENT_EXTTRIG = 3
IS_SET_EVENT_VSYNC = 4
IS_SET_EVENT_SEQ = 5
IS_SET_EVENT_STEAL = 6
IS_SET_EVENT_VPRES = 7
IS_SET_EVENT_CAPTURE_STATUS = 8
IS_SET_EVENT_TRANSFER_FAILED = IS_SET_EVENT_CAPTURE_STATUS
IS_SET_EVENT_DEVICE_RECONNECTED = 9
IS_SET_EVENT_MEMORY_MODE_FINISH = 10
IS_SET_EVENT_FRAME_RECEIVED = 11
IS_SET_EVENT_WB_FINISHED = 12
IS_SET_EVENT_AUTOBRIGHTNESS_FINISHED = 13
IS_SET_EVENT_OVERLAY_DATA_LOST = 16
IS_SET_EVENT_CAMERA_MEMORY = 17
IS_SET_EVENT_CONNECTIONSPEED_CHANGED = 18
IS_SET_EVENT_AUTOFOCUS_FINISHED = 19
IS_SET_EVENT_FIRST_PACKET_RECEIVED = 20
IS_SET_EVENT_PMC_IMAGE_PARAMS_CHANGED = 21
IS_SET_EVENT_DEVICE_PLUGGED_IN = 22
IS_SET_EVENT_DEVICE_UNPLUGGED = 23
IS_SET_EVENT_REMOVE = 128
IS_SET_EVENT_REMOVAL = 129
IS_SET_EVENT_NEW_DEVICE = 130
IS_SET_EVENT_STATUS_CHANGED = 131
# ----------------------------------------------------------------------------
# Window message defines
# ----------------------------------------------------------------------------
IS_UEYE_MESSAGE = (WM_USER + 0x0100) 
IS_FRAME = 0x0000
IS_SEQUENCE = 0x0001
IS_TRIGGER = 0x0002
IS_CAPTURE_STATUS = 0x0003
IS_TRANSFER_FAILED = IS_CAPTURE_STATUS
IS_DEVICE_RECONNECTED = 0x0004
IS_MEMORY_MODE_FINISH = 0x0005
IS_FRAME_RECEIVED = 0x0006
IS_GENERIC_ERROR = 0x0007
IS_STEAL_VIDEO = 0x0008
IS_WB_FINISHED = 0x0009
IS_AUTOBRIGHTNESS_FINISHED = 0x000A
IS_OVERLAY_DATA_LOST = 0x000B
IS_CAMERA_MEMORY = 0x000C
IS_CONNECTIONSPEED_CHANGED = 0x000D
IS_AUTOFOCUS_FINISHED = 0x000E
IS_FIRST_PACKET_RECEIVED = 0x000F
IS_PMC_IMAGE_PARAMS_CHANGED = 0x0010
IS_DEVICE_PLUGGED_IN = 0x0011
IS_DEVICE_UNPLUGGED = 0x0012
IS_DEVICE_REMOVED = 0x1000
IS_DEVICE_REMOVAL = 0x1001
IS_NEW_DEVICE = 0x1002
IS_DEVICE_STATUS_CHANGED = 0x1003
# ----------------------------------------------------------------------------
# Camera id constants
# ----------------------------------------------------------------------------
IS_GET_CAMERA_ID = 0x8000
# ----------------------------------------------------------------------------
# Camera info constants
# ----------------------------------------------------------------------------
IS_GET_STATUS = 0x8000
IS_EXT_TRIGGER_EVENT_CNT = 0
IS_FIFO_OVR_CNT = 1
IS_SEQUENCE_CNT = 2
IS_LAST_FRAME_FIFO_OVR = 3
IS_SEQUENCE_SIZE = 4
IS_VIDEO_PRESENT = 5
IS_STEAL_FINISHED = 6
IS_STORE_FILE_PATH = 7
IS_LUMA_BANDWIDTH_FILTER = 8
IS_BOARD_REVISION = 9
IS_MIRROR_BITMAP_UPDOWN = 10
IS_BUS_OVR_CNT = 11
IS_STEAL_ERROR_CNT = 12
IS_LOW_COLOR_REMOVAL = 13
IS_CHROMA_COMB_FILTER = 14
IS_CHROMA_AGC = 15
IS_WATCHDOG_ON_BOARD = 16
IS_PASSTHROUGH_ON_BOARD = 17
IS_EXTERNAL_VREF_MODE = 18
IS_WAIT_TIMEOUT = 19
IS_TRIGGER_MISSED = 20
IS_LAST_CAPTURE_ERROR = 21
IS_PARAMETER_SET_1 = 22
IS_PARAMETER_SET_2 = 23
IS_STANDBY = 24
IS_STANDBY_SUPPORTED = 25
IS_QUEUED_IMAGE_EVENT_CNT = 26
IS_PARAMETER_EXT = 27
# ----------------------------------------------------------------------------
# Interface type defines
# ----------------------------------------------------------------------------
IS_INTERFACE_TYPE_USB = 0x40
IS_INTERFACE_TYPE_USB3 = 0x60
IS_INTERFACE_TYPE_ETH = 0x80
IS_INTERFACE_TYPE_PMC = 0xf0
# ----------------------------------------------------------------------------
# Board type defines
# ----------------------------------------------------------------------------
IS_BOARD_TYPE_UEYE_USB = (IS_INTERFACE_TYPE_USB + 0)     # 0x40
IS_BOARD_TYPE_UEYE_USB_SE = IS_BOARD_TYPE_UEYE_USB          # 0x40
IS_BOARD_TYPE_UEYE_USB_RE = IS_BOARD_TYPE_UEYE_USB          # 0x40
IS_BOARD_TYPE_UEYE_USB_ME = (IS_INTERFACE_TYPE_USB + 0x01)  # 0x41
IS_BOARD_TYPE_UEYE_USB_LE = (IS_INTERFACE_TYPE_USB + 0x02)  # 0x42
IS_BOARD_TYPE_UEYE_USB_XS = (IS_INTERFACE_TYPE_USB + 0x03)  # 0x43
IS_BOARD_TYPE_UEYE_USB_ML = (IS_INTERFACE_TYPE_USB + 0x05)  # 0x45
IS_BOARD_TYPE_UEYE_USB3_LE = (IS_INTERFACE_TYPE_USB3 + 0x02) # 0x62
IS_BOARD_TYPE_UEYE_USB3_CP = (IS_INTERFACE_TYPE_USB3 + 0x04) # 0x64
IS_BOARD_TYPE_UEYE_USB3_ML = (IS_INTERFACE_TYPE_USB3 + 0x05) # 0x65
IS_BOARD_TYPE_UEYE_ETH = IS_INTERFACE_TYPE_ETH           # 0x80
IS_BOARD_TYPE_UEYE_ETH_HE = IS_BOARD_TYPE_UEYE_ETH          # 0x80
IS_BOARD_TYPE_UEYE_ETH_SE = (IS_INTERFACE_TYPE_ETH + 0x01)  # 0x81
IS_BOARD_TYPE_UEYE_ETH_RE = IS_BOARD_TYPE_UEYE_ETH_SE       # 0x81
IS_BOARD_TYPE_UEYE_ETH_LE = (IS_INTERFACE_TYPE_ETH + 0x02)  # 0x82
IS_BOARD_TYPE_UEYE_ETH_CP = (IS_INTERFACE_TYPE_ETH + 0x04)  # 0x84
IS_BOARD_TYPE_UEYE_ETH_SEP = (IS_INTERFACE_TYPE_ETH + 0x06)  # 0x86
IS_BOARD_TYPE_UEYE_ETH_REP = IS_BOARD_TYPE_UEYE_ETH_SEP      # 0x86
IS_BOARD_TYPE_UEYE_ETH_LEET = (IS_INTERFACE_TYPE_ETH + 0x07)  # 0x87
IS_BOARD_TYPE_UEYE_ETH_TE = (IS_INTERFACE_TYPE_ETH + 0x08)  # 0x88
# ----------------------------------------------------------------------------
# Camera type defines
# ----------------------------------------------------------------------------
IS_CAMERA_TYPE_UEYE_USB = IS_BOARD_TYPE_UEYE_USB_SE
IS_CAMERA_TYPE_UEYE_USB_SE = IS_BOARD_TYPE_UEYE_USB_SE
IS_CAMERA_TYPE_UEYE_USB_RE = IS_BOARD_TYPE_UEYE_USB_RE
IS_CAMERA_TYPE_UEYE_USB_ME = IS_BOARD_TYPE_UEYE_USB_ME
IS_CAMERA_TYPE_UEYE_USB_LE = IS_BOARD_TYPE_UEYE_USB_LE
IS_CAMERA_TYPE_UEYE_USB_ML = IS_BOARD_TYPE_UEYE_USB_ML
IS_CAMERA_TYPE_UEYE_USB3_LE = IS_BOARD_TYPE_UEYE_USB3_LE
IS_CAMERA_TYPE_UEYE_USB3_CP = IS_BOARD_TYPE_UEYE_USB3_CP
IS_CAMERA_TYPE_UEYE_USB3_ML = IS_BOARD_TYPE_UEYE_USB3_ML
IS_CAMERA_TYPE_UEYE_ETH = IS_BOARD_TYPE_UEYE_ETH_HE
IS_CAMERA_TYPE_UEYE_ETH_HE = IS_BOARD_TYPE_UEYE_ETH_HE
IS_CAMERA_TYPE_UEYE_ETH_SE = IS_BOARD_TYPE_UEYE_ETH_SE
IS_CAMERA_TYPE_UEYE_ETH_RE = IS_BOARD_TYPE_UEYE_ETH_RE
IS_CAMERA_TYPE_UEYE_ETH_LE = IS_BOARD_TYPE_UEYE_ETH_LE
IS_CAMERA_TYPE_UEYE_ETH_CP = IS_BOARD_TYPE_UEYE_ETH_CP
IS_CAMERA_TYPE_UEYE_ETH_SEP = IS_BOARD_TYPE_UEYE_ETH_SEP
IS_CAMERA_TYPE_UEYE_ETH_REP = IS_BOARD_TYPE_UEYE_ETH_REP
IS_CAMERA_TYPE_UEYE_ETH_LEET = IS_BOARD_TYPE_UEYE_ETH_LEET
IS_CAMERA_TYPE_UEYE_ETH_TE = IS_BOARD_TYPE_UEYE_ETH_TE
IS_CAMERA_TYPE_UEYE_PMC = (IS_INTERFACE_TYPE_PMC + 0x01)
# ----------------------------------------------------------------------------
# Readable operation system defines
# ----------------------------------------------------------------------------
IS_OS_UNDETERMINED = 0
IS_OS_WIN95 = 1
IS_OS_WINNT40 = 2
IS_OS_WIN98 = 3
IS_OS_WIN2000 = 4
IS_OS_WINXP = 5
IS_OS_WINME = 6
IS_OS_WINNET = 7
IS_OS_WINSERVER2003 = 8
IS_OS_WINVISTA = 9
IS_OS_LINUX24 = 10
IS_OS_LINUX26 = 11
IS_OS_WIN7 = 12
IS_OS_WIN8 = 13
IS_OS_WIN8SERVER = 14
IS_OS_GREATER_THAN_WIN8 = 15
# ----------------------------------------------------------------------------
# Bus speed
# ----------------------------------------------------------------------------
IS_USB_10 = 0x0001 #  1,5 Mb/s
IS_USB_11 = 0x0002 #   12 Mb/s
IS_USB_20 = 0x0004 #  480 Mb/s
IS_USB_30 = 0x0008 # 4000 Mb/s
IS_ETHERNET_10 = 0x0080 #   10 Mb/s
IS_ETHERNET_100 = 0x0100 #  100 Mb/s
IS_ETHERNET_1000 = 0x0200 # 1000 Mb/s
IS_ETHERNET_10000 = 0x0400 #10000 Mb/s
IS_USB_LOW_SPEED = 1
IS_USB_FULL_SPEED = 12
IS_USB_HIGH_SPEED = 480
IS_USB_SUPER_SPEED = 4000
IS_ETHERNET_10Base = 10
IS_ETHERNET_100Base = 100
IS_ETHERNET_1000Base = 1000
IS_ETHERNET_10GBase = 10000
# ----------------------------------------------------------------------------
# HDR
# ----------------------------------------------------------------------------
IS_HDR_NOT_SUPPORTED = 0
IS_HDR_KNEEPOINTS = 1
IS_DISABLE_HDR = 0
IS_ENABLE_HDR = 1
# ----------------------------------------------------------------------------
# Test images
# ----------------------------------------------------------------------------
IS_TEST_IMAGE_NONE = 0x00000000
IS_TEST_IMAGE_WHITE = 0x00000001
IS_TEST_IMAGE_BLACK = 0x00000002
IS_TEST_IMAGE_HORIZONTAL_GREYSCALE = 0x00000004
IS_TEST_IMAGE_VERTICAL_GREYSCALE = 0x00000008
IS_TEST_IMAGE_DIAGONAL_GREYSCALE = 0x00000010
IS_TEST_IMAGE_WEDGE_GRAY = 0x00000020
IS_TEST_IMAGE_WEDGE_COLOR = 0x00000040
IS_TEST_IMAGE_ANIMATED_WEDGE_GRAY = 0x00000080
IS_TEST_IMAGE_ANIMATED_WEDGE_COLOR = 0x00000100
IS_TEST_IMAGE_MONO_BARS = 0x00000200
IS_TEST_IMAGE_COLOR_BARS1 = 0x00000400
IS_TEST_IMAGE_COLOR_BARS2 = 0x00000800
IS_TEST_IMAGE_GREYSCALE1 = 0x00001000
IS_TEST_IMAGE_GREY_AND_COLOR_BARS = 0x00002000
IS_TEST_IMAGE_MOVING_GREY_AND_COLOR_BARS = 0x00004000
IS_TEST_IMAGE_ANIMATED_LINE = 0x00008000
IS_TEST_IMAGE_ALTERNATE_PATTERN = 0x00010000
IS_TEST_IMAGE_VARIABLE_GREY = 0x00020000
IS_TEST_IMAGE_MONOCHROME_HORIZONTAL_BARS = 0x00040000
IS_TEST_IMAGE_MONOCHROME_VERTICAL_BARS = 0x00080000
IS_TEST_IMAGE_CURSOR_H = 0x00100000
IS_TEST_IMAGE_CURSOR_V = 0x00200000
IS_TEST_IMAGE_COLDPIXEL_GRID = 0x00400000
IS_TEST_IMAGE_HOTPIXEL_GRID = 0x00800000
IS_TEST_IMAGE_VARIABLE_RED_PART = 0x01000000
IS_TEST_IMAGE_VARIABLE_GREEN_PART = 0x02000000
IS_TEST_IMAGE_VARIABLE_BLUE_PART = 0x04000000
IS_TEST_IMAGE_SHADING_IMAGE = 0x08000000
IS_TEST_IMAGE_WEDGE_GRAY_SENSOR = 0x10000000
IS_TEST_IMAGE_ANIMATED_WEDGE_GRAY_SENSOR = 0x20000000
IS_TEST_IMAGE_RAMPING_PATTERN = 0x40000000
IS_TEST_IMAGE_CHESS_PATTERN = 0x80000000
# ----------------------------------------------------------------------------
# Sensor scaler
# ----------------------------------------------------------------------------
IS_ENABLE_SENSOR_SCALER = 1
IS_ENABLE_ANTI_ALIASING = 2
# ----------------------------------------------------------------------------
# Timeouts
# ----------------------------------------------------------------------------
IS_TRIGGER_TIMEOUT = 0
# ----------------------------------------------------------------------------
# Auto pixel clock modes
# ----------------------------------------------------------------------------
IS_BEST_PCLK_RUN_ONCE = 0
# ----------------------------------------------------------------------------
# Sequence flags
# ----------------------------------------------------------------------------
IS_LOCK_LAST_BUFFER = 0x8002
IS_GET_ALLOC_ID_OF_THIS_BUF = 0x8004
IS_GET_ALLOC_ID_OF_LAST_BUF = 0x8008
IS_USE_ALLOC_ID = 0x8000
IS_USE_CURRENT_IMG_SIZE = 0xC000
# ------------------------------------------
# Memory information flags
# ------------------------------------------
IS_GET_D3D_MEM = 0x8000
# ----------------------------------------------------------------------------
# Image files types
# ----------------------------------------------------------------------------
IS_IMG_BMP = 0
IS_IMG_JPG = 1
IS_IMG_PNG = 2
IS_IMG_RAW = 4
IS_IMG_TIF = 8
# ----------------------------------------------------------------------------
# I2C defines
# nRegisterAddr | IS_I2C_16_BIT_REGISTER
# nRegisterAddr | IS_I2C_0_BIT_REGISTER
# ----------------------------------------------------------------------------
IS_I2C_16_BIT_REGISTER = 0x10000000
IS_I2C_0_BIT_REGISTER = 0x20000000
# nDeviceAddr | IS_I2C_DONT_WAIT
IS_I2C_DONT_WAIT = 0x00800000
# ----------------------------------------------------------------------------
# Gamma modes
# ----------------------------------------------------------------------------
IS_GET_GAMMA_MODE = 0x8000
IS_SET_GAMMA_OFF = 0
IS_SET_GAMMA_ON = 1
# ----------------------------------------------------------------------------
# Capture modes   (Falcon)
# ----------------------------------------------------------------------------
IS_GET_CAPTURE_MODE = 0x8000
IS_SET_CM_ODD = 0x0001
IS_SET_CM_EVEN = 0x0002
IS_SET_CM_FRAME = 0x0004
IS_SET_CM_NONINTERLACED = 0x0008
IS_SET_CM_NEXT_FRAME = 0x0010
IS_SET_CM_NEXT_FIELD = 0x0020
IS_SET_CM_BOTHFIELDS = (IS_SET_CM_ODD | IS_SET_CM_EVEN | IS_SET_CM_NONINTERLACED)
IS_SET_CM_FRAME_STEREO = 0x2004
# ----------------------------------------------------------------------------
# Typedefs
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# Invalid values for device handles
# ----------------------------------------------------------------------------
IS_INVALID_HIDS =0
IS_INVALID_HCAM =0
IS_INVALID_HFALC =0
# ----------------------------------------------------------------------------
# Info struct
# ----------------------------------------------------------------------------
IS_CAP_STATUS_API_NO_DEST_MEM       =   0xa2
IS_CAP_STATUS_API_CONVERSION_FAILED =   0xa3
IS_CAP_STATUS_API_IMAGE_LOCKED      =   0xa5
IS_CAP_STATUS_DRV_OUT_OF_BUFFERS    =   0xb2
IS_CAP_STATUS_DRV_DEVICE_NOT_READY  =   0xb4
IS_CAP_STATUS_USB_TRANSFER_FAILED   =   0xc7
IS_CAP_STATUS_DEV_TIMEOUT           =   0xd6
IS_CAP_STATUS_ETH_BUFFER_OVERRUN    =   0xe4
IS_CAP_STATUS_ETH_MISSED_IMAGES     =   0xe5
FIRMWARE_DOWNLOAD_NOT_SUPPORTED = 0x00000001
INTERFACE_SPEED_NOT_SUPPORTED = 0x00000002
INVALID_SENSOR_DETECTED = 0x00000004
AUTHORIZATION_FAILED = 0x00000008
DEVSTS_INCLUDED_STARTER_FIRMWARE_INCOMPATIBLE = 0x00000010
AC_SHUTTER = 0x00000001
AC_GAIN = 0x00000002
AC_WHITEBAL = 0x00000004
AC_WB_RED_CHANNEL = 0x00000008
AC_WB_GREEN_CHANNEL = 0x00000010
AC_WB_BLUE_CHANNEL = 0x00000020
AC_FRAMERATE = 0x00000040
AC_SENSOR_SHUTTER = 0x00000080
AC_SENSOR_GAIN = 0x00000100
AC_SENSOR_GAIN_SHUTTER = 0x00000200
AC_SENSOR_FRAMERATE = 0x00000400
AC_SENSOR_WB = 0x00000800
AC_SENSOR_AUTO_REFERENCE = 0x00001000
AC_SENSOR_AUTO_SPEED = 0x00002000
AC_SENSOR_AUTO_HYSTERESIS = 0x00004000
AC_SENSOR_AUTO_SKIPFRAMES = 0x00008000
AC_SENSOR_AUTO_CONTRAST_CORRECTION = 0x00010000
AC_SENSOR_AUTO_CONTRAST_FDT_AOI = 0x00020000
AC_SENSOR_AUTO_BACKLIGHT_COMP = 0x00040000
ACS_ADJUSTING = 0x00000001
ACS_FINISHED = 0x00000002
ACS_DISABLED = 0x00000004
IS_BOOTBOOST_ID_MIN = 1   #!< \brief minimum valid id 
IS_BOOTBOOST_ID_MAX = 254 #!< \brief maximum valid id 
IS_BOOTBOOST_ID_NONE = 0   #!< \brief special value: no id's 
IS_BOOTBOOST_ID_ALL = 255 #!< \brief special value: all id's 
IS_BOOTBOOST_DEFAULT_WAIT_TIMEOUT_SEC = 60
IS_BOOTBOOST_CMD_ENABLE             = 0x00010001
IS_BOOTBOOST_CMD_ENABLE_AND_WAIT    = 0x00010101
IS_BOOTBOOST_CMD_DISABLE            = 0x00010011
IS_BOOTBOOST_CMD_DISABLE_AND_WAIT   = 0x00010111
IS_BOOTBOOST_CMD_WAIT               = 0x00010100
IS_BOOTBOOST_CMD_GET_ENABLED        = 0x20010021
IS_BOOTBOOST_CMD_ADD_ID             = 0x10100001
IS_BOOTBOOST_CMD_SET_IDLIST         = 0x10100005
IS_BOOTBOOST_CMD_REMOVE_ID         = 0x10100011
IS_BOOTBOOST_CMD_CLEAR_IDLIST       = 0x00100015
IS_BOOTBOOST_CMD_GET_IDLIST        = 0x30100021
IS_BOOTBOOST_CMD_GET_IDLIST_SIZE    = 0x20100022
IS_DEVICE_FEATURE_CMD_GET_SUPPORTED_FEATURES                                = 1
IS_DEVICE_FEATURE_CMD_SET_LINESCAN_MODE                                     = 2
IS_DEVICE_FEATURE_CMD_GET_LINESCAN_MODE                                     = 3
IS_DEVICE_FEATURE_CMD_SET_LINESCAN_NUMBER                                   = 4
IS_DEVICE_FEATURE_CMD_GET_LINESCAN_NUMBER                                   = 5
IS_DEVICE_FEATURE_CMD_SET_SHUTTER_MODE                                      = 6
IS_DEVICE_FEATURE_CMD_GET_SHUTTER_MODE                                      = 7
IS_DEVICE_FEATURE_CMD_SET_PREFER_XS_HS_MODE                                 = 8
IS_DEVICE_FEATURE_CMD_GET_PREFER_XS_HS_MODE                                 = 9
IS_DEVICE_FEATURE_CMD_GET_DEFAULT_PREFER_XS_HS_MODE                         = 10,   
IS_DEVICE_FEATURE_CMD_GET_LOG_MODE_DEFAULT                                  = 11
IS_DEVICE_FEATURE_CMD_GET_LOG_MODE                                          = 12
IS_DEVICE_FEATURE_CMD_SET_LOG_MODE                                          = 13,   
IS_DEVICE_FEATURE_CMD_GET_LOG_MODE_MANUAL_VALUE_DEFAULT                     = 14
IS_DEVICE_FEATURE_CMD_GET_LOG_MODE_MANUAL_VALUE_RANGE                       = 15
IS_DEVICE_FEATURE_CMD_GET_LOG_MODE_MANUAL_VALUE                             = 16
IS_DEVICE_FEATURE_CMD_SET_LOG_MODE_MANUAL_VALUE                             = 17
IS_DEVICE_FEATURE_CMD_GET_LOG_MODE_MANUAL_GAIN_DEFAULT                      = 18
IS_DEVICE_FEATURE_CMD_GET_LOG_MODE_MANUAL_GAIN_RANGE                        = 19
IS_DEVICE_FEATURE_CMD_GET_LOG_MODE_MANUAL_GAIN                              = 20
IS_DEVICE_FEATURE_CMD_SET_LOG_MODE_MANUAL_GAIN                              = 21
IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_MODE_DEFAULT                   = 22
IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_MODE                           = 23
IS_DEVICE_FEATURE_CMD_SET_VERTICAL_AOI_MERGE_MODE                           = 24
IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_POSITION_DEFAULT               = 25
IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_POSITION_RANGE                 = 26
IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_POSITION                       = 27
IS_DEVICE_FEATURE_CMD_SET_VERTICAL_AOI_MERGE_POSITION                       = 28
IS_DEVICE_FEATURE_CMD_GET_FPN_CORRECTION_MODE_DEFAULT                       = 29
IS_DEVICE_FEATURE_CMD_GET_FPN_CORRECTION_MODE                               = 30
IS_DEVICE_FEATURE_CMD_SET_FPN_CORRECTION_MODE                               = 31
IS_DEVICE_FEATURE_CMD_GET_SENSOR_SOURCE_GAIN_RANGE                          = 32
IS_DEVICE_FEATURE_CMD_GET_SENSOR_SOURCE_GAIN_DEFAULT                        = 33
IS_DEVICE_FEATURE_CMD_GET_SENSOR_SOURCE_GAIN                                = 34
IS_DEVICE_FEATURE_CMD_SET_SENSOR_SOURCE_GAIN                                = 35
IS_DEVICE_FEATURE_CMD_GET_BLACK_REFERENCE_MODE_DEFAULT                      = 36
IS_DEVICE_FEATURE_CMD_GET_BLACK_REFERENCE_MODE                              = 37
IS_DEVICE_FEATURE_CMD_SET_BLACK_REFERENCE_MODE                              = 38
IS_DEVICE_FEATURE_CMD_GET_ALLOW_RAW_WITH_LUT                                = 39
IS_DEVICE_FEATURE_CMD_SET_ALLOW_RAW_WITH_LUT                                = 40
IS_DEVICE_FEATURE_CMD_GET_SUPPORTED_SENSOR_BIT_DEPTHS                       = 41
IS_DEVICE_FEATURE_CMD_GET_SENSOR_BIT_DEPTH_DEFAULT                          = 42
IS_DEVICE_FEATURE_CMD_GET_SENSOR_BIT_DEPTH                                  = 43
IS_DEVICE_FEATURE_CMD_SET_SENSOR_BIT_DEPTH                                  = 44
IS_DEVICE_FEATURE_CMD_GET_TEMPERATURE                                       = 45
IS_DEVICE_FEATURE_CMD_GET_JPEG_COMPRESSION                                  = 46
IS_DEVICE_FEATURE_CMD_SET_JPEG_COMPRESSION                                  = 47
IS_DEVICE_FEATURE_CMD_GET_JPEG_COMPRESSION_DEFAULT                          = 48
IS_DEVICE_FEATURE_CMD_GET_JPEG_COMPRESSION_RANGE                            = 49
IS_DEVICE_FEATURE_CMD_GET_NOISE_REDUCTION_MODE                              = 50
IS_DEVICE_FEATURE_CMD_SET_NOISE_REDUCTION_MODE                              = 51
IS_DEVICE_FEATURE_CMD_GET_NOISE_REDUCTION_MODE_DEFAULT                      = 52
IS_DEVICE_FEATURE_CMD_GET_TIMESTAMP_CONFIGURATION                           = 53
IS_DEVICE_FEATURE_CMD_SET_TIMESTAMP_CONFIGURATION                           = 54
IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_HEIGHT_DEFAULT                 = 55
IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_HEIGHT_NUMBER                  = 56
IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_HEIGHT_LIST                    = 57
IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_HEIGHT                         = 58
IS_DEVICE_FEATURE_CMD_SET_VERTICAL_AOI_MERGE_HEIGHT                         = 59
IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_ADDITIONAL_POSITION_DEFAULT    = 60
IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_ADDITIONAL_POSITION_RANGE      = 61
IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_ADDITIONAL_POSITION            = 62
IS_DEVICE_FEATURE_CMD_SET_VERTICAL_AOI_MERGE_ADDITIONAL_POSITION            = 63
IS_DEVICE_FEATURE_CMD_GET_SENSOR_TEMPERATURE_NUMERICAL_VALUE                = 64
IS_DEVICE_FEATURE_CMD_SET_IMAGE_EFFECT                                      = 65
IS_DEVICE_FEATURE_CMD_GET_IMAGE_EFFECT                                      = 66
IS_DEVICE_FEATURE_CMD_GET_IMAGE_EFFECT_DEFAULT                              = 67
IS_DEVICE_FEATURE_CMD_GET_EXTENDED_PIXELCLOCK_RANGE_ENABLE_DEFAULT			= 68
IS_DEVICE_FEATURE_CMD_GET_EXTENDED_PIXELCLOCK_RANGE_ENABLE					= 69
IS_DEVICE_FEATURE_CMD_SET_EXTENDED_PIXELCLOCK_RANGE_ENABLE					= 70
IS_DEVICE_FEATURE_CMD_MULTI_INTEGRATION_GET_SCOPE            			    = 71
IS_DEVICE_FEATURE_CMD_MULTI_INTEGRATION_GET_PARAMS           			    = 72
IS_DEVICE_FEATURE_CMD_MULTI_INTEGRATION_SET_PARAMS                 		    = 73
IS_DEVICE_FEATURE_CMD_MULTI_INTEGRATION_GET_MODE_DEFAULT                	= 74
IS_DEVICE_FEATURE_CMD_MULTI_INTEGRATION_GET_MODE                     	    = 75
IS_DEVICE_FEATURE_CMD_MULTI_INTEGRATION_SET_MODE                   	        = 76
IS_DEVICE_FEATURE_CMD_SET_I2C_TARGET                                        = 77
IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_MODE_SUPPORTED_LINE_MODES      = 85
IS_DEVICE_FEATURE_CAP_SHUTTER_MODE_ROLLING                      = 0x00000001
IS_DEVICE_FEATURE_CAP_SHUTTER_MODE_GLOBAL                       = 0x00000002
IS_DEVICE_FEATURE_CAP_LINESCAN_MODE_FAST                        = 0x00000004
IS_DEVICE_FEATURE_CAP_LINESCAN_NUMBER                           = 0x00000008
IS_DEVICE_FEATURE_CAP_PREFER_XS_HS_MODE                         = 0x00000010
IS_DEVICE_FEATURE_CAP_LOG_MODE                                  = 0x00000020
IS_DEVICE_FEATURE_CAP_SHUTTER_MODE_ROLLING_GLOBAL_START         = 0x00000040
IS_DEVICE_FEATURE_CAP_SHUTTER_MODE_GLOBAL_ALTERNATIVE_TIMING    = 0x00000080
IS_DEVICE_FEATURE_CAP_VERTICAL_AOI_MERGE                        = 0x00000100
IS_DEVICE_FEATURE_CAP_FPN_CORRECTION                            = 0x00000200
IS_DEVICE_FEATURE_CAP_SENSOR_SOURCE_GAIN                        = 0x00000400
IS_DEVICE_FEATURE_CAP_BLACK_REFERENCE                           = 0x00000800
IS_DEVICE_FEATURE_CAP_SENSOR_BIT_DEPTH                          = 0x00001000
IS_DEVICE_FEATURE_CAP_TEMPERATURE                               = 0x00002000
IS_DEVICE_FEATURE_CAP_JPEG_COMPRESSION                          = 0x00004000
IS_DEVICE_FEATURE_CAP_NOISE_REDUCTION                           = 0x00008000
IS_DEVICE_FEATURE_CAP_TIMESTAMP_CONFIGURATION                   = 0x00010000
IS_DEVICE_FEATURE_CAP_IMAGE_EFFECT                              = 0x00020000
IS_DEVICE_FEATURE_CAP_EXTENDED_PIXELCLOCK_RANGE					= 0x00040000
IS_DEVICE_FEATURE_CAP_MULTI_INTEGRATION                         = 0x00080000
IS_NOISE_REDUCTION_OFF        = 0
IS_NOISE_REDUCTION_ADAPTIVE   = 1
IS_LOG_MODE_FACTORY_DEFAULT    = 0
IS_LOG_MODE_OFF                = 1
IS_LOG_MODE_MANUAL             = 2
IS_LOG_MODE_AUTO               = 3
IS_VERTICAL_AOI_MERGE_MODE_OFF                      = 0
IS_VERTICAL_AOI_MERGE_MODE_FREERUN                  = 1
IS_VERTICAL_AOI_MERGE_MODE_TRIGGERED_SOFTWARE       = 2
IS_VERTICAL_AOI_MERGE_MODE_TRIGGERED_FALLING_GPIO1  = 3
IS_VERTICAL_AOI_MERGE_MODE_TRIGGERED_RISING_GPIO1   = 4
IS_VERTICAL_AOI_MERGE_MODE_TRIGGERED_FALLING_GPIO2  = 5
IS_VERTICAL_AOI_MERGE_MODE_TRIGGERED_RISING_GPIO2   = 6
IS_VERTICAL_AOI_MERGE_MODE_LINE_FREERUN             = 1
IS_VERTICAL_AOI_MERGE_MODE_LINE_SOFTWARE_TRIGGER    = 2
IS_VERTICAL_AOI_MERGE_MODE_LINE_GPIO_TRIGGER        = 4
IS_FPN_CORRECTION_MODE_OFF      = 0
IS_FPN_CORRECTION_MODE_HARDWARE = 1
IS_BLACK_REFERENCE_MODE_OFF           = 0x00000000
IS_BLACK_REFERENCE_MODE_COLUMNS_LEFT  = 0x00000001
IS_SENSOR_BIT_DEPTH_AUTO    = 0x00000000
IS_SENSOR_BIT_DEPTH_8_BIT   = 0x00000001
IS_SENSOR_BIT_DEPTH_10_BIT  = 0x00000002
IS_SENSOR_BIT_DEPTH_12_BIT  = 0x00000004
IS_RESET_TIMESTAMP_ONCE = 1
TIMESTAMP_CONFIGURATION_PIN_NONE        = 0
TIMESTAMP_CONFIGURATION_PIN_TRIGGER     = 1
TIMESTAMP_CONFIGURATION_PIN_GPIO_1      = 2
TIMESTAMP_CONFIGURATION_PIN_GPIO_2      = 3
TIMESTAMP_CONFIGURATION_EDGE_FALLING    = 0
TIMESTAMP_CONFIGURATION_EDGE_RISING     = 1
IS_IMAGE_EFFECT_DISABLE    = 0
IS_IMAGE_EFFECT_SEPIA      = 1
IS_IMAGE_EFFECT_MONOCHROME = 2
IS_IMAGE_EFFECT_NEGATIVE   = 3
IS_IMAGE_EFFECT_CROSSHAIRS = 4
EXTENDED_PIXELCLOCK_RANGE_OFF	= 0
EXTENDED_PIXELCLOCK_RANGE_ON	= 1
MULTI_INTEGRATION_MODE_OFF      = 0
MULTI_INTEGRATION_MODE_SOFTWARE = 1
MULTI_INTEGRATION_MODE_GPIO1    = 2
MULTI_INTEGRATION_MODE_GPIO2    = 3
I2C_TARGET_DEFAULT      = 0
I2C_TARGET_SENSOR_1     = 1
I2C_TARGET_SENSOR_2     = 2
I2C_TARGET_LOGIC_BOARD  = 4
IS_EXPOSURE_CMD_GET_CAPS                        = 1
IS_EXPOSURE_CMD_GET_EXPOSURE_DEFAULT            = 2
IS_EXPOSURE_CMD_GET_EXPOSURE_RANGE_MIN          = 3
IS_EXPOSURE_CMD_GET_EXPOSURE_RANGE_MAX          = 4
IS_EXPOSURE_CMD_GET_EXPOSURE_RANGE_INC          = 5
IS_EXPOSURE_CMD_GET_EXPOSURE_RANGE              = 6
IS_EXPOSURE_CMD_GET_EXPOSURE                    = 7
IS_EXPOSURE_CMD_GET_FINE_INCREMENT_RANGE_MIN    = 8
IS_EXPOSURE_CMD_GET_FINE_INCREMENT_RANGE_MAX    = 9
IS_EXPOSURE_CMD_GET_FINE_INCREMENT_RANGE_INC    = 10
IS_EXPOSURE_CMD_GET_FINE_INCREMENT_RANGE        = 11
IS_EXPOSURE_CMD_SET_EXPOSURE                    = 12
IS_EXPOSURE_CMD_GET_LONG_EXPOSURE_RANGE_MIN     = 13
IS_EXPOSURE_CMD_GET_LONG_EXPOSURE_RANGE_MAX     = 14
IS_EXPOSURE_CMD_GET_LONG_EXPOSURE_RANGE_INC     = 15
IS_EXPOSURE_CMD_GET_LONG_EXPOSURE_RANGE         = 16
IS_EXPOSURE_CMD_GET_LONG_EXPOSURE_ENABLE        = 17
IS_EXPOSURE_CMD_SET_LONG_EXPOSURE_ENABLE        = 18
IS_EXPOSURE_CMD_GET_DUAL_EXPOSURE_RATIO_DEFAULT = 19, 
IS_EXPOSURE_CMD_GET_DUAL_EXPOSURE_RATIO_RANGE   = 20, 
IS_EXPOSURE_CMD_GET_DUAL_EXPOSURE_RATIO         = 21
IS_EXPOSURE_CMD_SET_DUAL_EXPOSURE_RATIO         = 22
IS_EXPOSURE_CAP_EXPOSURE                        = 0x00000001
IS_EXPOSURE_CAP_FINE_INCREMENT                  = 0x00000002
IS_EXPOSURE_CAP_LONG_EXPOSURE                   = 0x00000004
IS_EXPOSURE_CAP_DUAL_EXPOSURE                   = 0x00000008
IS_TRIGGER_CMD_GET_BURST_SIZE_SUPPORTED      = 1
IS_TRIGGER_CMD_GET_BURST_SIZE_RANGE          = 2
IS_TRIGGER_CMD_GET_BURST_SIZE                = 3
IS_TRIGGER_CMD_SET_BURST_SIZE                = 4
IS_TRIGGER_CMD_GET_FRAME_PRESCALER_SUPPORTED = 5
IS_TRIGGER_CMD_GET_FRAME_PRESCALER_RANGE     = 6
IS_TRIGGER_CMD_GET_FRAME_PRESCALER           = 7
IS_TRIGGER_CMD_SET_FRAME_PRESCALER           = 8
IS_TRIGGER_CMD_GET_LINE_PRESCALER_SUPPORTED  = 9
IS_TRIGGER_CMD_GET_LINE_PRESCALER_RANGE      = 10
IS_TRIGGER_CMD_GET_LINE_PRESCALER            = 11
IS_TRIGGER_CMD_SET_LINE_PRESCALER            = 12
IS_DEVICE_INFO_CMD_GET_DEVICE_INFO  = 0x02010001
IS_CALLBACK_CMD_INSTALL     = 0x00000001
IS_CALLBACK_EV_IMGPOSTPROC_START = 0x00000001
IS_OPTIMAL_CAMERA_TIMING_CMD_GET_PIXELCLOCK = 0x00000001
IS_OPTIMAL_CAMERA_TIMING_CMD_GET_FRAMERATE  = 0x00000002
IS_ETH_DEVSTATUS_READY_TO_OPERATE=            0x00000001, #!< device is ready to operate 
IS_ETH_DEVSTATUS_TESTING_IP_CURRENT=          0x00000002, #!< device is (arp-)probing its current ip 
IS_ETH_DEVSTATUS_TESTING_IP_PERSISTENT=       0x00000004, #!< device is (arp-)probing its persistent ip 
IS_ETH_DEVSTATUS_TESTING_IP_RANGE=            0x00000008, #!< device is (arp-)probing the autocfg ip range 
IS_ETH_DEVSTATUS_INAPPLICABLE_IP_CURRENT=     0x00000010, #!< current ip is inapplicable 
IS_ETH_DEVSTATUS_INAPPLICABLE_IP_PERSISTENT=  0x00000020, #!< persistent ip is inapplicable 
IS_ETH_DEVSTATUS_INAPPLICABLE_IP_RANGE=       0x00000040, #!< autocfg ip range is inapplicable 
IS_ETH_DEVSTATUS_UNPAIRED=                    0x00000100, #!< device is unpaired 
IS_ETH_DEVSTATUS_PAIRING_IN_PROGRESS=         0x00000200, #!< device is being paired 
IS_ETH_DEVSTATUS_PAIRED=                      0x00000400, #!< device is paired 
IS_ETH_DEVSTATUS_FORCE_100MBPS=               0x00001000, #!< device phy is configured to 100 Mbps 
IS_ETH_DEVSTATUS_NO_COMPORT=                  0x00002000, #!< device does not support ueye eth comport 
IS_ETH_DEVSTATUS_RECEIVING_FW_STARTER=        0x00010000, #!< device is receiving the starter firmware 
IS_ETH_DEVSTATUS_RECEIVING_FW_RUNTIME=        0x00020000, #!< device is receiving the runtime firmware 
IS_ETH_DEVSTATUS_INAPPLICABLE_FW_RUNTIME=     0x00040000, #!< runtime firmware is inapplicable 
IS_ETH_DEVSTATUS_INAPPLICABLE_FW_STARTER=     0x00080000, #!< starter firmware is inapplicable 
IS_ETH_DEVSTATUS_REBOOTING_FW_RUNTIME=        0x00100000, #!< device is rebooting to runtime firmware 
IS_ETH_DEVSTATUS_REBOOTING_FW_STARTER=        0x00200000, #!< device is rebooting to starter firmware 
IS_ETH_DEVSTATUS_REBOOTING_FW_FAILSAFE=       0x00400000, #!< device is rebooting to failsafe firmware 
IS_ETH_DEVSTATUS_RUNTIME_FW_ERR0=             0x80000000  #!< checksum error runtime firmware 
IS_ETH_CTRLSTATUS_AVAILABLE =             0x00000001, #!< device is available TO SELF 
IS_ETH_CTRLSTATUS_ACCESSIBLE1 =           0x00000002, #!< device is accessible BY SELF, i.e. directly 'unicastable' 
IS_ETH_CTRLSTATUS_ACCESSIBLE2 =           0x00000004, #!< device is accessible BY SELF, i.e. not on persistent ip and adapters ip autocfg range is valid 
IS_ETH_CTRLSTATUS_PERSISTENT_IP_USED =    0x00000010, #!< device is running on persistent ip configuration 
IS_ETH_CTRLSTATUS_COMPATIBLE =            0x00000020, #!< device is compatible TO SELF 
IS_ETH_CTRLSTATUS_ADAPTER_ON_DHCP =       0x00000040, #!< adapter is configured to use dhcp 
IS_ETH_CTRLSTATUS_ADAPTER_SETUP_OK =      0x00000080, #!< adapter's setup is ok with respect to uEye needs 
IS_ETH_CTRLSTATUS_UNPAIRING_IN_PROGRESS = 0x00000100, #!< device is being unpaired FROM SELF 
IS_ETH_CTRLSTATUS_PAIRING_IN_PROGRESS =   0x00000200, #!< device is being paired TO SELF 
IS_ETH_CTRLSTATUS_PAIRED =                0x00001000, #!< device is paired TO SELF 
IS_ETH_CTRLSTATUS_OPENED =                0x00004000, #!< device is opened BY SELF 
IS_ETH_CTRLSTATUS_FW_UPLOAD_STARTER =     0x00010000, #!< device is receiving the starter firmware 
IS_ETH_CTRLSTATUS_FW_UPLOAD_RUNTIME =     0x00020000, #!< device is receiving the runtime firmware 
IS_ETH_CTRLSTATUS_REBOOTING =             0x00100000, #!< device is rebooting 
IS_ETH_CTRLSTATUS_BOOTBOOST_ENABLED =     0x01000000, #!< boot-boosting is enabled for this device 
IS_ETH_CTRLSTATUS_BOOTBOOST_ACTIVE =      0x02000000, #!< boot-boosting is active for this device 
IS_ETH_CTRLSTATUS_INITIALIZED =           0x08000000, #!< device object is initialized 
IS_ETH_CTRLSTATUS_TO_BE_DELETED =         0x40000000, #!< device object is being deleted 
IS_ETH_CTRLSTATUS_TO_BE_REMOVED =         0x80000000, #!< device object is being removed 
IS_ETH_PCKTFLT_PASSALL=       0,  #!< pass all packets to OS 
IS_ETH_PCKTFLT_BLOCKUEGET=    1,  #!< block UEGET packets to the OS 
IS_ETH_PCKTFLT_BLOCKALL=      2   #!< block all packets to the OS 
IS_ETH_LINKSPEED_100MB=		100,    #!< 100 MBits 
IS_ETH_LINKSPEED_1000MB=	    1000    #!< 1000 MBits 
IPCONFIG_CAP_PERSISTENT_IP_SUPPORTED    = 0x01
IPCONFIG_CAP_AUTOCONFIG_IP_SUPPORTED    = 0x04
IPCONFIG_CMD_QUERY_CAPABILITIES             = 0
IPCONFIG_CMD_SET_PERSISTENT_IP              = 0x01010000
IPCONFIG_CMD_SET_AUTOCONFIG_IP              = 0x01040000
IPCONFIG_CMD_SET_AUTOCONFIG_IP_BYDEVICE     = 0x01040100
IPCONFIG_CMD_RESERVED1                      = 0x01080000
IPCONFIG_CMD_GET_PERSISTENT_IP              = 0x02010000
IPCONFIG_CMD_GET_AUTOCONFIG_IP              = 0x02040000
IPCONFIG_CMD_GET_AUTOCONFIG_IP_BYDEVICE     = 0x02040100
IS_CONFIG_CPU_IDLE_STATES_BIT_AC_VALUE         = 0x01, #!< Mains power 
IS_CONFIG_CPU_IDLE_STATES_BIT_DC_VALUE         = 0x02, #!< Battery power 
IS_CONFIG_IPO_NOT_ALLOWED                      = 0
IS_CONFIG_IPO_ALLOWED                          = 1
IS_CONFIG_OPEN_MP_DISABLE                      = 0
IS_CONFIG_OPEN_MP_ENABLE                       = 1
IS_CONFIG_INITIAL_PARAMETERSET_NONE            = 0
IS_CONFIG_INITIAL_PARAMETERSET_1               = 1
IS_CONFIG_INITIAL_PARAMETERSET_2               = 2
IS_CONFIG_ETH_CONFIGURATION_MODE_OFF           = 0
IS_CONFIG_ETH_CONFIGURATION_MODE_ON            = 1
IS_CONFIG_TRUSTED_PAIRING_OFF                   = 0
IS_CONFIG_TRUSTED_PAIRING_ON                    = 1 
IS_CONFIG_CMD_GET_CAPABILITIES                         = 1, #!< Get supported configuration capabilities (bitmask of CONFIGURATION_CAPS)
IS_CONFIG_CPU_IDLE_STATES_CMD_GET_ENABLE               = 2, #!< Get the current CPU idle states enable state (bitmask of CONFIGURATION_SEL)
IS_CONFIG_CPU_IDLE_STATES_CMD_SET_DISABLE_ON_OPEN      = 4, #!< Disable migration to other CPU idle states (other than C0) if the first USB camera is being opened
IS_CONFIG_CPU_IDLE_STATES_CMD_GET_DISABLE_ON_OPEN      = 5, #!< Get the current setting of the command IS_CPU_IDLE_STATES_CMD_SET_DISABLE_ON_OPEN
IS_CONFIG_OPEN_MP_CMD_GET_ENABLE                       = 6
IS_CONFIG_OPEN_MP_CMD_SET_ENABLE                       = 7
IS_CONFIG_OPEN_MP_CMD_GET_ENABLE_DEFAULT               = 8
IS_CONFIG_INITIAL_PARAMETERSET_CMD_SET                 = 9
IS_CONFIG_INITIAL_PARAMETERSET_CMD_GET                 = 10
IS_CONFIG_ETH_CONFIGURATION_MODE_CMD_SET_ENABLE        = 11
IS_CONFIG_ETH_CONFIGURATION_MODE_CMD_GET_ENABLE        = 12
IS_CONFIG_IPO_CMD_GET_ALLOWED                          = 13
IS_CONFIG_IPO_CMD_SET_ALLOWED                          = 14
IS_CONFIG_CMD_TRUSTED_PAIRING_SET                       = 15
IS_CONFIG_CMD_TRUSTED_PAIRING_GET                       = 16
IS_CONFIG_CMD_TRUSTED_PAIRING_GET_DEFAULT               = 17
IS_CONFIG_CPU_IDLE_STATES_CAP_SUPPORTED                = 0x00000001, #!< CPU idle state commands are supported by the SDK 
IS_CONFIG_OPEN_MP_CAP_SUPPORTED                        = 0x00000002, #!< Open MP commands are supported by the SDK 
IS_CONFIG_INITIAL_PARAMETERSET_CAP_SUPPORTED           = 0x00000004, #!< Initial parameter set commands are supported by the SDK 
IS_CONFIG_IPO_CAP_SUPPORTED                            = 0x00000008, #!< "Intel Performance Thread" is supported by the SDK 
IS_CONFIG_TRUSTED_PAIRING_CAP_SUPPORTED                = 0x00000010  #!< Camera supports trusted pairing when network connection was lost 
IO_LED_STATE_1 = 0
IO_LED_STATE_2 = 1
IO_FLASH_MODE_OFF = 0
IO_FLASH_MODE_TRIGGER_LO_ACTIVE = 1
IO_FLASH_MODE_TRIGGER_HI_ACTIVE = 2
IO_FLASH_MODE_CONSTANT_HIGH = 3
IO_FLASH_MODE_CONSTANT_LOW = 4
IO_FLASH_MODE_FREERUN_LO_ACTIVE = 5
IO_FLASH_MODE_FREERUN_HI_ACTIVE = 6
IS_FLASH_MODE_PWM = 0x8000
IO_FLASH_MODE_GPIO_1 = 0x0010
IO_FLASH_MODE_GPIO_2 = 0x0020
IO_FLASH_MODE_GPIO_3 = 0x0040
IO_FLASH_MODE_GPIO_4 = 0x0080
IO_FLASH_MODE_GPIO_5 = 0x0100
IO_FLASH_MODE_GPIO_6 = 0x0200
IO_FLASH_GPIO_PORT_MASK = (IO_FLASH_MODE_GPIO_1 | IO_FLASH_MODE_GPIO_2 | IO_FLASH_MODE_GPIO_3 | IO_FLASH_MODE_GPIO_4 | IO_FLASH_MODE_GPIO_5 | IO_FLASH_MODE_GPIO_6)  
IO_GPIO_1 = 0x0001
IO_GPIO_2 = 0x0002
IO_GPIO_3 = 0x0004
IO_GPIO_4 = 0x0008
IO_GPIO_5 = 0x0010
IO_GPIO_6 = 0x0020
IS_GPIO_INPUT = 0x0001
IS_GPIO_OUTPUT = 0x0002
IS_GPIO_FLASH = 0x0004
IS_GPIO_PWM = 0x0008
IS_GPIO_COMPORT_RX = 0x0010
IS_GPIO_COMPORT_TX = 0x0020
IS_GPIO_MULTI_INTEGRATION_MODE = 0x0040
IS_GPIO_TRIGGER = 0x0080
IS_FLASH_AUTO_FREERUN_OFF = 0
IS_FLASH_AUTO_FREERUN_ON = 1
IS_IO_CMD_GPIOS_GET_SUPPORTED               = 1
IS_IO_CMD_GPIOS_GET_SUPPORTED_INPUTS        = 2
IS_IO_CMD_GPIOS_GET_SUPPORTED_OUTPUTS       = 3
IS_IO_CMD_GPIOS_GET_DIRECTION               = 4
IS_IO_CMD_GPIOS_SET_DIRECTION               = 5
IS_IO_CMD_GPIOS_GET_STATE                   = 6
IS_IO_CMD_GPIOS_SET_STATE                   = 7
IS_IO_CMD_LED_GET_STATE                     = 8
IS_IO_CMD_LED_SET_STATE                     = 9
IS_IO_CMD_LED_TOGGLE_STATE                  = 10
IS_IO_CMD_FLASH_GET_GLOBAL_PARAMS           = 11, 
IS_IO_CMD_FLASH_APPLY_GLOBAL_PARAMS         = 12
IS_IO_CMD_FLASH_GET_SUPPORTED_GPIOS         = 13
IS_IO_CMD_FLASH_GET_PARAMS_MIN              = 14
IS_IO_CMD_FLASH_GET_PARAMS_MAX              = 15
IS_IO_CMD_FLASH_GET_PARAMS_INC              = 16
IS_IO_CMD_FLASH_GET_PARAMS                  = 17
IS_IO_CMD_FLASH_SET_PARAMS                  = 18
IS_IO_CMD_FLASH_GET_MODE                    = 19
IS_IO_CMD_FLASH_SET_MODE                    = 20
IS_IO_CMD_PWM_GET_SUPPORTED_GPIOS           = 21,    
IS_IO_CMD_PWM_GET_PARAMS_MIN                = 22
IS_IO_CMD_PWM_GET_PARAMS_MAX                = 23
IS_IO_CMD_PWM_GET_PARAMS_INC                = 24
IS_IO_CMD_PWM_GET_PARAMS                    = 25
IS_IO_CMD_PWM_SET_PARAMS                    = 26
IS_IO_CMD_PWM_GET_MODE                      = 27
IS_IO_CMD_PWM_SET_MODE                      = 28
IS_IO_CMD_GPIOS_GET_CONFIGURATION           = 29
IS_IO_CMD_GPIOS_SET_CONFIGURATION           = 30
IS_IO_CMD_FLASH_GET_GPIO_PARAMS_MIN         = 31
IS_IO_CMD_FLASH_SET_GPIO_PARAMS             = 32
IS_IO_CMD_FLASH_GET_AUTO_FREERUN_DEFAULT    = 33
IS_IO_CMD_FLASH_GET_AUTO_FREERUN            = 34
IS_IO_CMD_FLASH_SET_AUTO_FREERUN            = 35
IS_AWB_CMD_GET_SUPPORTED_TYPES              = 1
IS_AWB_CMD_GET_TYPE                         = 2
IS_AWB_CMD_SET_TYPE                         = 3
IS_AWB_CMD_GET_ENABLE                       = 4
IS_AWB_CMD_SET_ENABLE                       = 5
IS_AWB_CMD_GET_SUPPORTED_RGB_COLOR_MODELS   = 6
IS_AWB_CMD_GET_RGB_COLOR_MODEL              = 7
IS_AWB_CMD_SET_RGB_COLOR_MODEL              = 8
IS_AWB_GREYWORLD = 0x0001
IS_AWB_COLOR_TEMPERATURE = 0x0002
IS_AUTOPARAMETER_DISABLE = 0
IS_AUTOPARAMETER_ENABLE = 1
IS_AUTOPARAMETER_ENABLE_RUNONCE = 2
IS_CONVERT_CMD_APPLY_PARAMS_AND_CONVERT_BUFFER = 1
IS_PARAMETERSET_CMD_LOAD_EEPROM                         = 1
IS_PARAMETERSET_CMD_LOAD_FILE                           = 2
IS_PARAMETERSET_CMD_SAVE_EEPROM                         = 3
IS_PARAMETERSET_CMD_SAVE_FILE                           = 4
IS_PARAMETERSET_CMD_GET_NUMBER_SUPPORTED                = 5
IS_PARAMETERSET_CMD_GET_HW_PARAMETERSET_AVAILABLE       = 6
IS_PARAMETERSET_CMD_ERASE_HW_PARAMETERSET               = 7
IS_EDGE_ENHANCEMENT_CMD_GET_RANGE   = 1
IS_EDGE_ENHANCEMENT_CMD_GET_DEFAULT = 2
IS_EDGE_ENHANCEMENT_CMD_GET         = 3
IS_EDGE_ENHANCEMENT_CMD_SET         = 4
IS_PIXELCLOCK_CMD_GET_NUMBER    = 1
IS_PIXELCLOCK_CMD_GET_LIST      = 2
IS_PIXELCLOCK_CMD_GET_RANGE     = 3
IS_PIXELCLOCK_CMD_GET_DEFAULT   = 4
IS_PIXELCLOCK_CMD_GET           = 5
IS_PIXELCLOCK_CMD_SET           = 6
IS_IMAGE_FILE_CMD_LOAD    = 1
IS_IMAGE_FILE_CMD_SAVE    = 2
IS_AUTO_BLACKLEVEL_OFF = 0
IS_AUTO_BLACKLEVEL_ON  = 1
IS_BLACKLEVEL_CAP_SET_AUTO_BLACKLEVEL   = 1
IS_BLACKLEVEL_CAP_SET_OFFSET            = 2
IS_BLACKLEVEL_CMD_GET_CAPS           = 1
IS_BLACKLEVEL_CMD_GET_MODE_DEFAULT   = 2
IS_BLACKLEVEL_CMD_GET_MODE           = 3
IS_BLACKLEVEL_CMD_SET_MODE           = 4
IS_BLACKLEVEL_CMD_GET_OFFSET_DEFAULT = 5
IS_BLACKLEVEL_CMD_GET_OFFSET_RANGE   = 6
IS_BLACKLEVEL_CMD_GET_OFFSET         = 7
IS_BLACKLEVEL_CMD_SET_OFFSET         = 8
IS_IMGBUF_DEVMEM_CMD_GET_AVAILABLE_ITERATIONS      = 1
IS_IMGBUF_DEVMEM_CMD_GET_ITERATION_INFO            = 2
IS_IMGBUF_DEVMEM_CMD_TRANSFER_IMAGE                = 3
IS_IMGBUF_DEVMEM_CMD_RELEASE_ITERATIONS            = 4
IS_MEASURE_CMD_SHARPNESS_AOI_SET		= 1
IS_MEASURE_CMD_SHARPNESS_AOI_INQUIRE	= 2
IS_MEASURE_CMD_SHARPNESS_AOI_SET_PRESET	= 3
IS_MEASURE_SHARPNESS_AOI_PRESET_1 = 1
IS_LUT_64 = 64
IS_LUT_128 = 128
IS_LUT_PRESET_ID_IDENTITY = 0
IS_LUT_PRESET_ID_NEGATIVE = 1
IS_LUT_PRESET_ID_GLOW1 = 2
IS_LUT_PRESET_ID_GLOW2 = 3
IS_LUT_PRESET_ID_ASTRO1 = 4
IS_LUT_PRESET_ID_RAINBOW1 = 5
IS_LUT_PRESET_ID_MAP1 = 6
IS_LUT_PRESET_ID_HOT = 7
IS_LUT_PRESET_ID_SEPIC = 8
IS_LUT_PRESET_ID_ONLY_RED = 9
IS_LUT_PRESET_ID_ONLY_GREEN = 10
IS_LUT_PRESET_ID_ONLY_BLUE = 11
IS_LUT_PRESET_ID_DIGITAL_GAIN_2X = 12
IS_LUT_PRESET_ID_DIGITAL_GAIN_4X = 13
IS_LUT_PRESET_ID_DIGITAL_GAIN_8X = 14
IS_LUT_CMD_SET_ENABLED = 0x0001
IS_LUT_CMD_SET_MODE = 0x0002
IS_LUT_CMD_GET_STATE = 0x0005
IS_LUT_CMD_GET_SUPPORT_INFO = 0x0006
IS_LUT_CMD_SET_USER_LUT = 0x0010
IS_LUT_CMD_GET_USER_LUT = 0x0011
IS_LUT_CMD_GET_COMPLETE_LUT = 0x0012
IS_LUT_CMD_GET_PRESET_LUT = 0x0013
IS_LUT_CMD_LOAD_FILE = 0x0100
IS_LUT_CMD_SAVE_FILE = 0x0101
IS_LUT_STATE_ID_FLAG_HARDWARE = 0x0010
IS_LUT_STATE_ID_FLAG_SOFTWARE = 0x0020
IS_LUT_STATE_ID_FLAG_GAMMA = 0x0100
IS_LUT_STATE_ID_FLAG_LUT = 0x0200
IS_LUT_STATE_ID_INACTIVE = 0x0000
IS_LUT_STATE_ID_NOT_SUPPORTED = 0x0001
IS_LUT_STATE_ID_HARDWARE_LUT = (IS_LUT_STATE_ID_FLAG_HARDWARE | IS_LUT_STATE_ID_FLAG_LUT)
IS_LUT_STATE_ID_HARDWARE_GAMMA = (IS_LUT_STATE_ID_FLAG_HARDWARE | IS_LUT_STATE_ID_FLAG_GAMMA)
IS_LUT_STATE_ID_HARDWARE_LUTANDGAMMA = (IS_LUT_STATE_ID_FLAG_HARDWARE | IS_LUT_STATE_ID_FLAG_LUT | IS_LUT_STATE_ID_FLAG_GAMMA)
IS_LUT_STATE_ID_SOFTWARE_LUT = (IS_LUT_STATE_ID_FLAG_SOFTWARE | IS_LUT_STATE_ID_FLAG_LUT)
IS_LUT_STATE_ID_SOFTWARE_GAMMA = (IS_LUT_STATE_ID_FLAG_SOFTWARE | IS_LUT_STATE_ID_FLAG_GAMMA)
IS_LUT_STATE_ID_SOFTWARE_LUTANDGAMMA = (IS_LUT_STATE_ID_FLAG_SOFTWARE | IS_LUT_STATE_ID_FLAG_LUT | IS_LUT_STATE_ID_FLAG_GAMMA)
IS_LUT_MODE_ID_DEFAULT = 0
IS_LUT_MODE_ID_FORCE_HARDWARE = 1
IS_LUT_MODE_ID_FORCE_SOFTWARE = 2
IS_LUT_DISABLED = 0
IS_LUT_ENABLED = 1
IS_GAMMA_CMD_SET = 0x0001
IS_GAMMA_CMD_GET_DEFAULT = 0x0002
IS_GAMMA_CMD_GET = 0x0003
IS_GAMMA_VALUE_MIN = 1
IS_GAMMA_VALUE_MAX = 1000
IS_MEMORY_GET_SIZE  = 1
IS_MEMORY_READ      = 2
IS_MEMORY_WRITE     = 3
IS_MEMORY_USER_1    = 1
IS_MEMORY_USER_2    = 2
IS_MC_CMD_FLAG_ACTIVE = 0x1000
IS_MC_CMD_FLAG_PASSIVE = 0x2000
# is_Multicast() commands for passive mode (listener only) 
IS_PMC_CMD_INITIALIZE = (   0x0001 | IS_MC_CMD_FLAG_PASSIVE )
IS_PMC_CMD_DEINITIALIZE = (   0x0002 | IS_MC_CMD_FLAG_PASSIVE )
IS_PMC_CMD_ADDMCDEVICE = (   0x0003 | IS_MC_CMD_FLAG_PASSIVE )
IS_PMC_CMD_REMOVEMCDEVICE = (   0x0004 | IS_MC_CMD_FLAG_PASSIVE )
IS_PMC_CMD_STOREDEVICES = (   0x0005 | IS_MC_CMD_FLAG_PASSIVE )
IS_PMC_CMD_LOADDEVICES = (   0x0006 | IS_MC_CMD_FLAG_PASSIVE )
IS_PMC_CMD_SYSTEM_SET_ENABLE = (   0x0007 | IS_MC_CMD_FLAG_PASSIVE )
IS_PMC_CMD_SYSTEM_GET_ENABLE = (   0x0008 | IS_MC_CMD_FLAG_PASSIVE )
IS_PMC_CMD_REMOVEALLMCDEVICES = (   0x0009 | IS_MC_CMD_FLAG_PASSIVE )
# is_Multicast() commands for active mode (master) 
IS_AMC_CMD_SET_MC_IP = (   0x0010 | IS_MC_CMD_FLAG_ACTIVE )
IS_AMC_CMD_GET_MC_IP = (   0x0011 | IS_MC_CMD_FLAG_ACTIVE )
IS_AMC_CMD_SET_MC_ENABLED = (   0x0012 | IS_MC_CMD_FLAG_ACTIVE )
IS_AMC_CMD_GET_MC_ENABLED = (   0x0013 | IS_MC_CMD_FLAG_ACTIVE )
IS_AMC_CMD_GET_MC_SUPPORTED = (   0x0014 | IS_MC_CMD_FLAG_ACTIVE )
IS_AMC_SUPPORTED_FLAG_DEVICE = (   0x0001 )
IS_AMC_SUPPORTED_FLAG_FIRMWARE = (   0x0002 )
IS_PMC_ERRORHANDLING_REJECT_IMAGES = 0x01
IS_PMC_ERRORHANDLING_IGNORE_MISSING_PARTS = 0x02
IS_PMC_ERRORHANDLING_MERGE_IMAGES_RELEASE_ON_COMPLETE = 0x03
IS_PMC_ERRORHANDLING_MERGE_IMAGES_RELEASE_ON_RECEIVED_IMGLEN = 0x04
