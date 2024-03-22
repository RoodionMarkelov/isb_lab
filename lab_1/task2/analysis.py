def frequency_analysis(text: str) -> list:
    """
    Функция возращает список пар - буква и её частота появления в тексте. Список отсортирован в убывающем порядке.
    :param text:
    :return list:
    """
    dictonary_of_frequency = {}
    len_text = len(text)
    for letter in text:
        if (letter not in dictonary_of_frequency.keys()):
            frequency = text.count(letter) / len_text
            dictonary_of_frequency[letter] = frequency
        else:
            continue
    result = sorted(dictonary_of_frequency.items(), key=lambda x: x[1], reverse=True)
    return result


if __name__ == "__main__":
    text = "7ОУ8cr8ЛБ8ЧХОДХЛМtcbЛrАc<МАcРcМАЕc<ХЛД8cХcБАc5МА1cБКХ<Хr8cКД8cr8cБК87ЛМОРДb8МЛbcАБМХЕОД4r ЕcОД>АКХМЕАЕcЛУОМХb?cБАЛ2АД42tcАrcr8cХЛБАД4Фt8МcrХ2О2А1cХrИАКЕОЧХХcАcЛУХЕО8ЕАЕcМ82ЛМ8?c<МАП cБАrbМ4c2О2cБКАХЛЙА7ХМcЛУОМХ8cХЛБАД4ФtaЬ88cФrОrХbcАcМ82ЛМ8cР8Кr8ЕЛbc2cБАrbМХbЕc5rМКАБХХcХcХrИАКЕОМХРrАЛМХcМ82ЛМОccЛРbФ4cЕ8У7tcР8КАbМrАЛМbЕХcХc2А7ОЕХcХФt<О8МЛbcРcОД>8ПКОХ<8Л2А1cМ8АКХХc2А7ХКАРОrХbcАЛrАРrА1cМ8АКХ81c2АМАКА1cbРДb8МЛbcrХ2МАcХrА1c2О2c2ДА7c5ДРt7cЫ8rrАrc8>АcМ8АК8Е c2А7ХКАРОrХbcХЛМА<rХ2ОcХЛБАД4ФtaМЛbcА<8r4cО2МХРrАcХcФ78Л4"
    dictonary1 = frequency_analysis(text)
    print(dictonary1)

    text = text.replace("a", "ю")
    text = text.replace("Ч", "ц")
    text = text.replace(" ", "ы")  # есть попадание
    text = text.replace("c", " ")  # есть попадание
    text = text.replace("А", "о")  # есть попадание
    text = text.replace("Х", "и")  # есть попадание
    text = text.replace("8", "е")  # есть попадание
    text = text.replace('О', "а")  # есть попадание
    text = text.replace("r", "н")  # есть попадание
    text = text.replace("2", "к")  # есть попадание
    text = text.replace("1", "й")  # есть попадание
    text = text.replace("И", "ф")  # есть попадание
    text = text.replace("К", "р")  # есть попадание
    text = text.replace("Е", "м")  # есть попадание
    text = text.replace("Ч", "и")  # есть попадание
    text = text.replace("М", "т")  # есть попадание
    text = text.replace("5", "э")  # есть попадание
    text = text.replace("Р", "в")  # есть попадание
    text = text.replace("Л", "с")  # есть попадание
    text = text.replace("<", "ч")  # есть попадание
    text = text.replace("Б", "п")  # есть попадание
    text = text.replace("Д", "л")  # есть попадание
    text = text.replace("b", "я")  # есть попадание
    text = text.replace(">", "г")  # есть попадание
    text = text.replace("4", "ь")  # есть попадание
    text = text.replace("7", "д")  # есть попадание
    text = text.replace("Ф", "з")  # есть попадание
    text = text.replace("t", "у")  # есть попадание
    text = text.replace("У", "ж")  # есть попадание
    text = text.replace("П", "б")  # есть попадание
    text = text.replace("Й", "х")  # есть попадание
    text = text.replace("Ы", "ш")  # есть попадание
    text = text.replace("?", "ъ")  # есть попадание
    text = text.replace("Ь", "щ")

    print(text)
