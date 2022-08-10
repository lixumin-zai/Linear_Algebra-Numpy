import numpy as np

def basic_operations(A: np.ndarray):
    # 求行列式
    D = np.linalg.det(A)
    print(D)

    # 转置
    A1 = A.T
    print(A)

    # 逆矩阵
    if D !=0:
        B = np.linalg.inv(A)
        print(B)
    E = np.dot(A, B)
    print(E)

    # 伴随矩阵
    A_bs = B*np.linalg.det(A)
    print(A_bs)

if __name__ == "__main__":
    A = np.mat("[1 2;3 4]")
    basic_operations(A)