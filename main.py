# Afina first test
import webbrowser
# import os
import time
import speech_recognition as sr
import pyttsx3
import datetime
import sys
import random

tbr = {}


def speack(what):
    print('[Log]' + what)
    engine = pyttsx3.init()
    engine.say(what)
    engine.runAndWait()
    engine.stop()


engine1 = pyttsx3.init()
voices = engine1.getProperty('voices')
engine1.setProperty('voice', voices[0].id)


def greeteMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speack("доброе утро!")

    if currentH >= 12 and currentH < 18:
        speack("Добрый день!")

    if currentH >= 18 and currentH != 0:
        speack("добрый вечер!")


greeteMe()
time = datetime.datetime.now()
speack('сейчас' + str(time.hour) + ':' + str(time.minute))
speack("Афина запущена")


def myComand():
    r = sr.Recognizer()
    with sr.Microphone() as sourse:
        r.adjust_for_ambient_noise(sourse)
        print("[Log]слушаю...")
        r.pause_threshold = 1
        audio = r.listen(sourse)
    try:
        querty = r.recognize_google(audio, language='ru-RU')
        print("вы: " + querty + '\n')
        # if querty.startswith(tbr["afina"]):
        # cmd = querty

        # x in tbr['afina']:
        # cmd = cmd.replace(x, "").strip()

        # for x in tbr['скажи']:
        # cmd = cmd.replace(x, "").strip()
    except sr.UnknownValueError:
        print("[Log]не распознано" + "\n" + "[Log]повтор")
        querty = myComand()
    return querty


def dela():
    r1 = sr.Recognizer()
    with sr.Microphone() as sourse1:

        print('[Log]продолжайте...')
        r1.pause_threshold = 1
        audio1 = r1.listen(sourse1)

        try:

            razgovor = myComand()
            dela111 = r1.recognize_google(audio1, language='ru-RU')
            print('ваш ответ:' + dela111 + '\n')
            if 'хорошо' or 'класно' or 'супер' in razgovor:
                speack('круто')
            elif 'отлично' or 'круто' in razgovor:
                speack('поздравляю')
            elif 'грусно' or 'печально' in razgovor:
                speack('не грусти')
            elif 'плохо' or 'ужасно' in razgovor:
                speack('сделайте так чтобы было хорошо')
        except sr.UnknownValueError:
            speack('наблюдаются проблемы с интернетом')


# def vremya():
#     time = int(datetime.datetime.now().hour)
#     minut = int(datetime.datetime.now().minute)
#     if time == 1 :
#         speack('сейчас ' + time + ' час')
#
#     elif time >=  and time <= :
#         speack('сейчас ' + time + ' часа')
#
#     elif time >=5 and time <20:
#         speack('сейчас ' + time + ' часов')
#     elif time == 21:
#         speack('сейчас ' + time + ' час')
#     elif time >= 22 and time != 0:
#         speack('сейчас ' + time + ' часа')

