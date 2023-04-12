import random

phrases = ["4 октября 1957 года был запущен первый спутник, пролетавший всего 92 дня",
           "Нептун совершил только один оборот вокруг Солнца с момента своего открытия",
           "Луна постепенно удаляется от нашей планеты. Это происходит со скоростью 38 мм в год",
           "Из-за того, что атмосфера Венеры вращается в 60 раз быстрее поверхности планеты, ветра там дуют со скоростью 500 км/ч",
           "В состоянии невесомости пламя распространяется во всех направлениях сразу",
           "Некоторые бактерии гораздо активнее растут в состоянии невесомости. нежели на Земле",
           "В одной только нашей Галактике ежегодно появляется около сорока новых звёзд",
           "Плотность некоторых газовых гигантов, например, Сатурна меньше плотности воды",
           "В наблюдаемой части Вселенной более ста миллиардов галактик",
           "Каждые сутки на Землю падает около двухсот тысяч метеоритов, но почти все они сгорают в атмосфере",
           "На орбите вокруг Земли находится около восьми тысяч объектов. В основном это разного рода обломки и космический мусор",
           "Размеры и возраст Вселенной лежат за пределами нормального человеческого понимания",
           "Масса Земли увеличивается примерно на два миллиарда тонн каждую тысячу лет за счёт выпадающей на её поверхность космической пыли"]

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
