from ctypes import ( c_int,
                     c_uint,
                     c_ubyte,
                     c_ushort,
                     c_double,
                     c_long,
                     c_longlong,
                     c_ulong,
                     c_ulonglong,
                     c_char,
                     c_char_p,
                     c_wchar_p,
                     c_void_p,
                     CFUNCTYPE,
                     POINTER,
                     Structure
                    )
STRING = c_char_p
WSTRING = c_wchar_p
# values for enumeration 'MapMode'
MapMode = c_int # enum
size_t = c_uint
Quantum = c_ushort
IndexPacket = Quantum
# values for enumeration 'MagickBooleanType'
MagickBooleanType = c_int # enum
# values for enumeration 'ComplianceType'
ComplianceType = c_int # enum
# values for enumeration 'ClassType'
ClassType = c_int # enum
# values for enumeration 'ColorspaceType'
ColorspaceType = c_int # enum

MagickRealType = c_double
MagickSizeType = c_ulonglong
MagickStatusType = c_uint

# values for enumeration 'VirtualPixelMethod'
VirtualPixelMethod = c_int # enum
# values for enumeration 'CompressionType'
CompressionType = c_int # enum
# values for enumeration 'MetricType'
MetricType = c_int # enum
# values for enumeration 'ChannelType'
ChannelType = c_int # enum
# values for enumeration 'CompositeOperator'
CompositeOperator = c_int # enum
# values for enumeration 'StorageType'
StorageType = c_int # enum
# values for enumeration 'MagickLayerMethod'
MagickLayerMethod = c_int # enum
ExtendedSignedIntegralType = c_longlong
ExtendedUnsignedIntegralType = c_ulonglong

__gnuc_va_list = STRING
va_list = __gnuc_va_list

# values for enumeration 'QuantumType'
QuantumType = c_int # enum
QuantumAny = c_ulong

# values for enumeration 'TimerState'
TimerState = c_int # enum

# values for enumeration 'ExceptionType'
ExceptionType = c_int # enum

# values for enumeration 'DistortImageMethod'
DistortImageMethod = c_int # enum

# values for enumeration 'AlignType'
AlignType = c_int # enum

# values for enumeration 'ClipPathUnits'
ClipPathUnits = c_int # enum

# values for enumeration 'DecorationType'
DecorationType = c_int # enum

# values for enumeration 'FillRule'
FillRule = c_int # enum

# values for enumeration 'GradientType'
GradientType = c_int # enum

# values for enumeration 'LineCap'
LineCap = c_int # enum

# values for enumeration 'LineJoin'
LineJoin = c_int # enum

# values for enumeration 'PrimitiveType'
PrimitiveType = c_int # enum

# values for enumeration 'ReferenceType'
ReferenceType = c_int # enum

# values for enumeration 'SpreadMethod'
SpreadMethod = c_int # enum

# values for enumeration 'GravityType'
GravityType = c_int # enum

# values for enumeration 'StyleType'
StyleType = c_int # enum

# values for enumeration 'StretchType'
StretchType = c_int # enum

# values for enumeration 'GeometryFlags'
GeometryFlags = c_int # enum

# values for enumeration 'AlphaChannelType'
AlphaChannelType = c_int # enum

# values for enumeration 'ImageType'
ImageType = c_int # enum

# values for enumeration 'InterlaceType'
InterlaceType = c_int # enum

# values for enumeration 'OrientationType'
OrientationType = c_int # enum

# values for enumeration 'ResolutionType'
ResolutionType = c_int # enum

# values for enumeration 'NoiseType'
NoiseType = c_int # enum

# values for enumeration 'PreviewType'
PreviewType = c_int # enum

# values for enumeration 'MagickEvaluateOperator'
MagickEvaluateOperator = c_int # enum

# values for enumeration 'TransmitType'
TransmitType = c_int # enum

# values for enumeration 'RenderingIntent'
RenderingIntent = c_int # enum

# values for enumeration 'FilterTypes'
FilterTypes = c_int # enum

# values for enumeration 'EndianType'
EndianType = c_int # enum

# values for enumeration 'DisposeType'
DisposeType = c_int # enum

# values for enumeration 'InterpolatePixelMethod'
InterpolatePixelMethod = c_int # enum

# values for enumeration 'LogEventType'
LogEventType = c_int # enum

# values for enumeration 'MagickThreadSupport'
MagickThreadSupport = c_int # enum

# values for enumeration 'MagickModuleType'
MagickModuleType = c_int # enum

# values for enumeration 'MontageMode'
MontageMode = c_int # enum

# values for enumeration 'MagickOption'
MagickOption = c_int # enum

# values for enumeration 'QuantumFormatType'
QuantumFormatType = c_int # enum

