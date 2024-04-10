def bubble_sort(arr):
    n = len(arr)
    
    # Percorre todos os elementos do array
    for i in range(n):
        # Últimos i elementos já estão no lugar correto
        for j in range(0, n-i-1):
            # Troca se o elemento atual for maior que o próximo
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Exemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Array ordenado:")
for i in range(len(arr)):
    print(arr[i], end=" ")
