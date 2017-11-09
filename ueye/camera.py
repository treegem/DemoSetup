import numpy


class Camera(object):
    """
    class Camera - base class describing minimum functionality of a camera
    """

    aoi = (0, 0, 1024, 768)
    roi = numpy.array([])  # list of regions of interest

    def __init__(self):
        self.roi = numpy.zeros((self.aoi[3], self.aoi[2]))

    def set_exposure(self, dt):
        pass

    def acquire_image(self):
        return numpy.zeros((self.aoi[3], self.aoi[2]))

    def acquire_image_roi(self):
        return numpy.zeros((self.roi.max() + 2,))

    def arm_video(self, nframes, timeout=30):
        """
        arm_video - prepare hardware triggered acquisition of nframes frames of video
        """
        pass

    def get_video(self):
        """
        get_video - wait for previously started acquisition to finish and retrieve video data
                         returns raw frame data
        """
        return numpy.zeros((nframes, self.aoi[3], self.aoi[2]))

    def get_video_roi(self):
        """
        get_video_roi - wait for previously started acquisition to finish and retrieve video data
                             returns counts for all rois
        """
        pass

    def acquire_video(self, nframes, timeout=30):
        """
        acquire_video - blocking video acquisition, free running acquisition
                        returns raw frame data
        """
        return numpy.zeros((nframes, self.aoi[3], self.aoi[2]))

    def acquire_video_roi(self, nframes, timeout=30):
        return numpy.zeros((nframes, self.roi.max() + 2))
