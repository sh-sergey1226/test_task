"""запуск тестов через pytest
pytest test_file.py"""


from subprocess import Popen, PIPE
from os import chdir
from main import steper

maze1 = ((0,0),(0,1),(3,3))
maze2 = ((0,0),(1,0),(3,3))
maze3 = ((0,0),(0,-1),(3,3))
maze4 = ((0,0),(-1,0),(3,3))
z_point = (0,0)
w_dict = {maze1: 'u', maze2:'r', maze3: 'd', maze4: 'l', 'ways': ['u','u','u','r','r','r']}

way1 = '!@#$%^&*()_+'
way2 = '🔥 💣 💥 🧨 🤔 🔎'
way3 = ' k f w e q v'
way4 = 'u r d l '
way5 = ''


class TestMainPage1():

    @classmethod
    def setup_class(self):
        chdir(r'C:\Users\MONOLIT\PycharmProjects\test_chellenge')

    def test_correct_result(self):
        """выдача корректного результата при задании шага"""
        result = steper(maze1, z_point, w_dict[maze1])
        assert result == list(maze1[1])

        result = steper(maze2, z_point, w_dict[maze2])
        assert result == list(maze2[1])

        result = steper(maze3, z_point, w_dict[maze3])
        assert result == list(maze3[1])

        result = steper(maze4, z_point, w_dict[maze4])
        assert result == list(maze4[1])

    def going_beyond_the_maze(self):
        """выдача корректного результата при попытке выхода за пределы лабиринта"""
        result = steper(maze1, z_point, w_dict['ways'])
        assert result == list(maze1[1])

        result = steper(maze2, z_point, w_dict['ways'])
        assert result == list(maze2[1])

        result = steper(maze3, z_point, w_dict['ways'])
        assert result == list(maze3[0])

        result = steper(maze4, z_point, w_dict['ways'])
        assert result == list(maze4[0])

    def test_arguments(self):
        """корректная работа аргументов, которые принимают параметры
        -m аргумент должен принимать только типы лабиринтов a,b bли с
        -w принимает любую строку, содержащую буквы u,r,l,d, разделителем может быть
        печатный символ ASCII, кроме пробела, также можно передавать в виде непустого списка, кортежа, словаря.
        -d не принимает параметры, выводит отладочную информацию
        -p не принимает аргументы, выводит изображение лабиринта"""

        cmd = '-m a'
        out, err = self.call_file(cmd)
        print(out)
        assert out == b'Your position [1, 1]\r\n'

        cmd = '-m b'
        out, err = self.call_file(cmd)
        print(out)
        assert out == b'Your position [1, 1]\r\n'

        cmd = '-m c'
        out, err = self.call_file(cmd)
        print(out)
        assert out == b'Your position [0, 1]\r\n'

        cmd = '-w r,r'
        out, err = self.call_file(cmd)
        print(out)
        assert out == b'Your position [2, 0]\r\n'

        cmd = '-w rr'
        out, err = self.call_file(cmd)
        print(out)
        assert out == b'Your position [2, 0]\r\n'

        cmd = '-w u/l/d/r/t/y/r/d/u'
        out, err = self.call_file(cmd)
        print(out, err)
        assert out == b'Your position [2, 0]\r\n'

        cmd = '-w [u,r]'
        out, err = self.call_file(cmd)
        print(out, err)
        assert out == b'Your position [1, 0]\r\n'

        cmd = '-w (u,r)'
        out, err = self.call_file(cmd)
        print(out, err)
        assert out == b'Your position [1, 0]\r\n'

        cmd = "-w {1:'u',2:'r'}"
        out, err = self.call_file(cmd)
        print(out, err)
        assert out == b'Your position [1, 0]\r\n'

        cmd = '-d'
        out, err = self.call_file(cmd)
        print(out)
        assert out == b"way_list: ['r', 'u'] \r\n" \
                      b"labyrinth: {'type': ((1, 1), (0, 0), (1, 0), (2, 0)), 'zero_p': (0, 0), 'finish': (1, 1)} \r\n" \
                      b"zero_point: (0, 0)\r\n" \
                      b"Your position [1, 1]\r\n"

        cmd = 'python main.py -p'
        """корректный результат - открылось окно tk с лабиринтом, проверка глазами"""
        proc = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)

    def test_incorrect_maze_type(self):
        """передача символов кириллицы, буквы, отличной от 'a', 'b', 'c', а также пустого/не пустого списка,
        кортежа, словаря как параметра типа лабиринта"""
        cmd = '-m а'
        out, err = self.call_file(cmd)
        print(out, err)
        assert err == b"usage: main.py [-h] [-w WAY] [-m {a,b,c}] [-d] [-p]\r\n" \
                      b"main.py: error: argument -m/--maze: invalid choice: '\xe0' (choose from 'a', 'b', 'c')\r\n"
        cmd = '-m с'
        out, err = self.call_file(cmd)
        print(out, err)
        assert err == b"usage: main.py [-h] [-w WAY] [-m {a,b,c}] [-d] [-p]\r\n" \
                      b"main.py: error: argument -m/--maze: invalid choice: '\xf1' (choose from 'a', 'b', 'c')\r\n"

        cmd = '-m q'
        out, err = self.call_file(cmd)
        print(out, err)
        assert err == b"usage: main.py [-h] [-w WAY] [-m {a,b,c}] [-d] [-p]\r\n" \
                      b"main.py: error: argument -m/--maze: invalid choice: 'q' (choose from 'a', 'b', 'c')\r\n"

        cmd = '-m aa'
        out, err = self.call_file(cmd)
        print(out, err)
        assert err == b"usage: main.py [-h] [-w WAY] [-m {a,b,c}] [-d] [-p]\r\n" \
                      b"main.py: error: argument -m/--maze: invalid choice: 'aa' (choose from 'a', 'b', 'c')\r\n"

        cmd = '-m []'
        out, err = self.call_file(cmd)
        print(out, err)
        assert err == b"usage: main.py [-h] [-w WAY] [-m {a,b,c}] [-d] [-p]\r\n" \
                      b"main.py: error: argument -m/--maze: invalid choice: '[]' (choose from 'a', 'b', 'c')\r\n"

        cmd = '-m {}'
        out, err = self.call_file(cmd)
        print(out, err)
        assert err == b"usage: main.py [-h] [-w WAY] [-m {a,b,c}] [-d] [-p]\r\n" \
                      b"main.py: error: argument -m/--maze: invalid choice: '{}' (choose from 'a', 'b', 'c')\r\n"

        cmd = '-m ()'
        out, err = self.call_file(cmd)
        print(out, err)
        assert err == b"usage: main.py [-h] [-w WAY] [-m {a,b,c}] [-d] [-p]\r\n" \
                      b"main.py: error: argument -m/--maze: invalid choice: '()' (choose from 'a', 'b', 'c')\r\n"

        cmd = '-m [a]'
        out, err = self.call_file(cmd)
        print(out, err)
        assert err == b"usage: main.py [-h] [-w WAY] [-m {a,b,c}] [-d] [-p]\r\n" \
                      b"main.py: error: argument -m/--maze: invalid choice: '[a]' (choose from 'a', 'b', 'c')\r\n"

        cmd = "-m {1:1}"
        out, err = self.call_file(cmd)
        print(out, err)
        assert err == b"usage: main.py [-h] [-w WAY] [-m {a,b,c}] [-d] [-p]\r\n" \
                      b"main.py: error: argument -m/--maze: invalid choice: '{1:1}' (choose from 'a', 'b', 'c')\r\n"

        cmd = '-m (a)'
        out, err = self.call_file(cmd)
        print(out, err)
        assert err == b"usage: main.py [-h] [-w WAY] [-m {a,b,c}] [-d] [-p]\r\n" \
                      b"main.py: error: argument -m/--maze: invalid choice: '(a)' (choose from 'a', 'b', 'c')\r\n"

    def test_incorrect_way(self):
        """передача невалидной строки, содержащей пробелы, символы юникод, отсутствие букв u,r,l,d как параметр пути"""
        cmd = '-w '+way1
        out, err = self.call_file(cmd)
        print(out, err)
        assert b'IndexError: pop from empty list' in err

        cmd = '-w '+way2
        out, err = self.call_file(cmd)
        print(out, err)
        assert b'error: unrecognized arguments: \\U0001f4a3 \\U0001f4a5 \\U0001f9e8 \\U0001f914 \\U0001f50e\r\n' in err

        cmd = '-w '+way3
        out, err = self.call_file(cmd)
        print(out, err)
        assert b'error: unrecognized arguments: f w e q v\r\n' in err

        cmd = '-w '+way4
        out, err = self.call_file(cmd)
        print(out, err)
        assert b'error: unrecognized arguments: r d l\r\n' in err

        cmd = '-w '+way5
        out, err = self.call_file(cmd)
        print(out, err)
        assert b'expected one argument' in err

        cmd = '-w []'
        out, err = self.call_file(cmd)
        print(out, err)
        assert b'IndexError: pop from empty list' in err

        cmd = '-w {}'
        out, err = self.call_file(cmd)
        print(out, err)
        assert b'IndexError: pop from empty list' in err

        cmd = '-w ()'
        out, err = self.call_file(cmd)
        print(out, err)
        assert b'IndexError: pop from empty list' in err

    def test_incorrect_parameters_of_arguments(self):
        """передача параметров в аргументы, которые их не принимают"""

        cmd = '-d on'
        out, err = self.call_file(cmd)
        print(out, err)
        assert b'error: unrecognized arguments: on' in err

        cmd = '-p gif'
        out, err = self.call_file(cmd)
        print(out, err)
        assert b'error: unrecognized arguments: gif' in err

    def test_without_arguments(self):
        """вызов без аргументов"""
        cmd = ''
        out, err = self.call_file(cmd)
        print(out, err)
        assert out == b'Your position [1, 1]\r\n'

    def call_file(self, param):
        cmd = 'python main.py '+str(param)
        proc = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        out, err = proc.communicate(timeout=3)
        return out, err