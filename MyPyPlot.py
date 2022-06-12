# encoding: UTF-8

"""
A small library of functions that helps the casual user to plot mathematical functions.
Its intended use is to create graphs suitable for tests and assignements in math.
"""

import numpy
import numpy as np
from numpy import *
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

############################################
# PRIVATE STUFF, NOT INTENDED FOR END USER #
############################################

fig, ax = plt.subplots()
xbounds = [0, 0]
ybounds = [0 ,0]
xlabel = '$x$'
ylabel = '$y$'

# fix standard arrows
rc = {"xtick.direction": "inout", "ytick.direction": "inout",
      "xtick.major.size": 5, "ytick.major.size": 5, }
with plt.rc_context(rc):
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # make arrows
    ax.plot((1), (0), ls="", marker=">", ms=10, color="k",
            transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot((0), (1), ls="", marker="^", ms=10, color="k",
            transform=ax.get_xaxis_transform(), clip_on=False)


###########################################
# PUBLIC FUNCTIONS, INTENDED FOR END USER #
###########################################

def plotf(fun, domain, range=None, color='k', points=200):
    """
    Plots a given function.
    :param fun: the function to be plotted
    :param domain: the domain of the function, i.e. the interval of the x-axis that will be shown
    :param range: the range of the function, i.e. the interval of the y-axis that will be shown. If left out it will be
    on auto
    :param color: the color of the graph, f.i. 'red'. Defaults to black.
    :param points: the number of points on the graph. Defaults to 200, which is sufficient in most cases
    :return: None
    """
    global ax
    global ybounds
    global xbounds
    t = linspace(domain[0], domain[1], points)
    y = fun(t)

    # save new range and domain if the new one is larger
    if range is not None:
        if range[0] < ybounds[0]:
            ybounds[0] = range[0]
        if range[1] > ybounds[1]:
            ybounds[1] = range[1]
    else:
        ybounds[0] = numpy.min(y)
        ybounds[1] = numpy.max(y)

    if domain[0] < xbounds[0]:
        xbounds[0] = domain[0]
    if domain[1] > xbounds[1]:
        xbounds[1] = domain[1]


    ax.plot(t, y, color=color)


def point(x = 0, y = 0, text: str = None, text_location='lower', marker='o', yoffset=0, xoffset=0):
    """
    Plots a point on the coordinate system with optional text.
    :param x: x-coordinate of the point
    :param y: y-coordinate of the point
    :param text: a string of text to accompany the point
    :param text_location: 'upper' to print above the point or 'lower' to print below the point
    :param marker: the glyph symbolizing the point. Can be None, '.' (dot) or 'o' (small filled circle)
    :param yoffset: negative values moves the text down, positive upwards
    :param xoffset: negative values moves the text to the left, positive to the right
    :return: None
    """
    global ax
    global xbounds
    global ybounds
    if text is not None:
        ax.annotate(text,
                    xycoords='data',
                    xy=(x, y),
                    textcoords='offset points',
                    xytext=(-6+xoffset if text_location == 'lower' else 0+xoffset,
                            -15+yoffset if text_location == 'lower' else 2+yoffset))
    if x < xbounds[0]:
        xbounds[0] = x
    elif x > xbounds[1]:
        xbounds[1] = x

    if y < ybounds[0]:
        ybounds[0] = y
    elif y > ybounds[1]:
        ybounds[1] = y

    if marker is not None:
        ax.plot([x], [y], marker)


def pointf(fun, x, text: str = None, text_location='lower', marker='o', yoffset=0, xoffset=0):
    """
    Plot a point on a function graph
    :param fun: the function where the point goes
    :param x: the x-coordinate of the point
    :param text: a string of text to accompany the point
    :param text_location: 'upper' to print above the point or 'lower' to print below the point
    :param marker: the glyph symbolizing the point. Can be None, '.' (dot) or 'o' (small filled circle)
    :param yoffset: fine tune the position of the text. Negative values moves the text down, positive upwards
    :param xoffset: fine tune the position of the text. negative values moves the text to the left, positive to the right
    :return: None
    """
    global ax
    y = fun(x)
    if text is not None:
        ax.annotate(text,
                    xycoords='data',
                    xy=(x, y),
                    textcoords='offset points',
                    xytext=(0+xoffset if text_location == 'lower' else 5+xoffset,
                            -15+yoffset if text_location == 'lower' else 10+yoffset))

    if x < xbounds[0]:
        xbounds[0] = x
    elif x > xbounds[1]:
        xbounds[1] = x

    if y < ybounds[0]:
        ybounds[0] = y
    elif y > ybounds[1]:
        ybounds[1] = y

    if marker is not None:
        ax.plot([x], [y], marker)


def label(x=0, y=0, text='', align='upper', yoffset=0, xoffset=0):
    """
    Puts a label in the coordinate system
    :param x: the x-coordinate of the label
    :param y: the y-coordinate of the label
    :param text: the text of the label
    :param align: 'upper' for text slightly above the point (x, y), 'lower' for slightly below
    :param yoffset: fine tune the position of the text. negative values moves the text down, positive upwards
    :param xoffset: fine tune the position of the text. negative values moves the text to the left, positive right
    :return: None
    """
    point(x, y, text, align, None, yoffset, xoffset)


def labelf(fun, x, text, align='upper', yoffset=0, xoffset=0):
    """
    Puts a label next to a function graph
    :param fun: the function to be labeled
    :param x: the x-coordinate of the label
    :param text: the text on the label
    :param align:  'upper' for text above the graph, 'lower' for below
    :param yoffset: fine tune the position of the text. negative values moves the text down, positive upwards
    :param xoffset: fine tune the position of the text. negative values moves the text to the left, positive right
    :return: None
    """
    pointf(fun, x, text, align, None, yoffset, xoffset)


def tangent(fun, x, h=0.0001, color='k'):
    """
    Draws a tangent to the function at a specified x
    :param fun: the function that gets the tangent
    :param x: the x-coordinate where the tangents brushes the function
    :param h: the difference used to approximate the derivative
    :param color: the color of the tangent, f.i. 'green' or 'red'. Defaults to black
    :return: k: the slope of the tangent, m: the intercept of the tangent
    """
    global ax
    global xbounds
    k = (fun(x+h) - fun(x-h))/(2*h)
    m = fun(x) - k*x
    t = (xbounds[0], xbounds[1])
    l = (k*t[0]+m, k*t[1]+m)
    ax.plot(t, l, color=color)
    return (k, m)


def integral1(fun, xrange):
    """
    Draws the area as a shaded region between the function fun and the x-axis on the interval xrange=(x1, x2)
    :param fun: the function to integrate
    :param xrange: tuple of two numbers (x1, x2) determining the start and stop of the integral
    :return: None
    """
    # Make the shaded region
    ix = np.linspace(xrange[0], xrange[1])
    iy = fun(ix)
    verts = [(xrange[0], 0), *zip(ix, iy), (xrange[1], 0)]
    poly = Polygon(verts, facecolor='0.8', edgecolor='0.5')
    ax.add_patch(poly)


def integral2(fun1, fun2, xrange):
    """
    Draws the area as a shaded region between the functions fun1 and fun2 on the interval xrange=(x1, x2)
    :param fun1: the first function
    :param fun2: the second function
    :param xrange: tuple of two numbers (x1, x2) determining the start and stop of the integral
    :return: None
    """
    ix = np.linspace(xrange[0], xrange[1])
    iy1 = fun1(ix)
    iy2 = fun2(ix)
    plt.fill_between(ix, iy1, iy2, facecolor='0.8', edgecolor='0.5')


def xtext(text):
    """
    Labels the x-axis with the string text
    :param text: a string with the text
    :return: None
    """
    global xlabel
    xlabel = text


def ytext(text):
    """
    Labels the y-axis with the string text
    :param text: a string with the text
    :return: None
    """
    global ylabel
    ylabel = text


def xticks(t):
    """
    Sets the spacing between the ticks on the x-axis.
    :param t: the spacing between the ticks. If None, no ticks will be drawn.
    :return: None
    """
    if t is None:
        plt.xticks([])
    else:
        plt.xticks(np.arange(start=amin(xbounds[0]), stop=amax(xbounds[1]), step=t))


def yticks(t):
    """
    Sets the spacing between the ticks on the y-axis.
    :param t: the spacing between the ticks. If None, no ticks will be drawn.
    :return: None
    """
    if t is None:
        plt.yticks([])
    else:
        plt.yticks(np.arange(start=amin(ybounds[0]), stop=amax(ybounds[1]), step=t))


def hidetickslabels(x=True, y=True):
    """
    Hides the labels on the ticks, i.e. only vertical lines and no numbers on the ticks
    :param x: True hides the labels on the x-axis, False displays them
    :param y: True hides the labels on the y-axis, False displays them
    :return:
    """
    if x:
        plt.xticks(color='w')
    else:
        plt.xticks(color='k')

    if y:
        plt.yticks(color='w')
    else:
        plt.yticks(color='k')


def vline(x, ymin=None, ymax=None, color=None, style=None):
    """
    Draws a vertical line at a given x-coordinate
    :param x:
    :param ymin:
    :param ymax:
    :param color:
    :param style:
    :return:
    """
    global ax
    global xbounds
    styles = {'-':'solid', '.':'dotted', '--':'dashed', '..':'dotted', ':':'dotted'}
    if style is None:
        style = '-'
    if ymin is None:
        ymin = ybounds[0]
    if ymax is None:
        ymax = ybounds[1]

    if x < xbounds[0]:
        xbounds[0] = x
    elif x > xbounds[1]:
        xbounds[1] = x


    ax.plot((x, x),(ymin, ymax), color=color, linestyle=styles[style])


def vlinef(fun,x, color=None, style=None):
    global ax
    styles = {'-':'solid', '.':'dotted', '--':'dashed', '..':'dotted', ':':'dotted'}
    if style is None:
        style = '-'

    ax.plot((x, x),(0, fun(x)), color=color, linestyle=styles[style])



def done():
    global xbounds
    global ybounds
    global ax
    global xlabel
    global ylabel

    if ybounds != [0, 0]:
        plt.ylim(ybounds[0], ybounds[1])

    plt.xlabel(xlabel, loc='right')
    plt.ylabel(ylabel, loc=('top'), rotation=0)

    yax_relpos = abs(xbounds[0])/(xbounds[1]-xbounds[0])
    # print('xbounds =', xbounds)
    # print('yax_relpos =', yax_relpos)
    xoffset = 0.07 if len(ylabel.strip('$'))==1 else 0.015*(len(ylabel.strip('$')))
    xtra_x_offset = 0.015 if xbounds[0] == 0 else 0
    yoffset = 0 if len(ylabel.strip('$'))==1 else 0.05
    ax.yaxis.set_label_coords(yax_relpos+xoffset+xtra_x_offset, 1.0+yoffset)
    plt.show()

if __name__ == '__main__':
    def f(x):
        return x*log(x)-x
    def g(x):
        return (x+10)/(x-4)
    # plot(f, (-5,10))
    plotf(g, (-10, 3.99), (-10, 10))
    plotf(g, (4.01, 10), (-10,10))
    plotf(f, (0.01, 10), (-10, 10))
    #tangent(g, 7.5)
    #tangent(g, 2)
    #integral(g, (0,2.5))
    #xtext('tid')
    #ytext('elförbrukning')
    point(x=12, text='c', text_location='lower')
    pointf(g, 10, '$P$', 'upper')
    #vlinef(g, 15, 'red', '..')
    #vline(4, style='--')
    integral2(f, g, (0.01, 2))
    yticks(2)
    done()