def recherche_sequentielle(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1

# Exemple d'utilisation :
# ma_liste = [2, 3, 4, 10, 40]
# resultat = recherche_sequentielle(ma_liste, 10)
# print("L'élément 10 est présent à l'index:", resultat)