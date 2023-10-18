import keyboard
import time
import slova
person = {"name": "\n\nИмя героя: Михаил", "city": "\nГород героя: Москва"}
name = person["name"]
city = person["city"]
age = 16
class9 = 9
text = "    Пол: Мужской    "
def variantmesta():
    variant = {"Вы сели на первый вариант.", "Вы сели на второй вариант."}
    print(variant.pop())
def vybor1():
    print("\nСделайте выбор:")
    global a
    try:
        vybor1 = int(input())
    except:
        print("Вы ввели неправильное значение, вам прийдется переходить игру заново(")
    if vybor1 == 1:
        print("Отношение ко мне было не очень со стороны одноклассников, я постоянно ловил косые взгляды, ко мне относились как к изгою...")
        a = 0
    if vybor1 == 2:
        print("Эту девочку звали Вика, она была очень классная как по общению, так и в учебе.", "\n Мы с ней очень хорошо ладили и я думал кое о чем с ней поговорить.")
        a = 1
    if vybor1 == 3:
        print("Эту девочку звали Саша, она странно на меня смотрела, постоянная была недовольна чем-то и меня это настораживало.")
        a = -1
def vybor2():
    print("\nСделайте выбор:")
    global b
    try:
        vybor2 = int(input())
    except:
        print("Вы ввели неправильное значение, вам прийдется переходить игру заново(")
    if vybor2 == 1:
        print("Мы договорились встретиться около парка и пошли гулять.\nЯ был удивлён её приглашению, но больше всего я удивился тому, что она была прекрасна.\nПрогулка получилась замечательной, несмотря даже на то, что было прохладно.\nМы о многом поговорили и много что обсудили.\nЭтой прогулкой я насладился, настроение стало ещё лучше, да и вспомнилось детство с зимними прогулками.")
        b = 1
    if vybor2 == 2:
        print("Встретившись у подъезда, Саша проводила к себе в квартиру. Мы сидели с ней в какой-то напряжённой обстановке, не знали о чём поговорить.\nЧтобы как-то разрядить обстановку, мы стали смотреть фильм,а после него я ушёл домой.\nВстреча с Сашей была максимально смазана, настроение стало непонятным.")
        b = -1
    if vybor2 == 3:
        print("Оставшись дома, я спокойно сделал свои дела, поиграл в Доту, пообщался с друзьями, с которыми я играю.\nВечер удался, я получил хорошие эмоции, а самое главное провёл время с теми, кем дорожу, хоть они и далеко.")
        b = 0
def vybor3():
    print("\nСделайте выбор:")
    global c
    try:
        vybor3= int(input())
    except:
        print("Вы ввели неправильное значение, вам прийдется переходить игру заново(")
    if vybor3 == 1:
        print("Вика быстро передала мне бумажку с купленными ответами.\nРаскрыв её я быстро переписал ответы, которые оказались верны, и я написал на 5.\nПоблагодарив Вику, я позвал её домой отблагодарить за это и мы отлично провели время, попивая кофе и обсуждая школьные моменты.")
        c = 1
    if vybor3 == 2:
        print("Саша передала шепотом ответ на одно из заданий, за что нам сделали замечание и чуть ли не выгнали с экзамена.\nВ итоге она передала какую-то помятую бумажку, написанную от руки, с помощью которой я написал на 3.\nПосле этого я был не в самом лучшем настроении, поэтому просто поблагодарил Сашу и пошёл домой.")
        c = -1
    if vybor3 == 3:
        print("Попытавшись решить самому и оперевшись только на свои знания, я смог написать экзамен на 4.\nПосле экзамена я пошёл домой отдыхать, поиграть со своими друзьями в игры.")
        c = 0
def vybor4():
    print("\nСделайте выбор:")
    global d
    try:
        vybor4 = int(input())
    except:
        print("Вы ввели неправильное значение, вам прийдется переходить игру заново(")
    if vybor4 == 1:
        print("Я решил провести лето самостоятельно.\nМоими самыми интересными занятиями были прогулка, компьютерные игры с моими виртуальными друзьями, а также занятие спортом. ")
        d = 0
    if vybor4 == 2:
        print("Я решил провести лето с Викой, и оно было просто незабываемым.\nМы сходили с ней в разные места Москвы, ходили в Аквапарк и даже на аттракционы.\nЯ никогда не забуду это лето, ведь оно было проведено с Викой.")
        d = 1
    if vybor4 == 3:
        print("Я решил провести лето с Сашей, я получил максимально смешанные чувства.\nБыли и хорошие и плохие моменты, но доверия к ней не было.\n С каждым днем я чувствовал, что она какая-то не такая.")
        d = -1
