import os


def count_line_dig():

    dig_count = 0

    with open(f"new_file.txt") as txt:
        for line in txt:
            for i in line:
                if i.isdigit():
                    dig_count += 1
                print(dig_count)


def specific_dig_count(a):

    count = 0
    with open(f"new_file.txt") as txt:
        for i in txt:
            if i == a:
                count += 1

    return count


def special_word():

    list_1 = []
    file_obj = open(f"new_file.txt", "r")
    txt = file_obj.read()
    x = txt.split()

    for i in x:
        if i.startswith("<<") and i.endswith(">>"):
            list_1.append(i)

    return list_1

print(special_word())

# 4


new_file_txt = ""
path = "new_file.txt"
file_obj = open(path, "r")
txt = file_obj.read()

for i in txt:
    if not i.isdigit():
        new_file_txt += i

new_file = os.path.join(os.getcwd(), "2nd_file.txt")
with open(new_file, "a") as new_file:
    new_file.write(new_file_txt)