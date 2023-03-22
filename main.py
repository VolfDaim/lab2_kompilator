import json

from reader import readContry

if __name__ == "__main__":
    f = open("jsonFile.json")
    data = json.loads(f.read())["Страны"]
    for item in data:
        readContry(item)
    f.close()