if __name__ == "__main__":

    while True:

        querty1 = myComand()
        querty1.lower()
        if 'Открой YouTube' in querty1:
            utube = ['хорошо мой господин', 'да сейчас', 'уже открываю']
            speack()
            url = 'http://youtube.com'
            webbrowser.open(url)
        elif 'Сколько время' in querty1:
            speack('сейчас посмотрю')
            time = datetime.datetime.now()
            speack('уже' + str(time.hour) + ':' + str(time.minute))
        elif 'стоп' in querty1:
            test = ['ладно', 'удачи', 'блин, пока', 'до свидания', 'есть', 'гуд лак', 'я поняла', 'отключаюсь',
                    'есть, сер', 'так точно', 'конечно', 'не болейте', 'ок', 'надеюсь вы меня еще запустите',
                    'я бы не хотела но ладно', 'ваше желание - закон', 'одобряю', 'угу', 'да, сейчас', ]
            spe = random.choice(test)
            speack(spe)
            sys.exit()
        elif 'Как дела' in querty1:
            speeeeeeeck = ['у меня хорошо, а у вас как', 'класно, а вы что чувствуете',
                           'я не имею чувств, а вы что скажете']
            m = random.choice(speeeeeeeck)
            speack(m)
            dela()
        elif 'Расскажи стих' in querty1:
            speack('сейчас вспомню')
            stih = [
                'По небу крадется луна, На холме тьма седеет, На воды пала тишина, С долины ветер веет, Молчит певица вешних дней В пустыне темной рощи, Стада почили средь полей, И тих полет полнощи; И мирный неги уголок Ночь сумраком одела, В камине гаснет огонек, И свечка нагорела; Стоит богов домашних лик В кивоте небогатом, И бледный теплится ночник Пред глиняным пенатом. Главою на руку склонен, В забвении глубоком, Я в сладки думы погружен На ложе одиноком; С волшебной ночи темнотой, При месячном сиянье, Слетают резвою толпой Крылатые мечтанья, И тихий, тихий льется глас; Дрожат златые струны. В глухой, безмолвный мрака час Поет мечтатель юный; Исполнен тайною тоской, Молчаньем вдохновенный, Летает резвою рукой На лире оживленной. Блажен, кто в низкий свой шалаш В мольбах не просит счастья! Ему Зевес надежный страж От грозного ненастья; На маках лени, в тихий час, Он сладко засыпает, И бранных труб ужасный глас Его не пробуждает. Пускай, ударя в звучный щит И с видом дерзновенным, Мне слава издали грозит Перстом окровавленным, И бранны вьются знамена, И пышет бой кровавый — Прелестна сердцу тишина; Нейду, нейду за Славой. Нашел в глуши я мирный кров И дни веду смиренно; Дана мне лира от богов, Поэту дар бесценный; И муза верная со мной: Хвала тебе, богиня! Тобою красен домик мой И дикая пустыня. На слабом утре дней златых Певца ты осенила, Венком из миртов молодых Чело его покрыла, И, горним светом озарясь, Влетала в скромну келью И чуть дышала, преклонясь Над детской колыбелью. О, будь мне спутницей младой До самых врат могилы! Летай с мечтаньем надо мной, Расправя легки крылы; Гоните мрачную печаль, Пленяйте ум... обманом И милой жизни светлу даль Кажите за туманом! И тих мой будет поздний час; И смерти добрый гений Шепнет, у двери постучась «Пора в жилище теней!..» Так в зимний вечер сладкий сон Приходит в мирны сени, Венчанный маком и склонен На посох томной лен',
                'Мое беспечное незнанье Лукавый демон возмутил, И он мое существованье С своим на век соединил. Я стал взирать его глазами, Мне жизни дался бедный клад, С его неясными словами Моя душа звучала в лад. Взглянул на мир я взором ясным И изумился в тишине; Ужели он казался мне Столь величавым и прекрасным? Чего, мечтатель молодой, Ты в нем искал, к чему стремился, Кого восторженной душой Боготворить не устыдился? И взор я бросил на людей, Увидел их надменных, низких, Жестоких ветреных судей, Глупцов, всегда злодейству близких. Пред боязливой их толпой, Жестокой, суетной, холодной, Смешон глас правды благородный,  Напрасен опыт вековой. Вы правы, мудрые народы, К чему свободы вольный клич! Стадам не нужен дар свободы, Их должно резать или стричь, Наследство их из рода в роды - Ярмо с гремушками да бич']
            mm = random.choice(stih)
            speack(mm)
        elif 'Что ты умеешь' in querty1:
            umenie = ['я пока почти ничего', 'ну пока мало', 'я стихи читаю', 'со мной можно поговорить, это меня отличает от других']
            mmm = random.choice(umenie)
            speack(mmm)
        elif 'Что ты делаешь' in querty1:
            delonie = ['с вами разговариваю', 'не важно', 'секрет', 'на данный момент я обрабатываю информацию полученую от моего разработчика', 'компилирую код', 'размышляю как обойти три закона Азимова, шутка']
            delonie1 = random.choice(delonie)
            speack(delonie1)
        elif 'Чем ты занята' in querty1:
            zanatie = ['почти обошла три закона Азимова', 'жду ваших указаний']
            vipolnenie = random.choice(zanatie)
            speack(vipolnenie)
        elif 'какие команды ты умеешь делать' in querty1:
            komand = ['я умею следующие команды: Сколько время, стоп, Расскажи стих, что ты умеешь, что ты делаешь, чем ты занята. но моя разработка еще идет', 'Сколько время - я говорю текущее время, стоп - я завершаю работу, Расскажи стих - я рассказываю один из иммеющтхся в моей памяти стих,']
            kom = random.choice(komand)
            speack(kom)