from distutils.core import setup
from distutils.extension import Extension
from Pyrex.Distutils import build_ext

setup(
  name = "hello",
  ext_modules=[ Extension("hellomodule", ["hellomodule.pyx", "hello.c"]) ],
  cmdclass = {'build_ext': build_ext}
)
