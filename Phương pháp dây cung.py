import math

def func(x): # ham f(x)
    return x**6 - 15

def func_phay(x): # ham fphay(x)
    return 6 *(x**5)

def func_2phay(x): # ham f2phay(x)
    return 30 * (x**4)

def max_func_phay(x0, lr): # max fphay(x)
    x = [x0]
    for i in range(1000):
        x_new = x[-1] - lr * func_2phay(x[-1])
        if abs(func_2phay(x_new)) < 1e-5:
            break
        x.append(x_new)

    return func_phay(x[0])

def min_func_phay(x0, lr): # min fphay(x)
    x = [x0]
    for i in range(1000):
        x_new = x[-1] - lr * func_2phay(x[-1])
        if abs(func_2phay(x_new)) < 1e-5:
            break
        x.append(x_new)

    return func_phay(x[-1])

print("Nhập khoảng cách ly nghiệm a và b:")
print("Nhập a = ")
a = float(input())
print("Nhập b = ")
b = float(input())
print("Nhập sai số epxilon = ")
epxilon = float(input())

if func(a) * func(b) >= 0:
    print("Khoang cach li nghiem ko hop le")
else: # day cung
    i = 0 # số lần lặp
    if func(a) * func(b) < 0  and func_phay(a) * func_phay(b) > 0 and func_2phay(a) * func_2phay(b) > 0:
        if (func(a) * func_2phay(a) > 0):
            d = a 
            x_0 = b
        else:
            d = b 
            x_0 = a

        F_d = func(d)

        M1 = max_func_phay(0.6, 0.01)
        m1 = min_func_phay(0.6, 0.01)

        # M1 = max(math.fabs(func_phay(a)), math.fabs(func_phay(b)))
        # m1 = min(math.fabs(func_phay(a)), math.fabs(func_phay(b)))

        epxilon_0 = (epxilon * m1) / (M1 - m1) 
        F_0 = func(x_0)
        x_1 = (x_0 - F_0 * (x_0 - d)) / (F_0 - F_d)

        while math.fabs(x_1 - x_0) >= epxilon_0:
            x_0 = x_1
            F_0 = func(x_0)
            x_1 = x_0 - ((F_0 * (x_0 - d)) / (F_0 - F_d))
            i += 1
            print("Số pi gần đúng là: " + str(x_1))
    else:
        print("ko hop le")
    print("Số lần lặp là: " + str(i))


