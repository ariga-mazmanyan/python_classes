import random
import requests


def password_generator():

    while True:
        password = ""
        for i in range(9):
            if i % 2 == 0:
                i = chr(random.randint(ord("a"), ord("z")))

                password += i

            else:
                i = random.randint(1,9)
                password += str(i)

        yield password


def quote_generator():
    while True:
        data = requests.get("https://zenquotes.io/api/random").json()

        for i, j in data[0].items():
            yield f"{i} -- {j}"


password_1 = password_generator()
print(next(password_1))
print(next(password_1))

quote = quote_generator()
print(next(quote))
print(next(quote))