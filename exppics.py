import os

tikxdict = {'colorbar.tikz': dict(fh='5cm', fw='2cm'),
            'domainaxis.tikz': dict(fh='5cm', fw='5cm')}

outnamelist = ["colorbar.pdf", "domainaxis.pdf"]

preamblestr = (
    '\\documentclass[tikz]{standalone}' +
    '\n%\usetikzlibrary{ tikz package already loaded by "tikz" option' +
    '\n\\usepackage{pgfplots}' +
    '\n\\pgfplotsset{compat=newest}' +
    '\n\\pgfplotsset{plot coordinates/math parser=false}' +
    '\n\\begin{document}' +
    '\n\\newlength\\figureheight' +
    '\n\\newlength\\figurewidth'
    )

for figname, figsize in tikxdict.items():
    curstring = (
        '\n\\setlength\\figureheight{{{0}}}'.format(figsize['fh']) +
        '\n\\setlength\\figurewidth{{{0}}}'.format(figsize['fw']) +
        '\n\\pgfplotsset{footnotesize}' +
        '\n{{\\input{{{0}}}}}'.format(figname) +
        '\n\\end{document}'
        )
    tmptexfile = open('exptikz.tex', 'w')
    tmptexfile.write(preamblestr + curstring)
    tmptexfile.close()

    # os.system("cp " + tikxlist[indx] + " pgfpictoexp.tex")
    os.system("pdflatex -interaction=nonstopmode exptikz.tex")
    os.system("mv exptikz.pdf " + figname+'.pdf')
