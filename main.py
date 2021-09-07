
def move(point, course, lab):
    x, y = point[0], point[1]
    if course == 'r' and (point[0]+1, point[1]) in lab:
        x+=1
    if course == 'l' and (point[0]-1, point[1]) in lab:
        x-=1
    if course == 'u' and (point[0], point[1]+1) in lab:
        y+=1
    if course == 'd' and (point[0], point[1]-1) in lab:
        y-=1
    new_point = [x, y]
    return new_point

def steper(lab, z_point, way):
    if len(way) == 1:
        new_position = move(z_point,way[0], lab)
        return new_position
    else:
        step = way.pop(0)
        new_position = move(z_point, step, lab)
        return steper(lab, new_position, way)

if __name__ == "__main__":
    import argparse
    from maze_templates import *
    from re import findall
    from graph_pic import *
    maze_dict = {
        'a': {'type': a, 'zero_p': zero_point_a, 'finish': finish_a},
        'b': {'type': b, 'zero_p': zero_point_b, 'finish': finish_b},
        'c': {'type': c, 'zero_p': zero_point_c, 'finish': finish_c},
    }

    parser = argparse.ArgumentParser(description='Great Description To Be Here')
    parser.add_argument('-w', '--way', dest='way', default='r,u', type=str,
                        help='Введите шаги, например: l,r,u,d или  lrud')
    parser.add_argument('-m', '--maze', dest='maze', default='a', choices=['a', 'b', 'c'], type=str,
                        help='Выберите тип лабиринта: a, b или c')
    parser.add_argument('-d', '--debug', dest='debug', action='store_true',
                        help='Вывод отладочной информации')
    parser.add_argument('-p', '--pict', dest='pict', action='store_true',
                        help='Вывод отладочно информации')

    args = parser.parse_args()

    way_list = findall('[u]|[r]|[l]|[d]', args.way)
    labyrinth = maze_dict[args.maze]
    zero_point = labyrinth['zero_p']
    finish = labyrinth['finish']

    if args.debug:
        print(f'way_list: {way_list} \nlabyrinth: {labyrinth} \nzero_point: {zero_point}')

    new_p = steper(labyrinth['type'], zero_point, way_list)
    if args.pict:
        create_pict(labyrinth['type'], new_p)
    print(f'Your position {new_p}')

