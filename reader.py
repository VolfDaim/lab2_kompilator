def readContries(data):
    for contry in data["Страны"]:
        readContry(contry)


def readContry(data):
    s_obl = 0
    for item in data:
        s_obl += readObl(item)
    if s_obl != data["Площадь"]:
        print("foo")


def readObl(data):
    s = 0
    for item in data:
        #s += item["Площадь"]
        print(item)
    if s != data["Площадь"]:
        print("foo")
    return s
