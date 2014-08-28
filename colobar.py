'''
Make a colorbar as a separate figure.
'''
from matplotlib import pyplot, mpl
import numpy as np


def exp_colormap(cmap=None, horizontal=True, titlestr='$|v|$',
                 cmin=0.0, cmax=1.0, figratio=20, exp2tikz=True):
    """
    Parameters:
    -----------
    cmap : `colormap`, optional
        as in the `matplotlib.mpl.cm` module, defaults to `coolwarm`
    cmin : real, optional
        minimal value of the variable described, defaults to 0
    cmax : real, optional
        maximal value of the variable described, defaults to 1
    titlestr : string, optional
        title for the color map
    horizontal : boolean, optional
        whether to return a horizontal colorbar, defaults to `False`
    figratio : real, optional
        ratio of longer edge to shorter edge
    """

    reso = 200
    figs = (figratio, 1)
    dataextend = [cmin, cmax, 0, 0.05*(cmax-cmin)]
    xrg = np.linspace(cmin, cmax, reso)
    yrg = np.array([[1], [1]])
    zrg = yrg*xrg

    if cmap is None:
        cmap = mpl.cm.jet_r
    if horizontal:
        zrg = zrg.T
        figs = (1, figratio)
        dataextend = [0, 0.05*(cmax-cmin), cmin, cmax]

    # Make a figure and axes with dimensions as desired.
    fig = pyplot.figure(figsize=figs)
    ax1 = fig.add_subplot(111, aspect='equal')
    if horizontal:
        ax1.set_xticklabels([])
        ax1.set_xticks([])
    else:
        ax1.set_yticklabels([])
        ax1.set_yticks([])
    ax1.set_title(titlestr)
    pyplot.imshow(zrg, cmap=cmap, extent=dataextend)

    if exp2tikz:
        from matplotlib2tikz import save as tikz_save
        fname = 'colorbar.tikz'
        extraaxiopts = frozenset([
            'scaled x ticks=false,\n' +
            'xtick={,,},\n' +
            'xticklabels={,,},\n' +
            # 'xlabel={$\phantom{x_0}$,\n' +  # for align with domainaxis
            'extra y ticks={\n' +
            '    \\pgfkeysvalueof{/pgfplots/ymin},\n' +
            '    \\pgfkeysvalueof{/pgfplots/ymax}\n' +
            '},\n' +
            'every extra y tick/.style={\n' +
            '    font=\\large,\n' +
            '    tick style=transparent, \n' +
            '    yticklabel pos=right,\n' +
            '    /pgf/number format/.cd,\n' +
            '    fixed,\n' +
            '    precision=3\n' +
            '},'])
        tikz_save(fname,
                  figureheight='\\figureheight',
                  figurewidth='\\figurewidth',
                  extra=extraaxiopts,
                  )
        print 'Plot saved to ' + fname
        print 'You may want to add \n'
        print 'scaled x ticks=false,'
        print 'xtick={,,},'
        print 'xticklabels={,,},'
        # print 'yticklabels={{{0},,{1}}}, \n'.format(cmin, cmax)

    print 'to the axis definition'

    pyplot.show(block=False)

if __name__ == '__main__':
    exp_colormap()
