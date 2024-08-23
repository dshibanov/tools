import math
import matplotlib.pyplot as plt
import matplotlib.pyplot as mpl
import numpy as np
import pandas as pd
import matplotlib.font_manager


from scipy.optimize import curve_fit

# TODO:
    # maybe I should name it properly,
    # 'SOFT DEADLINE' for example
    # and some another interface
    #
    #

# ALSO
#   I tried to make it automatic but gave up
#   is better to fit curve manually
#   in context how much time it need
#   and how often we do that
#
#   but maybe later we'll need automatic implementation
#   when we'll have more teams.. 
#
#   ok. I froze it and go to fix another issues
#
#
#   One way to make this is construct custom objective
#   where error on nominal should be as minimal as possible
#   and fine for errors in that point should be very high
#   so, I need custom function with adjustable fines for every data point

def new_soft_dd(nominal, premia, fine):

    def paymentf(a, b, c, x):
        return a + b*math.exp(-c*x)

    xdata = [premia[0], nominal[0], fine[0]]
    ydata = [premia[1], nominal[1], fine[1]]

    popt, pcov = curve_fit(paymentf, xdata, ydata, method = 'dogbox')

    print(popt)
    print(pcov)


def soft_deadline(nominal, premia, fine, start, end, degree):
    # this make a plot
    # and print output

    indentsY = (0.05, 0.3)
    # indentsX = (0.2, 0.2)

    bottom_line = nominal[1] * (1 - fine)
    top_line = nominal[1] * (1 + premia)

    print('top_line: ', top_line)
    print('bottom_line: ', bottom_line)

    def paymentf(a, b, c, x):
        return a + b*math.exp(-c*x)

    myFn = np.vectorize(paymentf, excluded=['a', 'b', 'c'])

    x = np.linspace(start, end, 100)
    y = myFn(bottom_line, top_line, degree, x)
    y2 = myFn(bottom_line, top_line, degree*2, x)
    y3 = myFn(bottom_line, top_line, degree*0.52, x)

    fig, ax = plt.subplots()

    # plt.xlim((0,4))
    plt.xlim((start,end))

    plt_up = top_line * (1 + indentsY[1])
    plt_down = bottom_line * (1 - indentsY[0])
    print(plt_down, plt_up)

    plt.ylim((plt_down, plt_up))

    # ax.plot(x, y, label='original', color='k', linewidth=2)
    ax.plot(x, y, color='k', linewidth=2)
    ax.plot(x, y2, color='b', linewidth=2)
    ax.plot(x, y3, color='g', linewidth=2)
    # ax.plot(x, y2, label='new')
    # ax.plot(x, y3, label='new2')
    ax.hlines(y=nominal[1], xmin=start, xmax=2, linewidth=1, linestyles='--', color='k')
    ax.hlines(y=bottom_line, xmin=start, xmax=4, linewidth=1, linestyles='--', color='k')
    ax.hlines(y=top_line, xmin=start, xmax=1, linewidth=1, linestyles='--', color='k')

    ax.vlines(x=1, ymin=plt_down, ymax=top_line, linewidth=1, linestyles='--', color='k')
    ax.vlines(x=2, ymin=plt_down, ymax=nominal[1], linewidth=1, linestyles='--', color='k')
    ax.vlines(x=3, ymin=plt_down, ymax=bottom_line, linewidth=1, linestyles='--', color='k')
    # ax.vlines(y=3500, xmin=0, xmax=4, linewidth=1, linestyles='--', color='k')
    # ax.vlines(y=5000, xmin=0, xmax=1, linewidth=1, linestyles='--', color='k')
    plt.legend(bbox_to_anchor=(1.04,0.5), loc="center left", borderaxespad=0)

    plt.yticks([bottom_line, nominal[1], top_line])
    plt.xticks([0, 1, 1.5, 2, 2.5, 3, 3.5, 4])

    hfont = {'fontname':'Inconsolata', 'fontsize': 'large'}

    mpl.rcParams['font.size'] = 25
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    plt.title('$(time)', loc='center', **hfont, x=0.5, y = 1.03)
    # from matplotlib import rc
    # rc('text', usetex=True)

    # plt.xlabel('Months', fontweight='bold', **hfont)
    plt.xlabel('Months', **hfont, x = 0.5, y = -1.5)
    plt.ylabel('Payment in USDT', **hfont, x=0, y = 0.5)
    plt.show()


def f(a, b, c, x):
    return a + b*math.exp(-c*x)


def payment_plot_simple():

    myFn = np.vectorize(f, excluded=['a', 'b', 'c'])

    x = np.linspace(0.8, 4, 40)
    y = myFn(3500, 21921.33, 2.67961, x)
    y2 = myFn(3500, 21921.33, 2.67961*2, x)
    y3 = myFn(3500, 21921.33, 2.67961*0.5, x)

    fig, ax = plt.subplots()
    # ax.plot(x, y, label='original', color='k', linewidth=2)
    ax.plot(x, y, color='k', linewidth=2)
    ax.plot(x, y2, label='new')
    ax.plot(x, y3, label='new2')
    ax.hlines(y=3600, xmin=0, xmax=2, linewidth=1, linestyles='--', color='k')
    ax.hlines(y=3500, xmin=0, xmax=4, linewidth=1, linestyles='--', color='k')
    ax.hlines(y=5000, xmin=0, xmax=1, linewidth=1, linestyles='--', color='k')

    ax.vlines(x=1, ymin=3200, ymax=5000, linewidth=1, linestyles='--', color='k')
    ax.vlines(x=2, ymin=3200, ymax=3600, linewidth=1, linestyles='--', color='k')
    ax.vlines(x=3, ymin=3200, ymax=3500, linewidth=1, linestyles='--', color='k')
    # ax.vlines(y=3500, xmin=0, xmax=4, linewidth=1, linestyles='--', color='k')
    # ax.vlines(y=5000, xmin=0, xmax=1, linewidth=1, linestyles='--', color='k')
    plt.legend(bbox_to_anchor=(1.04,0.5), loc="center left", borderaxespad=0)

    plt.xlim((0,4))
    plt.ylim((3200,6000))
    plt.yticks([3500, 3600, 5000])
    plt.xticks([0, 1, 1.5, 2, 2.5, 3, 3.5, 4])

    hfont = {'fontname':'Inconsolata', 'fontsize': 'large'}

    mpl.rcParams['font.size'] = 25
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    plt.title('$(time)', loc='center', **hfont, x=0.5, y = 1.03)
    # from matplotlib import rc
    # rc('text', usetex=True)

    # plt.xlabel('Months', fontweight='bold', **hfont)
    plt.xlabel('Months', **hfont, x = 0.5, y = -1.5)
    plt.ylabel('Payment in USDT', **hfont, x=0, y = 0.5)
    plt.show()

    fonts = matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
    fs = matplotlib.font_manager.get_font_names()
    payment = pd.DataFrame(list(zip(x,y)), columns = ['x', 'y'])
    # print(payment)



if __name__ == "__main__":
    print('heyahaa')
    # payment_plot_simple()
    #
    # да тут вот нужно чтобы сохранялось условие что 
    # при значении х == 2, y == 3600 
    # как такого добиться?
    # нужно наверное заново аппроксимацию делать
    #
    # 
    # soft_deadline((2,3600), 0.3, 0.1, 0, 4, 3)

    new_soft_dd((2,3600), (1, 7200), (3, 3500))

