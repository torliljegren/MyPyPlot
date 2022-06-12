from MyPyPlot import *
import numpy

# defines a function. This one is f(x) = 1/sqrt(x)
def f(x):
    return 1/sqrt(x)

# defines another function. This one is g(x) = exp(x)
def g(x):
    return 0.5*((x-3)**2)+1


# plots the function f on the domain and auto range
plotf(f, (0.01, 5))

# plots the functon g on the domain [-1, 5] and range [-2, 5]
plotf(g, domain=(0.01, 5), range=(-2, 5))

# puts a label in the plot at the point (0.5, 0) with the text (in Latex math style) 'x = 0.5'
label(x=0.5, y=0, text=' $x=0.5$', yoffset=0)

# put a label on the x-axis (y defaults to 0) with the text above the axis
label(x=2, text=' $x=2$', align='upper')

# plots the integral (area) of the function f from x=3 to x=4
integral1(f, (3, 4))

# plots the integral (area) between the two functions f and g from x=3 to x=4
integral2(f, g, (0.6, 1.5))

# draws a red dotted vertical line from the x-axis att x=1.7 to the graph of f
vlinef(f, 1.7, 'red', '.')

# marks a point on the x-axis at x=1.7 with the text 'C' (in Latex math style) below the axis
point(x=1.7, text=' $C$', text_location='lower')

# puts a label (in Latex math style) above the function f at x=0.25
labelf(f, 0.03, align='upper', text=r'$f(x)=\dfrac{1}{\sqrt{x}}$')

# puts a label (in Latex math style) below the function g at x=2
labelf(g, 2, align='upper', text=r'$g(x)=0.5(x-3)^{2}$')

tangent(g, 4, color='green')

# removes the ticks on the axes
xticks(None)
yticks(None)

# tells the program to render the plot
done()