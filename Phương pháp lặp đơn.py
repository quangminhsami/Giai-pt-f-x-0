import math

def func(x): # ham f(x)
    return (17/25) - (1/25) * (x**5) 

def func_phay(x): # ham fphay(x)
    return - (1/5) * (x**4) 

def func_2phay(x): # hamf f2phay(x)
    return - (4/5) * (x**3) 

def max_func_phay(x0, lr): # max fphay(x)
    x = [x0]
    for i in range(1000):
        x_new = x[-1] - lr * func_2phay(x[-1])
        if abs(func_2phay(x_new)) < 1e-5:
            break
        x.append(x_new)
    return func_phay(x[0])

# kiem tra khoang cach ly nghiem
print("Nhập khoảng cách ly nghiệm a và b:")
print("Nhập a = ")
a = float(input())
print("Nhập b = ")
b = float(input())
print("Nhập xấp xỉ đầu x_0 = ")
x_0 = float(input())
print("Nhập sai số epxilon = ")
epxilon = float(input())

if func(a) * func(b) >= 0:
    print("Khoang cach li nghiem ko hop le")
else:
    # q = max_func_phay(0.6, 0.01)
    q = 0.4 # tính tay  q = max(f'(x))
    # q = max(math.fabs(func_phay(a)), math.fabs(func_phay(b))) 

    epxilon_0 = epxilon * (1 - q) / q

    x_1 = func(x_0)

    i = 0   # số lần lặp

    while math.fabs(x_1 - x_0) > epxilon_0:
        x_0 = x_1
        x_1 = func(x_0)
        i += 1
        print("Nghiệm của phương trình là " + str(x_1))
    print("Số lần lặp: " + str(i))
        
    # Nghiem pt x = 1/(1 + e^(-x)) la x = 0.659046



