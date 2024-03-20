def frequency_analysis(text: str):
    dictonary_of_frequency = {}
    len_text = len(text)
    for letter in text:
        if(letter not in dictonary_of_frequency.keys()):
            frequency = text.count(letter) / len_text
            dictonary_of_frequency[letter] = frequency
        else:
            continue
    return dictonary_of_frequency

if __name__ == "__main__":
    text = "7ОУ8cr8ЛБ8ЧХОДХЛМtcbЛrАc<МАcРcМАЕc<ХЛД8cХcБАc5МА1cБКХ<Хr8cКД8cr8cБК87ЛМОРДb8МЛbcАБМХЕОД4r ЕcОД>АКХМЕАЕcЛУОМХb?cБАЛ2АД42tcАrcr8cХЛБАД4Фt8МcrХ2О2А1cХrИАКЕОЧХХcАcЛУХЕО8ЕАЕcМ82ЛМ8?c<МАП cБАrbМ4c2О2cБКАХЛЙА7ХМcЛУОМХ8cХЛБАД4ФtaЬ88cФrОrХbcАcМ82ЛМ8cР8Кr8ЕЛbc2cБАrbМХbЕc5rМКАБХХcХcХrИАКЕОМХРrАЛМХcМ82ЛМОccЛРbФ4cЕ8У7tcР8КАbМrАЛМbЕХcХc2А7ОЕХcХФt<О8МЛbcРcОД>8ПКОХ<8Л2А1cМ8АКХХc2А7ХКАРОrХbcАЛrАРrА1cМ8АКХ81c2АМАКА1cbРДb8МЛbcrХ2МАcХrА1c2О2c2ДА7c5ДРt7cЫ8rrАrc8>АcМ8АК8Е c2А7ХКАРОrХbcХЛМА<rХ2ОcХЛБАД4ФtaМЛbcА<8r4cО2МХРrАcХcФ78Л4"
    dictonary1 = frequency_analysis(text)
    print(dictonary1)
