def tri_bulles(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Exemple d'utilisation :
# ma_liste = [64, 34, 25, 12, 22, 11, 90]
# tri_bulles(ma_liste)
# print("Liste triée:", ma_liste)