from distutils.core import setup
from distutils.extension import Extension
from Pyrex.Distutils import build_ext

setup(
  name = "primes",
  ext_modules=[ 
    Extension("primes", ["primes.pyx"], libraries = [])
    ],
  cmdclass = {'build_ext': build_ext}
)
