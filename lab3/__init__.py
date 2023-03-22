import re


def z1():
    print("Задание 1")
    pattern = "abc\w*"
    print(re.match(pattern, "abcdefg"))
    print(re.match(pattern, "abcde"))
    print(re.match(pattern, "abc"))


def z1_2():
    print("Задание 1.2")
    pattern = '[A-Za-z "=;]*\d{0,4}[A-Za-z "=;]*'
    print(re.match(pattern, "abc123xyz"))
    print(re.match(pattern, 'define "123"'))
    print(re.match(pattern, "var g = 123;"))


def z2():
    print("Задание 2")
    pattern = '[a-z0-9?=+]{3}\.'
    print(re.match(pattern, "cat."))
    print(re.match(pattern, '896.'))
    print(re.match(pattern, "?=+."))
    print(re.match(pattern, "abc1"))


def z3():
    print("Задание 3")
    pattern = '[cmf]an'
    print(re.match(pattern, "can"))
    print(re.match(pattern, 'man'))
    print(re.match(pattern, "fan"))
    print(re.match(pattern, "dan"))
    print(re.match(pattern, "ran"))
    print(re.match(pattern, "pan"))


def z4():
    print("Задание 4")
    pattern = "[^b]og"
    print(re.match(pattern, "hog"))
    print(re.match(pattern, "dog"))
    print(re.match(pattern, "bog"))


def z5():
    print("Задание 5")
    pattern = '[A-C][d-z][a-c]'
    print(re.match(pattern, "Ana"))
    print(re.match(pattern, 'Bob'))
    print(re.match(pattern, "Cpc"))
    print(re.match(pattern, "aax"))
    print(re.match(pattern, "bby"))
    print(re.match(pattern, "ccz"))


def z6():
    print("Задание 6")
    pattern = "waz{2,5}up"
    print(re.match(pattern, "wazzzzzup"))
    print(re.match(pattern, "wazzzup"))
    print(re.match(pattern, "wazup"))


def z7():
    print("Задание 7")
    pattern = 'a\w+'
    print(re.match(pattern, "aaaabcc"))
    print(re.match(pattern, 'aabbbbc'))
    print(re.match(pattern, "aacc"))
    print(re.match(pattern, "a"))


def z8():
    print("Задание 8")
    pattern = '\d\d? files? found?\?'
    print(re.match(pattern, "1 file found?"))
    print(re.match(pattern, '2 files found?'))
    print(re.match(pattern, "24 files found?"))
    print(re.match(pattern, "No files found."))


def z9():
    print("Задание 9")
    pattern = '\d. \s+abc'
    print(re.match(pattern, "1.   abc"))
    print(re.match(pattern, '2.        abc'))
    print(re.match(pattern, "3.            abc"))
    print(re.match(pattern, "abc"))


def z10():
    print("Задание 10")
    pattern = '^([A-Za-z]+: successful)$'
    print(re.match(pattern, "Mission: successful"))
    print(re.match(pattern, 'Last Mission: unsuccessful'))
    print(re.match(pattern, "Next Mission: successful upon capture of target"))


def z11():
    print("Задание 11")
    pattern = '^(\w+).pdf$'
    print(re.match(pattern, "file_record_transcript.pdf"))
    print(re.match(pattern, 'file_07241999.pdf'))
    print(re.match(pattern, "testfile_fake.pdf.tmp"))


def z12():
    print("Задание 12")
    pattern = '^(\w{3} (\d{4}))$'
    print(re.sub(pattern, "Jan 1987", "Jan 1987 1987"))
    print(re.sub(pattern, 'May 1969', 'May 1969 1969'))
    print(re.sub(pattern, "Aug 2011", "Aug 2011 2011"))


def z13():
    print("Задание 13")
    pattern = '^((\d+)x(\d+))$'
    print(re.sub(pattern, "1280x720", "1280 720"))
    print(re.sub(pattern, '1920x1600', '1920 1600'))
    print(re.sub(pattern, "1024x768", '1024 768'))


def z14():
    print("Задание 14")
    pattern = 'I love (cats|dogs)'
    print(re.match(pattern, "I love cats"))
    print(re.match(pattern, 'I love dogs'))
    print(re.match(pattern, "I love logs"))
    print(re.match(pattern, "I love cogs"))


if __name__ == '__main__':
    z1()
    z1_2()
    z2()
    z3()
    z4()
    z5()
    z6()
    z7()
    z8()
    z9()
    z10()
    z11()
    z12()
    z13()
    z14()
