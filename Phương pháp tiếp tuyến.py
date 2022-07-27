import math

def func(x): # ham f(x)
    return math.log(x) - 1

def func_phay(x): # ham f_phay(x)
    return 1 / x

def func_2phay(x): # ham f2phay(x)
    return -1 / (x * x)

def min_func_phay(x0, lr): # min fphay(x)
    x = [x0]
    for i in range(1000):
        x_new = x[-1] - lr * func_2phay(x[-1])
        if abs(func_2phay(x_new)) < 1e-5:
            break
        x.append(x_new)

    return func_phay(x[-1])

# kiem tra khoang cach ly nghiem
print("Nhập khoảng cách ly nghiệm a và b:")
print("Nhập a = ")
a = float(input())
print("Nhập b = ")
b = float(input())
print("Nhập sai số epxilon = ")
epxilon = float(input())

if func(a) * func(b) >= 0:
    print("Khoang cach li nghiem ko hop le")
else: # tiep tuyen
    m_1 = min_func_phay(0.06, 0.01)
    # m_1 = min(func_phay(a),func_phay(b))

    i = 0 # số lần lặp

    epxilon_0 = m_1 * epxilon

    if func(a) * func_2phay(a) > 0:
        x_0 = a
        while math.fabs(func(x_0)) > epxilon_0:
            x_0 = x_0 - func(x_0) / func_phay(x_0)
            i += 1
            print("Số e gần đúng : " + str(x_0))
        
    if func(b) * func_2phay(b) > 0:
        x_0 = b
        while math.fabs(func(x_0)) > epxilon_0:
            x_0 = x_0 - func(x_0) / func_phay(x_0)
            print("Số e gần đúng : " + str(x_0))

    print("Số lần lặp: " + str(i))

