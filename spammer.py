from selenium import webdriver
import time
browser = webdriver.Chrome('PATH/chromedriver')

# Превьюха
print( """                                          
  mmmm  m    mmmmmmmm m    m m    m   mm  
 #"   " #    #   #    #    # #  m"    ##  
 "#mmm  #mmmm#   #    #    # #m#     #  #  -------------------
     "# #    #   #    #    # #  #m   #mm#  |   by Mr.Devid   | 
 "mmm#" #    #   #    "mmmm" #   "m #    # -------------------   
 """)

# Счетчики
schet = 0 # Счетчик сообщений
prohod = 0 # Счетчик проходов 
skolko = 5 # Сколько нужно написать сообщений
chil = 2 # После скольки сообщений делать перерыв
time_chil = 0.2 # Сколько минут ждать во время перерыва. Пример: 0.1 = 6 секунд

# Запрос пароля и логина 
log = "" #Логин
pas = "" # Пароль

# Сообщение 
message = """Здравствуйте! 
У вас классный аккаунт!!)
Я предполагаю, что вы открыты к разговору)
Давайте знакомиться)). 
Совсем недавно развиваюсь в одном интернет проекте). 
Для меня неожиданно, что я стала этим заниматься))) Но после объявления продления самоизоляции до 30 апреля, перестала ждать у моря погоды и включился здравый смысл!))"""


# Вход в инсту
browser.get("https://www.instagram.com")
time.sleep(2)
browser.find_element_by_xpath("//section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys(log)
browser.find_element_by_xpath("//section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys(pas)
browser.find_element_by_xpath("//section/main/article/div[2]/div[1]/div/form/div[4]").click()
time.sleep(4)
browser.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()

users = open("filter_users.txt", "r")

# Цикл в котором всё происходит
while prohod <= skolko: 

    chiller = prohod%chil # Матиматическая штучка для пофиг чего 
    
    if chiller == 0 and prohod != 0: # Условие для паузы
        time.sleep(time_chil)
        print("")
        print("---------------------------------------------------")
        print("|    Сейчас у нас отдых что бы не получить бан    |")
        print("---------------------------------------------------")
        print("")

    prohod += 1 # Считаем проходы 

    # Берём людей со списка и проходимся по каждому 
    for user_link in users:
        browser.get(user_link) # Переход на страничку пользователя

        # Хитрая штука. Работает хоть и не должно. Или должно?......
        try:
            if browser.find_element_by_xpath('//section/main/div/header/section/div[1]/div[1]/span/span[1]/button').text == "Подписаться":
                # Подписываемся
                browser.find_element_by_xpath("//section/main/div/header/section/div[1]/div[1]/span/span[1]/button").click()
                time.sleep(2)

                # Откриваем чат
                browser.find_element_by_xpath("//section/main/div/header/section/div[1]/div[1]/div/button").click()
                time.sleep(3)
             
                # Пишем сообщение 
                browser.find_element_by_xpath("//section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(message)
                time.sleep(2)
                # Отправляем сообщение
                browser.find_element_by_xpath("//section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
                time.sleep(2)

        except:

            # Откриваем чат
            browser.find_element_by_xpath("//section/main/div/header/section/div[1]/div[1]/div/button").click()
            time.sleep(4)
         
            # Пишем сообщение 
            browser.find_element_by_xpath("//section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(message)
            time.sleep(2)

            # Отправляем сообщение
            browser.find_element_by_xpath("//section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
            time.sleep(2)

            # Декоративная фигня. Для удобства и отслеживания действий 
            user = user_link[26::]
            user = ' '.join(user)
            schet += 1
            print("Написано пользователю: " + user)
            print("Это сообщение № " + str(schet))
            print("------------------------------")
            print("")
