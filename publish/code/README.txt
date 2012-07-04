This is the source code for my LLNL course on *Intermediate and Advanced
Software Carpentry in Python*.

Directories
===========

Each directory contains the examples for a specific

hello
-----

A few simple examples of a hand-built C extension module for Python.

To build & run the hello examples: ::

   python setup.py build
   python run.py

ctypes
------

An example showing how to use the ctypes library module to execute
C functions directly from dynamic libraries.

To build the ctypes example: ::

	make
	LD_LIBRARY_CONFIG=. python hello_mod.py

You may need to change the Makefile to put the right magic flags in to
build a shared library on your platform.  Flags for Linux & Mac OS X
are already there.

parallelpython
--------------

A simple example of using the parallelpython package
(http://www.parallelpython.com/).

To run the examples on two CPUs, install parallelpython and run: ::

   cd parallelpython
   python calc_primes.py 2

profiling
---------

Simple examples of using cProfile, hotshot, `statprof
<http://vallista.idyll.org/wiki/StatProf>`__, and timeit to profile
and time the execution of Python code.  See the files run-*.

psyco
-----

Simple example of using psyco, a specializing compiler for Python.

Go into the ``psyco/`` subdirectory and type ::

   python psyco-test.py

pyrex-hello
-----------

A simple example of using `pyrex <http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/>`__ to wrap a C function ("Hello, world").

Execute: ::

   cd pyrex-hello/
   python setup.py build_ext --inplace
   python run.py

pyrex-primes
------------

A simple example of using `pyrex <http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/>`__ to speed up Python.

Execute: ::

   cd pyrex-primes/
   python setup.py build_ext --inplace
   python run-primes.py

rpy
---

Driving `R <http://www.r-project.org/>`__ from Python using `rpy
<http://rpy.sf.net/>`__ to run and display a Principle Components
Analysis.

Execute: ::

   cd rpy/
   python do-pca.py

sip
---

A simple example of using `SIP <http://www.riverbankcomputing.co.uk/sip/>`__
to wrap C code in a Python extension module.

Execute: ::

   cd sip/
   bash ./make-libhello.sh
   python configure.py
   make
   python run.py

swig-demo
---------

A simple example of using SWIG to wrap a C module for Python.

Execute: ::

	 cd swig-demo/
	 make
	 python run.py
