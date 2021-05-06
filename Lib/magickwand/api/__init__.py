from lib import MagickWand

#===============================================================================
# API
#===============================================================================
class API( object ):
    def __init__( self, lib ):
        self.lib = lib
        self.functions = {}
        self.errors = {}

    def register( self, name, restype = None, argtypes = None ):
        try:
            self.functions[name] = self.lib[ name ]
            self.functions[name].restype = restype
            self.functions[name].argtypes = argtypes
            return self.functions[name]
        except AttributeError, ex:
            self.errors[name] = ex


    def register_all( self, list ):
        for ( name, restype, argtypes ) in list:
            self.register( name, restype, argtypes )

    def __getattr__( self, name ):
        if self.functions.has_key( name ): return self.functions[name]
        else:
            if self.errors.has_key( name ):
                raise KeyError( '%s is not a valid symbol in %s' % ( name, self.lib ) )
            else:
                raise KeyError( 'please register the function %s' % name )

api = API( MagickWand )
