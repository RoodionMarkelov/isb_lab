matrix_of_letter = [
    ["а", "б", "в", "г", "д"],
    ["е", "ё", "ж", "з", "и"],
    ["й", "к", "л", "м", "н"],
    ["о", "п", "р", "с", "т"],
    ["у", "ф", "х", "ц", "ч"],
    ["ш", "щ", "ъ", "ы", "ь"],
    ["э", "ю", "я", " ", " "]
]

signs = {".", ","}
def get_i_j(letter: str):
    for i in range(0, 7):
        for j in range(0, 5):
            if (letter == matrix_of_letter[i][j]):
                return i,j
# print(get_i_j("я"))