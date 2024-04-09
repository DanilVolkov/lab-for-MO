import numpy as np


class NelderMead:
    def solve(self, f, n, alpha=1, beta=0.5, gamma=2):
        simplex = np.eye(n + 1, n)

        for i in range(1000):
            # Подготовка
            f_value = [f(x) for x in simplex]
            best, pre_best, worst = 0, 1, 0

            # Сортировка
            f_best = f(simplex[best])
            f_pre_best = f(simplex[pre_best])
            f_worst = f(simplex[worst])
            if f_pre_best > f_best:
                f_pre_best, f_best = f_best, f_pre_best
                pre_best, best = best, pre_best

            for i in range(2, len(simplex)):
                if f(simplex[i]) >= f_best:
                    f_pre_best = f_best
                    pre_best = best
                    f_best = f(simplex[i])
                    best = i
                elif f(simplex[i]) > f_pre_best:
                    f_pre_best = f(simplex[i])
                    pre_best = i

            for i in range(len(simplex)):
                if f(simplex[i]) < f_worst:
                    f_worst = f(simplex[i])
                    worst = i

            # Центр тяжести

            center_of_grav = (sum(simplex) - simplex[best]) / n

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
                f_xr, f_value[h] = f_value[h], f_xr
                fl_6 = True
            elif f_xh < f_xr:
                fl_6 = True

            if fl_6:
                xs = beta * x0[h] + (1 - beta) * xc
                f_xs = f(xs)
                if f_xs < f_xh:
                    x0[h] = xs
                    f_value[h] = f_xs
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
