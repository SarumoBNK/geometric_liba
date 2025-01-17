class RectangleDef():
    def area(a, b): 
        '''
        Вовращает площадь прямоугольника.
            Параметры:
                a (int) : Первая сторона прямоугольника
                b (int) : Вторая сторона прямоугольника
            
            Возвращаемое значение:
                s (int) : Произведение a и b
            
            Пример работы функции:
            >> area(10, 7)
            >> 70
        '''
        s = a * b
        return s

    def perimeter(a, b):
        ''' Принимает числа a и b, возвращает их удвоенную сумму - периметр прямоугольника

            Пример работы функции:
            >> perimeter(5, 8)
            >> 26
        '''
        return (a+b) * 2
