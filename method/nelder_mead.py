import numpy as np


class NelderMead:
    @staticmethod
    def _symmetrical_point(x1, x2, a):
        return x1 + a * (x2 - x1)

    @staticmethod
    def calculate(function, n_dimension, alpha=1.5, beta=1.5, gamma=1.5):
        # Создаем изначальный симплекс (тетраедр в углу координатной сетки)
        simplex_vertex = np.eye(n_dimension + 1, n_dimension)
        # Цикл, пока все вершины симплекса не станут равны с точностью 10^-5
        while not np.isclose(simplex_vertex, simplex_vertex[0]).all():
            # Пересчет значений функции в вершинах симплекса
            function_value = [function(x0) for x0 in simplex_vertex]
            # Ищем вершину с минимальным значением функции
            function_min_value = min(function_value)
            x_for_min_value = simplex_vertex[function_value.index(function_min_value)]
            # Ищем вершину с максимальным значением функции
            function_max_value = max(function_value)
            ind_x_for_max_value = function_value.index(function_max_value)
            x_for_max_value = simplex_vertex[ind_x_for_max_value]
            # Ищем среднюю точку (исключая вершину, соответствующую максимальному значению функции)
            average_x = (sum(simplex_vertex) - x_for_max_value) / n_dimension
            # Симметрично отражаем вершину, соответсвующую максимальному значению
            symmetrical_x = NelderMead._symmetrical_point(average_x, x_for_max_value, -alpha)
            function_symmetrical_x_value = function(symmetrical_x)
            # Если значение функции в отраженной точке меньше текущего минимума
            if function_min_value > function_symmetrical_x_value:
                # Вспомогательную точку с помощью параметра gamma
                x1 = NelderMead._symmetrical_point(average_x, symmetrical_x, gamma)
                # Если в ней значение меньше,
                # то меняем в симплексе точку максимального значения на вспомогательную
                if function_symmetrical_x_value > function(x1):
                    simplex_vertex[ind_x_for_max_value] = x1
                # Иначе, меняем на симметрично отраженную точку максимального значения
                else:
                    simplex_vertex[ind_x_for_max_value] = symmetrical_x
            else:
                # Ищем второе максимальное значение функции
                function_premax_value = function_min_value
                for i in range(n_dimension + 1):
                    if i != ind_x_for_max_value and function_premax_value < function_value[i]:
                        function_premax_value = function_value[i]
                # Если второй максимум больше значения функции в симметрично отраженной точке,
                # меняем точку максимума на ее отражение
                if function_premax_value >= function_symmetrical_x_value:
                    simplex_vertex[ind_x_for_max_value] = symmetrical_x
                # Если значение в отражении максимума меньше масимума,
                # то вспомогательная точка - это отражение
                if function_symmetrical_x_value < function_max_value:
                    function_x2_value = function_symmetrical_x_value
                    x2 = symmetrical_x
                # Иначе - точка максимума
                else:
                    function_x2_value = function_max_value
                    x2 = x_for_max_value
                # Построим отражение вспомогательной точки с помощью beta, вычислим функцию в нем
                x3 = NelderMead._symmetrical_point(average_x, x2, beta)
                function_x3_value = function(x3)
                # Если это значение больше значения функции во вспомогательной точке,
                # то "ужимаем" весь симплекс
                if function_x3_value > function_x2_value:
                    simplex_vertex = NelderMead._symmetrical_point(simplex_vertex, x_for_min_value, 0.5)
                # Иначе меняем точку максимума на это отражение
                else:
                    simplex_vertex[ind_x_for_max_value] = x3
        return np.round(sum(simplex_vertex) / (n_dimension + 1), 5)
