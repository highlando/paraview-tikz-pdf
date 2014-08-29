import os

tikxdict = {'colorbar.tikz': dict(fh='5cm', fw='2cm'),
            'domainaxis.tikz': dict(fh='5cm', fw='5cm')}
defstex = 'def'  # add a .tex file with definitions or modify def.tex

preamblestr = (
    '\\documentclass[tikz]{standalone}' +
    '\n%\usetikzlibrary{ tikz package already loaded by "tikz" option' +
    '\n\\usepackage{pgfplots}' +
    '\n\\pgfplotsset{compat=newest}' +
    '\n\\pgfplotsset{plot coordinates/math parser=false}' +
    '\n\\begin{document}' +
    '\n\\input{' + defstex + '}' +
    '\n\\newlength\\figureheight' +
    '\n\\newlength\\figurewidth'
    )

for figname, figinfo in tikxdict.items():
    curstring = (
        '\n\\setlength\\figureheight{{{0}}}'.format(figinfo['fh']) +
        '\n\\setlength\\figurewidth{{{0}}}'.format(figinfo['fw']) +
        '\n\\pgfplotsset{footnotesize}' +
        '\n{{\\input{{{0}}}}}'.format(figname) +
        '\n\\end{document}'
        )
    tmptexfile = open('exptikz.tex', 'w')
    tmptexfile.write(preamblestr + curstring)
    tmptexfile.close()

    # os.system("cp " + tikxlist[indx] + " pgfpictoexp.tex")
    os.system("pdflatex -interaction=nonstopmode exptikz.tex")
    os.system("mv exptikz.pdf " + figname + '.pdf')
