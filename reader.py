def readContry(data):
    name = data["Название"]
    s_contry = data["Площадь"]
    s_obl = 0
    for item in data["Страна"]:
        s_obl += readObl(item)
    if s_obl != s_contry:
        print(f"Суммарная площадь областей не соответствует площади страны {name}")


def readObl(data):
    name = data["Название"]
    s_rayon = 0
    s_obl = data["Площадь"]
    for item in data["Область"]:
        s_rayon += item["Площадь"]
    if (s_rayon != s_obl):
        print(f"Суммарная площадь районов не соответствует площади области {name}")
    return s_obl
