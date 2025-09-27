import numpy as np
from sko.DE import DE

# دالة الهدف
def obj_func(p):
    x1, x2, x3 = p
    return x1 ** 2 + x2 ** 2 + x3 ** 2

# القيود
constraint_eq = [
    lambda x: 1 - x[1] - x[2]    # x2 + x3 = 1
]

constraint_ueq = [
    lambda x: 1 - x[0] * x[1],   # x1*x2 >= 1
    lambda x: x[0] * x[1] - 5    # x1*x2 <= 5
]

# تهيئة DE
de = DE(func=obj_func, n_dim=3, size_pop=50, max_iter=800,
        lb=[0, 0, 0], ub=[5, 5, 5],
        constraint_eq=constraint_eq, constraint_ueq=constraint_ueq)

# تشغيل الخوارزمية
best_x, best_y = de.run()
print('DE - best_x:', best_x, '\nDE - best_y:', best_y)
