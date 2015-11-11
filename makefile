quae.pdf: quae.tex
	pdflatex quae.tex

quae.tex: gen.py
	python gen.py > quae.tex

open:
	xdg-open quae.pdf

clean:
	rm quae.aux quae.log
