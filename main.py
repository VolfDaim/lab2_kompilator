import json

if __name__ == "__main__":
    f = open("jsonFile.json")
    data = json.load(f)
    print(data)
    for item in data["Страны"]:
        print(item)

        print(item["Площадь"])
        for items in item:
            print(items["Площадь"])
    f.close()
