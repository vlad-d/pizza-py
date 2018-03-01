import numpy as np

fileName = 'data/example.in'


def readData(fileName):
    data = {}
    matrix = []
    with open(fileName, 'r') as file:
        firstLine = file.readline().split()
        data['rows'] = int(firstLine[0])
        data['columns'] = int(firstLine[1])
        data['minIngredients'] = int(firstLine[2])
        data['maxArea'] = int(firstLine[3])
        while True:
            line = file.readline()
            if not line:
                break
            row = []
            for character in line.strip():
                row.append(character)
            matrix.append(row)
            data['data'] = matrix

    return data


def printMatrix(matrix):
    for row in matrix:
        for col in row:
            print(col, end='')
        print()


def sliceThePizza(inputData):
    pizza = inputData['data']
    slicesResult = []  # list of pizza slices
    rowStart = 0
    height = 1
    width = inputData['maxArea'] - 1
    # 'slice of pizza' is defined by [height] rows x [width] columns =  pizza area
    # pizza area must be less than or equal to maxArea and more than or equal to minIngredients

    minSlicesPerBeam = 1  # min nr of slices we want to find in a beam
    while True:  # temporary
        # start beam
        print('start beam')
        colStart = 0
        slicesPerBeam = 0
        while True:  # temporary
            print('start slice')
            ingredients = []
            # compute width
            width = (int)
            rowEnd = rowStart + height
            colEnd = colStart + width
            for row in range(rowStart, rowEnd):
                for col in range(colStart, colEnd):
                    ingredients.append(pizza[row][col])
            if validateIngredients(ingredients, inputData['minIngredients'], inputData['maxArea']):
                print('valid slice')
                slicesResult.append({
                    'rowStart': rowStart,
                    'rowEnd': rowEnd,
                    'colStart': colStart,
                    'colEnd': colEnd,
                    'ingredients': ingredients
                })
                slicesPerBeam += 1
                if inputData['columns'] - colEnd > inputData['minIngredients'] * 2:
                    # if there is a chance to find another valid slice then go for it
                    colStart = colEnd + 1
                else:
                    break
            else:
                print('not valid slice')
                print(inputData['columns'] - colStart)
                if inputData['columns'] - colStart + 1 > inputData['minIngredients'] * 2:
                    colStart += 1
                else:
                    break

        # next beam
        if slicesPerBeam >= minSlicesPerBeam:
            rowStart += 1
        else:
            height += 1
            slicesResult = slicesResult[: -slicesPerBeam or None]

        if rowStart > inputData['rows'] - 1:
            break
    print(slicesResult)


def validateIngredients(ingredients, minIng, maxIng):
    mushrooms = 0
    tomatoes = 0
    for ingredient in ingredients:
        if ingredient == 'T':
            tomatoes += 1
        if ingredient == 'M':
            mushrooms += 1
    if tomatoes < minIng or mushrooms < minIng:
        return False
    if tomatoes + mushrooms > maxIng:
        return False
    return True


pizzaData = readData(fileName)
sliceThePizza(pizzaData)
# print(data['rows'], data['columns'], data['minIngredients'], data['maxArea'])
# printMatrix(data['data'])
