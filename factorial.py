def factoriaL(X):
    if X == 0:
        return 1
    else:
        return X * factoriaL(X - 1)

print(factoriaL(5))
print(factoriaL(0))
print(factoriaL(3))
print(factoriaL(1))
print(factoriaL(4))