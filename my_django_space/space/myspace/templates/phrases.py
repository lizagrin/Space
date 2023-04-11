import random

phrases = ["4 октября 1957 года был запущен первый спутник, пролетавший всего 92 дня",
           "красный",
           "желтый",
           "зеленый",
           "синий"]

num1 = random.randint(0, len(phrases) - 1)
count, num2, num3 = 0, 0, 0
while num2 == num1:
    num2 = random.randint(0, len(phrases) - 1)
while num3 == num2 or num3 == num1:
    num3 = random.randint(0, len(phrases) - 1)
if count == 1:
    print(phrases[num1])
elif count == 2:
    print(phrases[num2])
else:
    print(phrases[num3])
