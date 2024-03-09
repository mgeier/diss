@default_files = ('geier_dissertation_2024');

#$pdf_mode = 1;  # $pdflatex
#$pdf_mode = 3;  # $dvipdf
$pdf_mode = 4;  # $lualatex
#$pdf_mode = 5;  # $xelatex

$bibtex_use = 2;  # run always, delete .bbl files on cleanup

$dvipdf = "dvipdfmx %O -o %D %S";

# Add current directory (and subdirs) to LaTeX path:
ensure_path('TEXINPUTS', './/');

# syntax highlighting of code blocks:
system("./pygmentize.py");

$clean_ext = "run.xml";
