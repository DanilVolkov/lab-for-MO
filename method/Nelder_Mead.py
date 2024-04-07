import numpy as np


class NelderMead:

    def solve(self, f, n, alpha=1, beta=0.5, gamma=2):

        x0 = np.eye(n + 1, n)

        f0 = [f(x) for x in x0]

        for pepe in range(1000):
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

            xc = np.array((sum(x0[:]) - x0[h]) / n)

            xr = (1 + alpha) * xc - alpha * x0[h]
            f_xr = f(xr)

            fl_6 = False  # rename this shit

            if f_xr < f_xl:
                xe = (1 - gamma) * xc + gamma * xr
                f_xe = f(xe)
                if f_xe < f_xr:
                    x0[h] = xe
                    f0[h] = f_xe  # )))
                    f_xh = f_xe  # )))
                elif f_xr < f_xe:
                    x0[h] = xr
                    f0[h] = f_xr  # )))
                    f_xh = f_xr  # )))
            elif f_xl < f_xr < f_xg:
                x0[h] = xr
                f0[h] = f_xr  # )))
                f_xh = f_xr  # )))
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

        return x0[n, :]
