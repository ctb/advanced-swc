all:

day3:
	python combine.py c++-wrapping.txt multiprocessing.txt useful-packages.txt new-style-classes.txt gui-gossip.txt python-30.txt > day3.txt
	rst2html.py day3.txt day3.html

day2:
	python combine.py idiomatic-python-2.txt increasing-performance.txt tools.txt pyparsing-presentation.txt online-resources.txt > day2.txt
	rst2html.py day2.txt day2.html

day1:
	python combine.py idiomatic-python.txt structuring-python.txt testing-python.txt nose-intro.txt > day1.txt
	rst2html.py day1.txt day1.html

%.html : %.txt
	@./run-doctests.py $<
	@rst2html.py $< $@