# values for enumeration 'ResourceType'
ResourceType = c_int # enum

# values for enumeration 'PathType'
PathType = c_int # enum

# values for enumeration 'ImageLayerMethod'
ImageLayerMethod = c_int # enum

# values for enumeration 'PaintMethod'
PaintMethod = c_int # enum

# values for enumeration 'RegistryType'
RegistryType = c_int # enum

MagickOffsetType = c_longlong



#------------------------------------------------------------------------------ 



#------------------------------------------------------------------------------ 
class SemaphoreInfo( Structure ): pass
SemaphoreInfo._fields_ = []
#------------------------------------------------------------------------------ 
class _Ascii85Info( Structure ): pass
_Ascii85Info._fields_ = []
Ascii85Info = _Ascii85Info
#------------------------------------------------------------------------------ 
class _MagickWand( Structure ): pass
_MagickWand._fields_ = []
MagickWand = _MagickWand
#------------------------------------------------------------------------------ 
class _PixelIterator( Structure ): pass
_PixelIterator._fields_ = []
PixelIterator = _PixelIterator
#------------------------------------------------------------------------------ 
class _DrawingWand( Structure ): pass
_DrawingWand._fields_ = []
DrawingWand = _DrawingWand
#------------------------------------------------------------------------------ 
class _SignatureInfo( Structure ): pass
_SignatureInfo._fields_ = []
SignatureInfo = _SignatureInfo
#------------------------------------------------------------------------------ 
class _SplayTreeInfo( Structure ): pass
_SplayTreeInfo._fields_ = []
SplayTreeInfo = _SplayTreeInfo
#------------------------------------------------------------------------------ 
class _ViewInfo( Structure ): pass
_ViewInfo._fields_ = []
ViewInfo = _ViewInfo
#------------------------------------------------------------------------------ 
class _LinkedListInfo( Structure ):
    pass
_LinkedListInfo._fields_ = []
LinkedListInfo = _LinkedListInfo
#------------------------------------------------------------------------------ 
class _RectangleInfo( Structure ): pass
_RectangleInfo._fields_ = [
    ( 'width', c_ulong ),
    ( 'height', c_ulong ),
    ( 'x', c_long ),
    ( 'y', c_long ),
]
RectangleInfo = _RectangleInfo
#------------------------------------------------------------------------------ 
class _ResampleFilter( Structure ): pass
_ResampleFilter._fields_ = []
ResampleFilter = _ResampleFilter
#------------------------------------------------------------------------------ 
class _MimeInfo( Structure ): pass
_MimeInfo._fields_ = []
MimeInfo = _MimeInfo
#------------------------------------------------------------------------------ 
class _LogInfo( Structure ): pass
_LogInfo._fields_ = []
LogInfo = _LogInfo
#------------------------------------------------------------------------------ 
class _BlobInfo( Structure ): pass
_BlobInfo._fields_ = []
BlobInfo = _BlobInfo
#------------------------------------------------------------------------------ 
class _HashmapInfo( Structure ): pass
_HashmapInfo._fields_ = []
HashmapInfo = _HashmapInfo
#------------------------------------------------------------------------------ 
class _IO_FILE( Structure ): pass
FILE = _IO_FILE
#------------------------------------------------------------------------------ 
class _PixelPacket( Structure ): pass
_PixelPacket._fields_ = [
    ( 'blue', Quantum ),
    ( 'green', Quantum ),
    ( 'red', Quantum ),
    ( 'opacity', Quantum ),
]
PixelPacket = _PixelPacket
#------------------------------------------------------------------------------ 
class _ThresholdMap( Structure ): pass
_ThresholdMap._fields_ = []
ThresholdMap = _ThresholdMap
#------------------------------------------------------------------------------ 
class _TokenInfo( Structure ): pass
_TokenInfo._fields_ = []
TokenInfo = _TokenInfo
#------------------------------------------------------------------------------ 
class _PixelWand( Structure ): pass
_PixelWand._fields_ = []
PixelWand = _PixelWand
#------------------------------------------------------------------------------ 
class _PrimaryInfo( Structure ): pass
_PrimaryInfo._pack_ = 4
_PrimaryInfo._fields_ = [
    ( 'x', c_double ),
    ( 'y', c_double ),
    ( 'z', c_double ),
]
PrimaryInfo = _PrimaryInfo
#------------------------------------------------------------------------------ 
class _ErrorInfo( Structure ): pass
_ErrorInfo._pack_ = 4
_ErrorInfo._fields_ = [
    ( 'mean_error_per_pixel', c_double ),
    ( 'normalized_mean_error', c_double ),
    ( 'normalized_maximum_error', c_double ),
]
ErrorInfo = _ErrorInfo
#------------------------------------------------------------------------------ 
class _ExceptionInfo( Structure ): pass
_ExceptionInfo._fields_ = [
    ( 'severity', ExceptionType ),
    ( 'error_number', c_int ),
    ( 'reason', STRING ),
    ( 'description', STRING ),
    ( 'exceptions', c_void_p ),
    ( 'relinquish', MagickBooleanType ),
    ( 'semaphore', POINTER( SemaphoreInfo ) ),
    ( 'signature', c_ulong ),
]
ExceptionInfo = _ExceptionInfo
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 



