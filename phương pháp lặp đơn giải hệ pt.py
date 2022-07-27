import numpy as np

A = np.loadtxt('single_loop.txt', dtype = float)
b = np.array([1,2,3,4])

print(np.linalg.solve(A,b))

# kiem tra cheo troi

# duong cheo
diag_A = np.diag(np.abs(A)) 

# tong theo hang
sum_of_row_except_diag_A = np.sum(np.abs(A), axis = 1) - diag_A 

# tong theo cot
sum_of_col_except_diag_A = np.sum(np.abs(A), axis = 0) - diag_A 

# kiem tra ma tran cheo troi
if np.all(diag_A > sum_of_row_except_diag_A) and np.all(diag_A > sum_of_col_except_diag_A):
    print('A la ma tran cheo troi')

    eps = float(input())

    # xap xi dau x0
    x0 = np.zeros_like(b)

    # kich thuoc theo hang cua ma tran A
    n,_ = np.shape(A)

    # ma trận đơn vị của A
    I = np.identity(n) 

    i = 0 # so lan lap

    # ma trận nghich dao đường chéo của A
    T = np.linalg.inv(np.diag(np.diag(A)))

    B = I - np.dot(T, A)

    d = np.dot(T, b)

    x1 = np.dot(B, x0) + d

    norm_1 = np.linalg.norm(B, 1) # chuẩn 1 của ma trận B
    norm_inf = np.linalg.norm(B, np.inf) # chuẩn vo cung của ma trận B

    if norm_1 < 1 :
        print('thoa man dieu kien hoi tu')

        lst = np.diag(A)

        lamda = max(abs(lst)) / min(abs(lst))

        eps0 = ((1 - norm_1) * eps) / ( lamda * norm_1)

        while np.linalg.norm((x1 - x0), 1) > eps0:
            x0 = x1
            x1 = np.dot(B, x0) + d
            i += 1
            print(x1)
        print("so lan lap", i)

    elif norm_inf < 1:
        eps0 = ((1 - norm_inf) * eps) / norm_inf

        while np.linalg.norm((x1 - x0), np.inf) > eps0 :
            x0 = x1
            x1 = np.dot(B, x0) + d
            i += 1
            print(x1)
        print("so lan lap", i)
    else:
        print("khong thoa man dieu kien hoi tu")

else:
    print('A khong phai ma tran cheo troi')