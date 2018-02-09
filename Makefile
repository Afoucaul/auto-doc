output.tex: template.tex
	python3 generate.py template.tex tmp.tex
	pdflatex --jobname=output tmp.tex 
	rm tmp.tex output.log output.aux
