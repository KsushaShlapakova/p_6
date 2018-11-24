from math import sqrt

def diagonal_square(b, d_p):
    # The diagonal of a square
    return sqrt(d_p ** 2 - b ** 2)


def side_square(b, d_p):
    # Side of a square
    return sqrt((diagonal_square(b, d_p)/2)**2 + (diagonal_square(b, d_p)/2)**2)


def V(b, d_p):
    # Volume
    return b * side_square(b, d_p) ** 2


def main():
    # Start program
    b = float(input('Введите длину боковой стороны: '))
    d_p = float(input('Введите длину диагонали параллелепипеда: '))
    if d_p < b:
        print('Ошибка: длина боковой стороны не может быть длиннее диагонали.')
        return
    if b <= 0 or d_p <= 0:
        print('Ошибка: значения должны быть больше нуля.')
    v = V(b, d_p)
    print('Объем параллелепипеда приблизительно равен: ', int(v))


if __name__ == '__main__':
    main()