#------------------------------------------------------------------------------ 
class _QuantumInfo( Structure ): pass
_QuantumInfo._pack_ = 4
_QuantumInfo._fields_ = [
    ( 'quantum', c_ulong ),
    ( 'format', QuantumFormatType ),
    ( 'minimum', c_double ),
    ( 'maximum', c_double ),
    ( 'scale', c_double ),
    ( 'pad', size_t ),
    ( 'min_is_white', MagickBooleanType ),
    ( 'pack', MagickBooleanType ),
    ( 'semaphore', POINTER( SemaphoreInfo ) ),
    ( 'signature', c_ulong ),
]
QuantumInfo = _QuantumInfo
#------------------------------------------------------------------------------ 
class _QuantizeInfo( Structure ): pass
_QuantizeInfo._fields_ = [
    ( 'number_colors', c_ulong ),
    ( 'tree_depth', c_ulong ),
    ( 'dither', MagickBooleanType ),
    ( 'colorspace', ColorspaceType ),
    ( 'measure_error', MagickBooleanType ),
    ( 'signature', c_ulong ),
]
QuantizeInfo = _QuantizeInfo
#------------------------------------------------------------------------------ 
class _StringInfo( Structure ): pass
_StringInfo._fields_ = [
    ( 'path', c_char * 4096 ),
    ( 'datum', POINTER( c_ubyte ) ),
    ( 'length', size_t ),
    ( 'signature', c_ulong ),
]
StringInfo = _StringInfo
#------------------------------------------------------------------------------ 
class _LongPixelPacket( Structure ): pass
_LongPixelPacket._fields_ = [
    ( 'red', c_ulong ),
    ( 'green', c_ulong ),
    ( 'blue', c_ulong ),
    ( 'opacity', c_ulong ),
    ( 'index', c_ulong ),
]
LongPixelPacket = _LongPixelPacket
#------------------------------------------------------------------------------ 
class _OptionInfo( Structure ): pass
_OptionInfo._fields_ = [
    ( 'mnemonic', STRING ),
    ( 'type', c_long ),
]
OptionInfo = _OptionInfo
#------------------------------------------------------------------------------ 
class _MontageInfo( Structure ): pass
_MontageInfo._pack_ = 4
_MontageInfo._fields_ = [
    ( 'geometry', STRING ),
    ( 'tile', STRING ),
    ( 'title', STRING ),
    ( 'frame', STRING ),
    ( 'texture', STRING ),
    ( 'font', STRING ),
    ( 'pointsize', c_double ),
    ( 'border_width', c_ulong ),
    ( 'shadow', MagickBooleanType ),
    ( 'fill', PixelPacket ),
    ( 'stroke', PixelPacket ),
    ( 'background_color', PixelPacket ),
    ( 'border_color', PixelPacket ),
    ( 'matte_color', PixelPacket ),
    ( 'gravity', GravityType ),
    ( 'filename', c_char * 4096 ),
    ( 'debug', MagickBooleanType ),
    ( 'signature', c_ulong ),
]
MontageInfo = _MontageInfo
#------------------------------------------------------------------------------ 
class _ModuleInfo( Structure ): pass
__time_t = c_long
time_t = __time_t
_ModuleInfo._fields_ = [
    ( 'path', STRING ),
    ( 'tag', STRING ),
    ( 'handle', c_void_p ),
    ( 'unregister_module', CFUNCTYPE( None ) ),
    ( 'register_module', CFUNCTYPE( c_ulong ) ),
    ( 'load_time', time_t ),
    ( 'stealth', MagickBooleanType ),
    ( 'previous', POINTER( _ModuleInfo ) ),
    ( 'next', POINTER( _ModuleInfo ) ),
    ( 'signature', c_ulong ),
]
ModuleInfo = _ModuleInfo
#------------------------------------------------------------------------------ 
class _MagicInfo( Structure ): pass
_MagicInfo._pack_ = 4
_MagicInfo._fields_ = [
    ( 'path', STRING ),
    ( 'name', STRING ),
    ( 'target', STRING ),
    ( 'magic', POINTER( c_ubyte ) ),
    ( 'length', size_t ),
    ( 'offset', MagickOffsetType ),
    ( 'stealth', MagickBooleanType ),
    ( 'previous', POINTER( _MagicInfo ) ),
    ( 'next', POINTER( _MagicInfo ) ),
    ( 'signature', c_ulong ),
]
MagicInfo = _MagicInfo
#------------------------------------------------------------------------------ 
class _LocaleInfo( Structure ): pass
_LocaleInfo._fields_ = [
    ( 'path', STRING ),
    ( 'tag', STRING ),
    ( 'message', STRING ),
    ( 'stealth', MagickBooleanType ),
    ( 'previous', POINTER( _LocaleInfo ) ),
    ( 'next', POINTER( _LocaleInfo ) ),
    ( 'signature', c_ulong ),
]
LocaleInfo = _LocaleInfo
#------------------------------------------------------------------------------ 
class _Timer( Structure ): pass
_Timer._pack_ = 4
_Timer._fields_ = [
    ( 'start', c_double ),
    ( 'stop', c_double ),
    ( 'total', c_double ),
]
Timer = _Timer
#------------------------------------------------------------------------------ 
class _TimerInfo( Structure ): pass
_TimerInfo._fields_ = [
    ( 'user', Timer ),
    ( 'elapsed', Timer ),
    ( 'state', TimerState ),
    ( 'signature', c_ulong ),
]
TimerInfo = _TimerInfo
#------------------------------------------------------------------------------ 
class _ProfileInfo( Structure ): pass
_ProfileInfo._fields_ = [
    ( 'name', STRING ),
    ( 'length', size_t ),
    ( 'info', POINTER( c_ubyte ) ),
    ( 'signature', c_ulong ),
]
ProfileInfo = _ProfileInfo
#------------------------------------------------------------------------------ 
class _ChromaticityInfo( Structure ): pass
_ChromaticityInfo._fields_ = [
    ( 'red_primary', PrimaryInfo ),
    ( 'green_primary', PrimaryInfo ),
    ( 'blue_primary', PrimaryInfo ),
    ( 'white_point', PrimaryInfo ),
]
ChromaticityInfo = _ChromaticityInfo
#------------------------------------------------------------------------------
MagickProgressMonitor = CFUNCTYPE( MagickBooleanType, STRING, MagickOffsetType, MagickSizeType, c_void_p )
#------------------------------------------------------------------------------ 
class _Image( Structure ): pass
Image = _Image
_Image._pack_ = 4
_Image._fields_ = [
    ( 'storage_class', ClassType ),
    ( 'colorspace', ColorspaceType ),
    ( 'compression', CompressionType ),
    ( 'quality', c_ulong ),
    ( 'orientation', OrientationType ),
    ( 'taint', MagickBooleanType ),
    ( 'matte', MagickBooleanType ),
    ( 'columns', c_ulong ),
    ( 'rows', c_ulong ),
    ( 'depth', c_ulong ),
    ( 'colors', c_ulong ),
    ( 'colormap', POINTER( PixelPacket ) ),
    ( 'background_color', PixelPacket ),
    ( 'border_color', PixelPacket ),
    ( 'matte_color', PixelPacket ),
    ( 'gamma', c_double ),
    ( 'chromaticity', ChromaticityInfo ),
    ( 'rendering_intent', RenderingIntent ),
    ( 'profiles', c_void_p ),
    ( 'units', ResolutionType ),
    ( 'montage', STRING ),
    ( 'directory', STRING ),
    ( 'geometry', STRING ),
    ( 'offset', c_long ),
    ( 'x_resolution', c_double ),
    ( 'y_resolution', c_double ),
    ( 'page', RectangleInfo ),
    ( 'extract_info', RectangleInfo ),
    ( 'tile_info', RectangleInfo ),
    ( 'bias', c_double ),
    ( 'blur', c_double ),
    ( 'fuzz', c_double ),
    ( 'filter', FilterTypes ),
    ( 'interlace', InterlaceType ),
    ( 'endian', EndianType ),
    ( 'gravity', GravityType ),
    ( 'compose', CompositeOperator ),
    ( 'dispose', DisposeType ),
    ( 'clip_mask', POINTER( _Image ) ),
    ( 'scene', c_ulong ),
    ( 'delay', c_ulong ),
    ( 'ticks_per_second', c_long ),
    ( 'iterations', c_ulong ),
    ( 'total_colors', c_ulong ),
    ( 'start_loop', c_long ),
    ( 'error', ErrorInfo ),
    ( 'timer', TimerInfo ),
    ( 'progress_monitor', MagickProgressMonitor ),
    ( 'client_data', c_void_p ),
    ( 'cache', c_void_p ),
    ( 'attributes', c_void_p ),
    ( 'ascii85', POINTER( Ascii85Info ) ),
    ( 'blob', POINTER( BlobInfo ) ),
    ( 'filename', c_char * 4096 ),
    ( 'magick_filename', c_char * 4096 ),
    ( 'magick', c_char * 4096 ),
    ( 'magick_columns', c_ulong ),
    ( 'magick_rows', c_ulong ),
    ( 'exception', ExceptionInfo ),
    ( 'debug', MagickBooleanType ),
    ( 'reference_count', c_long ),
    ( 'semaphore', POINTER( SemaphoreInfo ) ),
    ( 'color_profile', ProfileInfo ),
    ( 'iptc_profile', ProfileInfo ),
    ( 'generic_profile', POINTER( ProfileInfo ) ),
    ( 'generic_profiles', c_ulong ),
    ( 'signature', c_ulong ),
    ( 'previous', POINTER( _Image ) ),
    ( 'list', POINTER( _Image ) ),
    ( 'next', POINTER( _Image ) ),
    ( 'interpolate', InterpolatePixelMethod ),
    ( 'black_point_compensation', MagickBooleanType ),
    ( 'transparent_color', PixelPacket ),
    ( 'mask', POINTER( _Image ) ),
    ( 'tile_offset', RectangleInfo ),
    ( 'properties', c_void_p ),
    ( 'artifacts', c_void_p ),
]
#------------------------------------------------------------------------------ 
StreamHandler = CFUNCTYPE( size_t, POINTER( Image ), c_void_p, size_t )
#------------------------------------------------------------------------------ 
class _ImageInfo( Structure ): pass
ImageInfo = _ImageInfo
_ImageInfo._pack_ = 4
_ImageInfo._fields_ = [
    ( 'compression', CompressionType ),
    ( 'orientation', OrientationType ),
    ( 'temporary', MagickBooleanType ),
    ( 'adjoin', MagickBooleanType ),
    ( 'affirm', MagickBooleanType ),
    ( 'antialias', MagickBooleanType ),
    ( 'size', STRING ),
    ( 'extract', STRING ),
    ( 'page', STRING ),
    ( 'scenes', STRING ),
    ( 'scene', c_ulong ),
    ( 'number_scenes', c_ulong ),
    ( 'depth', c_ulong ),
    ( 'interlace', InterlaceType ),
    ( 'endian', EndianType ),
    ( 'units', ResolutionType ),
    ( 'quality', c_ulong ),
    ( 'sampling_factor', STRING ),
    ( 'server_name', STRING ),
    ( 'font', STRING ),
    ( 'texture', STRING ),
    ( 'density', STRING ),
    ( 'pointsize', c_double ),
    ( 'fuzz', c_double ),
    ( 'background_color', PixelPacket ),
    ( 'border_color', PixelPacket ),
    ( 'matte_color', PixelPacket ),
    ( 'dither', MagickBooleanType ),
    ( 'monochrome', MagickBooleanType ),
    ( 'colors', c_ulong ),
    ( 'colorspace', ColorspaceType ),
    ( 'type', ImageType ),
    ( 'preview_type', PreviewType ),
    ( 'group', c_long ),
    ( 'ping', MagickBooleanType ),
    ( 'verbose', MagickBooleanType ),
    ( 'view', STRING ),
    ( 'authenticate', STRING ),
    ( 'channel', ChannelType ),
    ( 'attributes', POINTER( Image ) ),
    ( 'options', c_void_p ),
    ( 'progress_monitor', MagickProgressMonitor ),
    ( 'client_data', c_void_p ),
    ( 'cache', c_void_p ),
    ( 'stream', StreamHandler ),
    ( 'file', POINTER( FILE ) ),
    ( 'blob', c_void_p ),
    ( 'length', size_t ),
    ( 'magick', c_char * 4096 ),
    ( 'unique', c_char * 4096 ),
    ( 'zero', c_char * 4096 ),
    ( 'filename', c_char * 4096 ),
    ( 'debug', MagickBooleanType ),
    ( 'tile', STRING ),
    ( 'subimage', c_ulong ),
    ( 'subrange', c_ulong ),
    ( 'pen', PixelPacket ),
    ( 'signature', c_ulong ),
    ( 'virtual_pixel_method', VirtualPixelMethod ),
    ( 'transparent_color', PixelPacket ),
    ( 'profile', c_void_p ),
]
#------------------------------------------------------------------------------ 
class _GeometryInfo( Structure ): pass
_GeometryInfo._pack_ = 4
_GeometryInfo._fields_ = [
    ( 'rho', c_double ),
    ( 'sigma', c_double ),
    ( 'xi', c_double ),
    ( 'psi', c_double ),
    ( 'chi', c_double ),
]
GeometryInfo = _GeometryInfo
#------------------------------------------------------------------------------ 
class _FrameInfo( Structure ): pass
_FrameInfo._fields_ = [
    ( 'width', c_ulong ),
    ( 'height', c_ulong ),
    ( 'x', c_long ),
    ( 'y', c_long ),
    ( 'inner_bevel', c_long ),
    ( 'outer_bevel', c_long ),
]
FrameInfo = _FrameInfo
#------------------------------------------------------------------------------ 
class _CoderInfo( Structure ): pass
_CoderInfo._fields_ = [
    ( 'path', STRING ),
    ( 'magick', STRING ),
    ( 'name', STRING ),
    ( 'stealth', MagickBooleanType ),
    ( 'previous', POINTER( _CoderInfo ) ),
    ( 'next', POINTER( _CoderInfo ) ),
    ( 'signature', c_ulong ),
]
CoderInfo = _CoderInfo
#------------------------------------------------------------------------------ 
class _DelegateInfo( Structure ): pass
_DelegateInfo._fields_ = [
    ( 'path', STRING ),
    ( 'decode', STRING ),
    ( 'encode', STRING ),
    ( 'commands', STRING ),
    ( 'mode', c_long ),
    ( 'thread_support', MagickBooleanType ),
    ( 'spawn', MagickBooleanType ),
    ( 'stealth', MagickBooleanType ),
    ( 'previous', POINTER( _DelegateInfo ) ),
    ( 'next', POINTER( _DelegateInfo ) ),
    ( 'signature', c_ulong ),
]
DelegateInfo = _DelegateInfo
#------------------------------------------------------------------------------ 
class _ImageAttribute( Structure ): pass
_ImageAttribute._fields_ = [
    ( 'key', STRING ),
    ( 'value', STRING ),
    ( 'compression', MagickBooleanType ),
    ( 'previous', POINTER( _ImageAttribute ) ),
    ( 'next', POINTER( _ImageAttribute ) ),
]
ImageAttribute = _ImageAttribute
#------------------------------------------------------------------------------ 
class _DoublePixelPacket( Structure ): pass
_DoublePixelPacket._pack_ = 4
_DoublePixelPacket._fields_ = [
    ( 'red', c_double ),
    ( 'green', c_double ),
    ( 'blue', c_double ),
    ( 'opacity', c_double ),
    ( 'index', c_double ),
]
DoublePixelPacket = _DoublePixelPacket
#------------------------------------------------------------------------------ 
class _MagickPixelPacket( Structure ): pass
_MagickPixelPacket._pack_ = 4
_MagickPixelPacket._fields_ = [
    ( 'storage_class', ClassType ),
    ( 'colorspace', ColorspaceType ),
    ( 'matte', MagickBooleanType ),
    ( 'fuzz', c_double ),
    ( 'depth', c_ulong ),
    ( 'red', MagickRealType ),
    ( 'green', MagickRealType ),
    ( 'blue', MagickRealType ),
    ( 'opacity', MagickRealType ),
    ( 'index', MagickRealType ),
]
MagickPixelPacket = _MagickPixelPacket
#------------------------------------------------------------------------------ 
class _ColorInfo( Structure ): pass
_ColorInfo._fields_ = [
    ( 'path', STRING ),
    ( 'name', STRING ),
    ( 'compliance', ComplianceType ),
    ( 'color', MagickPixelPacket ),
    ( 'stealth', MagickBooleanType ),
    ( 'previous', POINTER( _ColorInfo ) ),
    ( 'next', POINTER( _ColorInfo ) ),
    ( 'signature', c_ulong ),
]
ColorInfo = _ColorInfo
#------------------------------------------------------------------------------ 
class _ColorPacket( Structure ): pass
_ColorPacket._pack_ = 4
_ColorPacket._fields_ = [
    ( 'pixel', PixelPacket ),
    ( 'index', IndexPacket ),
    ( 'count', MagickSizeType ),
]
ColorPacket = _ColorPacket
#------------------------------------------------------------------------------
class _ConfigureInfo( Structure ): pass
_ConfigureInfo._fields_ = [
    ( 'path', STRING ),
    ( 'name', STRING ),
    ( 'value', STRING ),
    ( 'stealth', MagickBooleanType ),
    ( 'previous', POINTER( _ConfigureInfo ) ),
    ( 'next', POINTER( _ConfigureInfo ) ),
    ( 'signature', c_ulong ),
]
ConfigureInfo = _ConfigureInfo
#------------------------------------------------------------------------------ 
class _ChannelStatistics( Structure ): pass
_ChannelStatistics._pack_ = 4
_ChannelStatistics._fields_ = [
    ( 'depth', c_ulong ),
    ( 'minima', c_double ),
    ( 'maxima', c_double ),
    ( 'mean', c_double ),
    ( 'standard_deviation', c_double ),
]
ChannelStatistics = _ChannelStatistics
#------------------------------------------------------------------------------ 
class _TypeInfo( Structure ): pass
_TypeInfo._fields_ = [
    ( 'face', c_ulong ),
    ( 'path', STRING ),
    ( 'name', STRING ),
    ( 'description', STRING ),
    ( 'family', STRING ),
    ( 'style', StyleType ),
    ( 'stretch', StretchType ),
    ( 'weight', c_ulong ),
    ( 'encoding', STRING ),
    ( 'foundry', STRING ),
    ( 'format', STRING ),
    ( 'metrics', STRING ),
    ( 'glyphs', STRING ),
    ( 'stealth', MagickBooleanType ),
    ( 'previous', POINTER( _TypeInfo ) ),
    ( 'next', POINTER( _TypeInfo ) ),
    ( 'signature', c_ulong ),
]
TypeInfo = _TypeInfo
#------------------------------------------------------------------------------ 
class _XMLTreeInfo( Structure ): pass
_XMLTreeInfo._fields_ = []
XMLTreeInfo = _XMLTreeInfo
#------------------------------------------------------------------------------ 
class _XImportInfo( Structure ): pass
_XImportInfo._fields_ = [
    ( 'frame', MagickBooleanType ),
    ( 'borders', MagickBooleanType ),
    ( 'screen', MagickBooleanType ),
    ( 'descend', MagickBooleanType ),
    ( 'silent', MagickBooleanType ),
]
XImportInfo = _XImportInfo
#------------------------------------------------------------------------------ 
class _StopInfo( Structure ): pass
_StopInfo._pack_ = 4
_StopInfo._fields_ = [
    ( 'color', MagickPixelPacket ),
    ( 'offset', MagickRealType ),
]
StopInfo = _StopInfo
class _SegmentInfo( Structure ): pass
_SegmentInfo._pack_ = 4
_SegmentInfo._fields_ = [
    ( 'x1', c_double ),
    ( 'y1', c_double ),
    ( 'x2', c_double ),
    ( 'y2', c_double ),
]
SegmentInfo = _SegmentInfo
class _GradientInfo( Structure ): pass
_GradientInfo._fields_ = [
    ( 'type', GradientType ),
    ( 'bounding_box', RectangleInfo ),
    ( 'gradient_vector', SegmentInfo ),
    ( 'stops', POINTER( StopInfo ) ),
    ( 'number_stops', c_ulong ),
    ( 'spread', SpreadMethod ),
    ( 'debug', MagickBooleanType ),
    ( 'signature', c_ulong ),
]
GradientInfo = _GradientInfo
#------------------------------------------------------------------------------
class _AffineMatrix( Structure ): pass
AffineMatrix = _AffineMatrix
_AffineMatrix._pack_ = 4
_AffineMatrix._fields_ = [
    ( 'sx', c_double ),
    ( 'rx', c_double ),
    ( 'ry', c_double ),
    ( 'sy', c_double ),
    ( 'tx', c_double ),
    ( 'ty', c_double ),
]
#------------------------------------------------------------------------------ 
class _ElementReference( Structure ): pass
ElementReference = _ElementReference
_ElementReference._fields_ = [
    ( 'id', STRING ),
    ( 'type', ReferenceType ),
    ( 'gradient', GradientInfo ),
    ( 'signature', c_ulong ),
    ( 'previous', POINTER( _ElementReference ) ),
    ( 'next', POINTER( _ElementReference ) )
]
#------------------------------------------------------------------------------ 
class _DrawInfo( Structure ): pass
DrawInfo = _DrawInfo
_DrawInfo._pack_ = 4
_DrawInfo._fields_ = [
    ( 'primitive', STRING ),
    ( 'geometry', STRING ),
    ( 'viewbox', RectangleInfo ),
    ( 'affine', AffineMatrix ),
    ( 'gravity', GravityType ),
    ( 'fill', PixelPacket ),
    ( 'stroke', PixelPacket ),
    ( 'stroke_width', c_double ),
    ( 'gradient', GradientInfo ),
    ( 'fill_pattern', POINTER( Image ) ),
    ( 'tile', POINTER( Image ) ),
    ( 'stroke_pattern', POINTER( Image ) ),
    ( 'stroke_antialias', MagickBooleanType ),
    ( 'text_antialias', MagickBooleanType ),
    ( 'fill_rule', FillRule ),
    ( 'linecap', LineCap ),
    ( 'linejoin', LineJoin ),
    ( 'miterlimit', c_ulong ),
    ( 'dash_offset', c_double ),
    ( 'decorate', DecorationType ),
    ( 'compose', CompositeOperator ),
    ( 'text', STRING ),
    ( 'face', c_ulong ),
    ( 'font', STRING ),
    ( 'metrics', STRING ),
    ( 'family', STRING ),
    ( 'style', StyleType ),
    ( 'stretch', StretchType ),
    ( 'weight', c_ulong ),
    ( 'encoding', STRING ),
    ( 'pointsize', c_double ),
    ( 'density', STRING ),
    ( 'align', AlignType ),
    ( 'undercolor', PixelPacket ),
    ( 'border_color', PixelPacket ),
    ( 'server_name', STRING ),
    ( 'dash_pattern', POINTER( c_double ) ),
    ( 'clip_mask', STRING ),
    ( 'bounds', SegmentInfo ),
    ( 'clip_units', ClipPathUnits ),
    ( 'opacity', Quantum ),
    ( 'render', MagickBooleanType ),
    ( 'element_reference', ElementReference ),
    ( 'debug', MagickBooleanType ),
    ( 'signature', c_ulong ),
]
#------------------------------------------------------------------------------ 
class _PointInfo( Structure ): pass
_PointInfo._pack_ = 4
_PointInfo._fields_ = [
    ( 'x', c_double ),
    ( 'y', c_double ),
]
PointInfo = _PointInfo
#------------------------------------------------------------------------------ 
class _PrimitiveInfo( Structure ): pass
_PrimitiveInfo._fields_ = [
    ( 'point', PointInfo ),
    ( 'coordinates', c_ulong ),
    ( 'primitive', PrimitiveType ),
    ( 'method', PaintMethod ),
    ( 'text', STRING ),
]
PrimitiveInfo = _PrimitiveInfo
#------------------------------------------------------------------------------ 
class _TypeMetric( Structure ): pass
TypeMetric = _TypeMetric
_TypeMetric._pack_ = 4
_TypeMetric._fields_ = [
    ( 'pixels_per_em', PointInfo ),
    ( 'ascent', c_double ),
    ( 'descent', c_double ),
    ( 'width', c_double ),
    ( 'height', c_double ),
    ( 'max_advance', c_double ),
    ( 'underline_position', c_double ),
    ( 'underline_thickness', c_double ),
    ( 'bounds', SegmentInfo ),
    ( 'origin', PointInfo ),
]
#------------------------------------------------------------------------------ 
DrawContext = POINTER( _DrawingWand )
MonitorHandler = CFUNCTYPE( MagickBooleanType, STRING, MagickOffsetType, MagickSizeType, POINTER( ExceptionInfo ) )
ErrorHandler = CFUNCTYPE( None, ExceptionType, STRING, STRING )
FatalErrorHandler = CFUNCTYPE( None, ExceptionType, STRING, STRING )
WarningHandler = CFUNCTYPE( None, ExceptionType, STRING, STRING )
DecodeImageHandler = CFUNCTYPE( POINTER( Image ), POINTER( ImageInfo ), POINTER( ExceptionInfo ) )
EncodeImageHandler = CFUNCTYPE( MagickBooleanType, POINTER( ImageInfo ), POINTER( Image ) )
IsImageFormatHandler = CFUNCTYPE( MagickBooleanType, POINTER( c_ubyte ), size_t )
ImageFilterHandler = CFUNCTYPE( c_ulong, POINTER( POINTER( Image ) ), c_int, POINTER( STRING ), POINTER( ExceptionInfo ) )

#------------------------------------------------------------------------------ 
class _MagickInfo( Structure ): pass
_MagickInfo._fields_ = [
    ( 'name', STRING ),
    ( 'description', STRING ),
    ( 'version', STRING ),
    ( 'note', STRING ),
    ( 'module', STRING ),
    ( 'image_info', POINTER( ImageInfo ) ),
    ( 'decoder', POINTER( DecodeImageHandler ) ),
    ( 'encoder', POINTER( EncodeImageHandler ) ),
    ( 'magick', POINTER( IsImageFormatHandler ) ),
    ( 'client_data', c_void_p ),
    ( 'adjoin', MagickBooleanType ),
    ( 'raw', MagickBooleanType ),
    ( 'endian_support', MagickBooleanType ),
    ( 'blob_support', MagickBooleanType ),
    ( 'seekable_stream', MagickBooleanType ),
    ( 'thread_support', MagickStatusType ),
    ( 'stealth', MagickBooleanType ),
    ( 'previous', POINTER( _MagickInfo ) ),
    ( 'next', POINTER( _MagickInfo ) ),
    ( 'signature', c_ulong ),
]
MagickInfo = _MagickInfo
