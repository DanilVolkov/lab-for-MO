import numpy as np


class NelderMead:

    def calculate(self, f, n, alpha=1.5, beta=1.5, gamma=1.5):
        x = np.eye(n + 1, n)
        while True:
            fun = [f(x0) for x0 in x]
            fun_xr = min(fun)
            xr, ind_xr = x[fun.index(fun_xr)], fun.index(fun_xr)
            fun_xs = max(fun)
            xs, ind_xs = x[fun.index(fun_xs)], fun.index(fun_xs)
            x_mid = (sum(x) - xs) / n
            x_sim = x_mid + alpha * (x_mid - xs)
            fun_x_sim = f(x_sim)
            if fun_xr > fun_x_sim:
                x1 = x_mid + gamma * (x_sim - x_mid)
                fun_x1 = f(x1)
                if fun_x_sim > fun_x1:
                    x[ind_xs] = x1
                else:
                    x[ind_xs] = x_sim
            else:
                fun_xss = fun_xr
                for i in range(n + 1):
                    if i != ind_xs and fun_xss < fun[i]:
                        fun_xss = fun[i]
                        xss = x[i]
                        ind_xss = i
                if fun_xss >= fun_x_sim:
                    x[ind_xs] = x_sim
                if fun_x_sim < fun_xs:
                    fun_xl = fun_x_sim
                    xl = xs
                else:
                    fun_xl = fun_xs
                    xl = x_sim
                xll = x_mid + beta * (xl - x_mid)
                fun_xll = f(xll)
                if fun_xll > fun_xl:
                    x = x + 0.5 * (xr - x)
                else:
                    x[ind_xs] = xll
        return x
    