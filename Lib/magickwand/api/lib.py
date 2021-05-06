import platform
from ctypes import CDLL
from ctypes.util import find_library


platform_type = platform.uname()[0]
if platform_type == "Darwin":
    # I suppose that ImageMagick is here
    MagickWand = CDLL( "/opt/local/lib/libMagickWand.dylib" )
elif platform_type == "Linux":
    MagickWand = CDLL( find_library( 'MagickWand' ) )
else:pass

