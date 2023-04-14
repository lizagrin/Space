import random

phrases = ["4 октября 1957 года был запущен первый спутник, пролетавший всего 92 дня",
           "Нептун совершил только один оборот вокруг Солнца с момента своего открытия",
           "Луна постепенно удаляется от нашей планеты. Это происходит со скоростью 38 мм в год",
           "Из-за того, что атмосфера Венеры вращается в 60 раз быстрее поверхности планеты, ветра там дуют со скоростью 500 км/ч",
           "В состоянии невесомости пламя распространяется во всех направлениях сразу",
           "Некоторые бактерии гораздо активнее растут в состоянии невесомости, нежели на Земле",
           "В одной только нашей Галактике ежегодно появляется около сорока новых звёзд",
           "Плотность некоторых газовых гигантов, например, Сатурна, меньше плотности воды",
           "В наблюдаемой части Вселенной более ста миллиардов галактик",
           "Каждые сутки на Землю падает около двухсот тысяч метеоритов, но почти все они сгорают в атмосфере",
           "На орбите вокруг Земли находится около восьми тысяч объектов. В основном это разного рода обломки и космический мусор",
           "Размеры и возраст Вселенной лежат за пределами нормального человеческого понимания",
           "Масса Земли увеличивается примерно на два миллиарда тонн каждую тысячу лет за счёт выпадающей на её поверхность космической пыли",
           "Если звезда будет пролетать близко с черной дырой ее может разорвать на части",
           "Возраст нашей солнечной около 4 миллиарда 570 миллионов лет",
           "Следы от ботинок или лунохода на Луне останутся навсегда",
           "Из-за гравитационной разницы те кто весят на Земле 100 кг на Марсе весят 38,1 килограмм",
           "Юпитер имеет 79 спутников",
           "Спутник НАСА для зондирования кратеров обнаружил воду на Луне",
           "Космос – это на самом деле пустота, которая содержит очень мало материи",
           "В видимой или известной вселенной насчитывается почти два триллиона галактик",
           "Космическое пространство между галактиками не пустое. В среднем на один кубический метр приходится один атом",
           "Галактика Андромеда приближается к нашей галактике со скоростью 110 километров в секунду",
           "Скафандр НАСА стоит 12 000 000 долларов",
           "Китайцы заметили комету Галлея ещё в 240 году до нашей эры. Начиная с 164 года до нашей эры, они отмечали каждое её появление",
           "Шимпанзе, собаки, морские свинки и обезьяны летали в космос",
           "Земля получает от Солнца за час больше энергии, чем использует за целый год",
           "Если вы окажетесь на экваторе Марса, температура у ваших ног будет тёплой, а у вашей головы – холодной"]


num1 = random.randint(0, len(phrases) - 1)
count = 0
num2 = 0
num3 = 0

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
