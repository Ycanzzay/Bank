K = int(input())
N = int(input())
L = int(input())
def bank(K,N,L):
    for _ in range(N):
        K += K * (L/100)
    return K

result = bank(K, N, L)

print(f"Человек,в результате вклада получит:{result} рублей")