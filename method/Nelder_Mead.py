import numpy as np


class NelderMead:

    def calculate(self, f, n, alpha=1.5, beta=1.5, gamma=1.5):
        x = np.eye(n + 1, n)
        for pepe in range(1000):
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
                xss = xr
                ind_xss = ind_xr
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

    def solve(self, f, n, s_point, alpha=1, beta=0.5, gamma=2):

        x0 = np.eye(n + 1, n)
        if not x0.__contains__(s_point):
            x0[n] = s_point

        for pepe in range(100):
            f0 = [f(x) for x in x0]

            if f0[0] > f0[1]:
                f_xh = f0[0]
                h = 0
                f_xg = f0[1]
                g = 1
            else:
                f_xh = f0[1]
                h = 1
                f_xg = f0[0]
                g = 0

            l = f0.index(min(f0))
            f_xl = f0[l]
            # тут все упадет однажды...
            # h - максимум, g - второй максимум, l - минимум
            for i in range(2, len(f0)):
                if f0[i] > f_xh:
                    f_xh = f0[i]
                    h = i
                elif f0[i] >= f_xg and i != h:
                    f_xg = f0[i]
                    g = i

            xc = np.array((sum(x0[:]) - x0[h]) / n)  # убрать np.array можно

            xr = (1 + alpha) * xc - alpha * x0[h]
            f_xr = f(xr)

            fl_6 = False  # rename this shit

            if f_xr < f_xl:
                xe = (1 - gamma) * xc + gamma * xr
                f_xe = f(xe)
                if f_xe < f_xr:
                    x0[h] = xe
                elif f_xr < f_xe:
                    x0[h] = xr
            elif f_xl < f_xr < f_xg:
                x0[h] = xr
            elif f_xg < f_xr < f_xh:
                xr, x0[h] = x0[h], xr
                f_xr, f0[h] = f0[h], f_xr
                fl_6 = True
            elif f_xh < f_xr:
                fl_6 = True

            if fl_6:
                xs = beta * x0[h] + (1 - beta) * xc
                f_xs = f(xs)
                if f_xs < f_xh:
                    x0[h] = xs
                    f0[h] = f_xs
                elif f_xs > f_xh:
                    xl = x0[l]
                    for i in range(len(x0)):
                        if i != l:
                            x0[i] = xl + (x0[i] - xl)
            disp = np.var(x0)
            print(disp)
            # по осям... disp_self = (sum(x0[:] ** 2) / n) - (sum(x0[:]) / n) ** 2
            # мб бахнуть формулой Герона площади треугольников - граней и смотреть чтобы она была меньше eps

        return x0[n, :]
