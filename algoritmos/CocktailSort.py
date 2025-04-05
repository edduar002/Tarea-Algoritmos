class CocktailSort:
    
    def __init__(self):
        pass

    def cocktail_sort(self, arr):
        primero = 1
        ultimo = len(arr) - 1
        dir = len(arr) - 1
        while ultimo >= primero:
            # Recorrido de derecha a izquierda
            for i in range(ultimo, primero - 1, -1):
                if arr[i - 1][1] > arr[i][1]:
                    arr[i - 1], arr[i] = arr[i], arr[i - 1]
                    dir = i
            primero = dir + 1
            # Recorrido de izquierda a derecha
            for i in range(primero, ultimo + 1):
                if arr[i - 1][1] > arr[i][1]:
                    arr[i - 1], arr[i] = arr[i], arr[i - 1]
                    dir = i
            ultimo = dir - 1
        return arr