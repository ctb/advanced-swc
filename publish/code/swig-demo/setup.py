from distutils.core import setup, Extension

# the c++ extension module (needs to be linked in with libmotility...)
extension_mod = Extension("_swigdemo",
                          ["_swigdemo_module.cc", "swigdemo.cc"])

setup(name = "swigdemo", version="blah", ext_modules=[extension_mod])
