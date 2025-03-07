import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 1st order differential eq
def func_dydt(y, t):
    dydt = -y
    return dydt

# 2D visualization
def plot2d(t_list, y_list, t_label, y_label, color, linewidth, label):
    plt.xlabel(t_label)
    plt.ylabel(y_label)
    plt.grid()
    plt.plot(t_list, y_list, color=color, linewidth=linewidth, label=label)

    plt.legend()
    plt.show()

def main():
    t_list = np.linspace(0.0, 10.0, 1000)
    y_init = 1.0
    y_list = odeint(func_dydt, y_init, t_list)

    plot2d(t_list, y_list[:, 0], "$t$", "$y(t)$", "r", 3, "$dydt = -y$")

if __name__ == '__main__':
    main()