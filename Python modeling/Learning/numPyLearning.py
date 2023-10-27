import numpy as np

twoDimarr = np.eye(4) # - утворює 2-вимірний масив з заданою к-стю масивів в ньому 

print(twoDimarr[...]) # - під час індексування ... оператор означає нескінченну к-сть (обмежену глибиною масива) операторів :, що копіюють весь масив на даному рівні
print(twoDimarr[twoDimarr>0]) # - повертає одновимірний масив з елементами, що задовольнили умову

print(twoDimarr.T) # - придає масиву сприятливого вигляду для читання
print(twoDimarr.shape) # - (к-сть рядків, к-сть стовпців)
print(twoDimarr.ravel()) 

#-------------------------------------Duck Typing - компілятору байдуже на сам об'єкт, з котрого викликається метод, якщо метод є - то все правильно
# def func(obj):
#     obj.execute()

# class duck:
#     def execute(self):
#         print("instance of duck is executing")

# class bird:
#     def execute(self):
#         print("instance of bird is executing")

# obj1 = duck()
# obj2 = bird()

# func(obj1)
# func(obj2)
#------------------------------------------------------------------------------

print(np.mean(twoDimarr*2)) # - такі встроєні функції більш оптимізовані ніж їх інтерпретація plain codo'м, оскільки NumPy наперед знає, якого типу всі елементи даного масиву. А Python - ні, через Duck Typing