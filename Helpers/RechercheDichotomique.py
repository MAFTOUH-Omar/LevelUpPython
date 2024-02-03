def recherche_dichotomique(arr, element):
    debut = 0
    fin = len(arr) - 1
    while debut <= fin:
        milieu = (debut + fin) // 2
        if arr[milieu] == element:
            return milieu
        elif arr[milieu] < element:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return -1

# Exemple d'utilisation :
# ma_liste = [2, 3, 4, 10, 40]
# resultat = recherche_dichotomique(ma_liste, 10)
# print("L'élément 10 est présent à l'index:", resultat)