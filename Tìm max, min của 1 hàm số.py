import numpy as np

def func(x): # Nhập hàm f(x)
    return x**2 - x + 5*np.sin(x) 

def grad(x): # Đạo hàm của f(x)
    return 2*x - 1 + 5*np.cos(x) 
# lr: learning rate (tốc độ hội tụ)
# x_0 : biến ban đầu 

lr = 0.01
x_0 = 2.4

x = [x_0] # khởi tạo 

for i in range(1000):
    x_new = x[-1] - lr * grad(x[-1])
    if abs(grad(x_new)) < 1e-5: # 1e-5 là sai số 
        break 
    x.append(x_new)

print('x = %f, min = %f, iterations = %d '%(x[-1], func(x[-1]), i))

print('x = %f, max = %f, iterations = %d '%(x[0], func(x[0]), i))

# x là nghiệm của đạo hàm
# min là giá trị nhỏ nhất của hàm số
# iterations là số lần lặp 