def konec():
    global a
    global b
    global c
    global d
    if a + b + c + d == 0:
        print("\n\tМоя жизнь в новой школе особо не удалась, так как я так и остался незаметным парнем.\nВика и Саша так и остались просто одноклассницами, не более.")
    if a + b + c + d == 1:
        print("\n\tЖизнь в новой школе была впринципе неплохой, я нашел прекрасного товарища Вику.\nНаши пути хоть и разошлись, но остались неплохие впечатления о ней.")
    if a + b + c + d == 2:
        print("\n\tМоя школьная жизнь превзошла мои ожидания, и я нашёл потрясающего друга Вику.\nРаз в неделю мы с ней видимся и вспоминаем всё, что было, а также обсуждаем какие-либо темы.")
    if (a + b + c + d == 3) or (a + b + c + d == 4):
        print("\n\tМоя школьная жизнь оказалась прекрасной, и я нашёл потрясающую девушку.\nПосле экзаменов я предложил Вике встречаться, я так рад этой новости, мы с ней гуляем почти каждый день и думаем о совместном будущем.")
    if a + b + c + d == -1:
        print("\n\tМоя школьная жизнь стала чуть хуже, чем было, Саша повлияло на моё эмоционально состояние.\nПосле школы я оправился от этого, но впечатления были не самые лучшие.")
    if a + b + c + d == -2:
        print("\n\tМоя школьная жизнь стала ужасной, так как Саша оказалась коварной, и я стал посмешищем школы.\nПосле этого я хоть и остался в этой же школе, но доверять людям перестал.")
    if (a + b + c + d == -3) or (a + b + c + d == -4):
        print("\n\tМоя школьная жизнь стала просто невыносимой, Саша обманула меня и подсадила меня на вредные привычки.\nТак как её знал почти весь район, то она распустила очень плохие слухи обо мне и меня стали преследовать по всему району, а иногда даже и избивать.\nЯ перевёлся в другую школу и полностью закрылся в себя, так как стал ненавидеть людей и жизнь.")
def anim(lst):
    keyboard.wait("ctrl")
    for i in lst:
        print(i, end="", flush=True)
        time.sleep(0.015)
anim(slova.nachalo[0])
anim(slova.nachalo[1])
anim(slova.nachalo[2])
anim(slova.nachalo[3])
anim(slova.nachalo[4])
anim(slova.nachalo[5])
anim(slova.nachalo[6])
anim(slova.znakomstvo[0])
anim(slova.znakomstvo[1])
anim(name)
print(text.strip())
message = f"\nВозраст героя:{age} лет"
anim(message)
message1 = f"\nКласс обучения:{class9} класс"
anim(message1)
anim(city)
anim(slova.mesto[0])
anim(slova.mesto[1])
anim(slova.mesto[2])
anim(slova.mesto[3])
vybor1()
variantmesta()
anim(slova.nachalozima[0])
anim(slova.nachalozima[1])
anim(slova.nachalozima[2])
anim(slova.nachalozima[3])
anim(slova.nachalozima[4])
anim(slova.nachalozima[5])
anim(slova.nachalozima[6])
anim(slova.nachalozima[7])
anim(slova.nachalozima[8])
anim(slova.nachalozima[9])
anim(slova.progulka[0])
anim(slova.progulka[1])
anim(slova.progulka[2])
vybor2()
anim(slova.nachalovaesna[0])
anim(slova.nachalovaesna[1])
anim(slova.nachalovaesna[2])
anim(slova.nachalovaesna[3])
anim(slova.nachalovaesna[4])
anim(slova.nachalovaesna[5])
anim(slova.nachalovaesna[6])
anim(slova.nachalovaesna[7])
anim(slova.nachalovaesna[8])
anim(slova.pomosh[0])
anim(slova.pomosh[1])
anim(slova.pomosh[2])
vybor3()
anim(slova.nachaloleto[0])
anim(slova.nachaloleto[1])
anim(slova.nachaloleto[2])
anim(slova.nachaloleto[3])
anim(slova.nachaloleto[4])
anim(slova.nachaloleto[5])
anim(slova.nachaloleto[6])
anim(slova.nachaloleto[7])
anim(slova.leto[0])
anim(slova.leto[1])
anim(slova.leto[2])
vybor4()
konec()
anim(slova.zakluchenie[0])
anim(slova.zakluchenie[1])
anim(slova.zakluchenie[2])
anim(slova.zakluchenie[3])
anim(slova.zakluchenie[4])
anim(slova.zakluchenie[5])
anim(slova.zakluchenie[6])
anim(slova.zakluchenie[7])
anim(slova.zakluchenie[8])
anim(slova.zakluchenie[9])
anim(slova.zakluchenie[10])
anim(slova.zakluchenie[11])
anim(slova.zakluchenie[12])
anim(slova.zakluchenie[13])
anim(slova.zakluchenie[14])
anim(slova.zakluchenie[15])
anim(slova.zakluchenie[16])
anim(slova.zakluchenie[17])
anim(slova.zakluchenie[18])
anim(slova.zakluchenie[19])
anim(slova.zakluchenie[20])
anim(slova.zakluchenie[21])
anim(slova.zakluchenie[22])
anim(slova.zakluchenie[23])
anim(slova.zakluchenie[24])
anim(slova.zakluchenie[25])
anim(slova.gameover[0])
anim(slova.gameover[1])
anim(slova.gameover[2])
anim(slova.pobeda[0])

