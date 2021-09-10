Описание задачи:
Разработать функционал "навигации по лабиринту": имея карту лабиринта, координаты стартовой точки и маршрут, требуется 
определить координаты конечной точки.
- Лабиринт представляется в виде набора секций на двумерной плоскости.
-- Положение секции определяется двумя целочисленными координатами, например секция (0, 2).
-- Если две секции расположены рядом по горизонтали или вертикали (не по диагонали), то между ними есть проход.
-- Например:
--- набор секций с координатами (0, 0), (0, 1), (1, 0), (1, 1) задает квадратный лабиринт 2x2.
--- набор секций с координатами (-1, 0), (0, 0), (1, 0), (0, 1), (0, -1) задает лабиринт из 5 секций в виде креста
с центром в секции (0, 0).
-- Лабиринт может иметь произвольную форму, состоять из нескольких не связанных между собой частей и т. д.
- Маршрут в лабиринте задается последовательностью шагов.
-- Шагать можно только по 4 направлениям: вверх, вниз, вправо и влево.
-- Если в направлении шага есть переход в соседнюю секцию, то текущее положение меняется на нее.
-- Если в направлении шага перехода в соседнюю секцию нет, то шаг не имеет эффекта и текущее положение не меняется.
-- Например, для лабиринта из двух секций (0, 0) и (1, 0), стартовой точки (0, 0) и маршрута "вправо, вправо, вправо",
только первый шаг будет иметь эффект (0, 0) -> (1, 0). Второй и третий шаг оставят текущее положение без изменений,
поскольку секции (2, 0) не существует, и конечная точка маршрута останется (1, 0).
- Требуется определить положение после последнего шага маршрута.
Требования к реализации:
========================
- Требуется реализовать этот функционал в виде проекта на python, а также снабдить его тестами на pytest
- Выбор деталей реализации (API, обработка ошибок, кол-во и содержание тестов, документация, проч.) остается на ваше 
усмотрение.
- При этом:
-- Представьте, что этот функционал будет доступен другим пользователям, которым потребуется понимать его возможности и
особенности использования, не вникая в реализацию / не читая её, в том числе в ошибочных ситуациях
-- Представьте, что вы работаете над этим проектом совместно с другими разработчиками, и кому-то другому может понадобиться
понять реализацию / внести изменения в имеющийся функционал - возможно, уже без вашего участия. Учитывая это, оформите его
содержимое в соответствии с теми best practiсes, с которыми знакомы и считаете правильными.

запуск производится с помощью командной строки из папки с проектом.
пример:
C:\Users\MONOLIT\PycharmProjects\test_chellenge>python main.py -p
ключи запуска:
-w ввод пути по лабиринту, принимает на вход строку без пробелов, в которой должны содержаться направления u,d,l,r (up, down, left, right).
по умолчанию = 'r,u'
-m выбор типа лабиринта: a,b, или c.
по умолчанию = 'a'
-d вывод отладочной информации - значения переменных.
-p рисует изображение лабиринта в виде ячеек, где синий квадрат - старт, зеленый финиш.