import QuadEquation
 
print("Введите коэффициенты для ax² + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

error, answer = QuadEquation.Equation(a, b, c)
if len(answer) > 1:
    print("Ответ: ")
    print(answer[0])
    print(answer[1])
elif len(answer) == 1: 
    print("Ответ: ")
    print(answer[0])
else: 
    print("Ошибка: ")
    print(error)
