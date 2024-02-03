def tri_selection(arr):
    for i in range(len(arr)):
        indice_min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[indice_min]:
                indice_min = j
        arr[i], arr[indice_min] = arr[indice_min], arr[i]
    return arr

# Exemple d'utilisation :
# ma_liste = [64, 25, 12, 22, 11]
# tri_selection(ma_liste)
# print("Liste triée:", ma_liste)