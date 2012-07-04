cd ctypes/ && (make && LD_LIBRARY_PATH=. python hello_mod.py) || echo ERROR
cd ../

cd hello/ && python setup.py build_ext --inplace || echo ERROR
cd ../

cd parallelpython && python calc_primes.py 2 || echo ERROR
cd ../

cd profiling && (python run-cprofile && python run-hotshot && \
    python run-statprof && python run-timeit) || echo ERROR
cd ../

cd psyco && python psyco-test.py 1 || echo ERROR
cd ../

cd pyrex-hello/ && (python setup.py build_ext --inplace && python run.py) \
    || echo ERROR
cd ../

cd pyrex-primes/ && (python setup.py build_ext --inplace && \
    python run-primes.py) || echo ERROR
cd ../

cd rpy/ && python do-pca.py || echo ERROR
cd ../

cd sip/ && (bash make-libhello.sh && python configure.py) || echo ERROR
cd ../

cd swig-demo/ && make && python run.py || echo ERROR
cd ../

cd pyrex-primes/ && (python setup.py build_ext --inplace && \
    python run-primes.py) || echo ERROR
cd ../

cd sip/ && (bash ./make-libhello.sh && python configure.py && make) \
    || echo ERROR
cd ../

cd swig-demo/ && (make && python run.py) || echo ERROR
cd ../
