from collections import deque


def digit_sum(digit):
    """
    считтает сумму цифр в числе
    :param digit: int
    :return: int
    """
    return sum(map(int, str(abs(digit))))


def right_sum(digit1, digit2):
    """
    Проверяем что сумма цифр в числе не превышает 25
    :param digit1: int
    :param digit2: int
    :return: bool
    """
    return digit_sum(digit1) + digit_sum(digit2) <= 25


def ant_path(x, y):
    """
    Считает количество точек, где был муравей
    :param x: int
    :param y: int
    :return: int
    """
    path = set()  # где были
    queue = deque([(x, y)])  # откуда еще не ходили, двойная очередь для более быстрой реализации очереди
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))  # варианты куда идти, право, лево, вверх, вниз
    path.add((x, y))  # добавляем первую точку, ибо включительно

    while queue:  # пока есть точки откуда можно ходить
        x, y = queue.popleft()  # удаляем точку из возможных отправных и распаковываем x и y
        for dx, dy in directions:  # проходим по возможным шагам распаковывая их на перемещение x и y
            new_step_x, new_step_y = x + dx, y + dy  # расчет новой точки
            if (new_step_x, new_step_y) not in path and right_sum(new_step_x,
                                                                  new_step_y):  # если мы там не были и точка удовлетворяет условию
                path.add((new_step_x, new_step_y))  # добавляем точку в пройденный путь
                queue.append((new_step_x, new_step_y))  # добавляем точку в точки откуда можно выходить
    path_length = len(path)  # считаем количество возможных точек
    return path_length

print(ant_path(1000, 1000))  # 148848