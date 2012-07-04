all: index.html \
	c++-wrapping.html \
	gui-gossip.html \
	idiomatic-python-2.html \
	idiomatic-python.html \
	increasing-performance.html \
	multiprocessing.html \
	new-style-classes.html \
	online-resources.html \
	python-30.html \
	structuring-python.html \
	testing-python.html \
	tools.html \
	useful-packages.html \
	pyparsing-presentation.html \
	nose-intro.html \
	combined.html

%.html : %.txt
	@./run-doctests.py $<
	@rst2html.py $< $@

combined.txt: header.txt idiomatic-python.txt structuring-python.txt \
		testing-python.txt nose-intro.txt idiomatic-python-2.txt \
		increasing-performance.txt tools.txt online-resources.txt \
		c++-wrapping.txt multiprocessing.txt useful-packages.txt \
		new-style-classes.txt gui-gossip.txt python-30.txt
	python combine.py header.txt idiomatic-python.txt structuring-python.txt \
		testing-python.txt nose-intro.txt idiomatic-python-2.txt \
		increasing-performance.txt tools.txt online-resources.txt \
		c++-wrapping.txt multiprocessing.txt useful-packages.txt \
		new-style-classes.txt gui-gossip.txt python-30.txt \
		> combined.txt
