# Код был написан опираясь на принципы программирования 
# Вот приблезительный список использовавшихся пригципов
#	- Хуяк-Хуяк и в продакшн
#	- Работает - не трогай
# 	- Не знаю как это вообще работает.. Но что-то происходит


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time
from datetime import timedelta, datetime

browser = webdriver.Chrome('PATH/chromedriver')

days = 20 # Максимальное количество дней с момента последней публикации
acc_subscription = 500 # Максимум подписок на аккаутне 
publications = 10 #Минимум публикаций
schet = 0 # Создание счётчика
today = datetime.now() # Получаем сегодняшнюю дату

# Магическая функция отлова ошибок
def xpath_existance(url):
	try:
		browser.find_element_by_xpath(url)
		existence = 1
	except NoSuchElementException:		
		existence = 0
	return existence

# Запрос пароля и логина 

log = "meta_traveler"
pas = "travel"

# log = "_nakrut0chka_"
# pas = "kasha228"


# Вход в инсту
browser.get("https://www.instagram.com")
time.sleep(2)
browser.find_element_by_xpath("//section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys(log)
browser.find_element_by_xpath("//section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys(pas)
browser.find_element_by_xpath("//section/main/article/div[2]/div[1]/div/form/div[4]").click()
time.sleep(4)
browser.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()

# Открываем нужные файлы
users = open("users.txt", "r") 
filter_users = open("filter_users.txt", "a")


file_list = [] # Создание пустого списка

# Считиваем из файла всех ссылок на пользователей
for user in users:
	file_list.append(user) # Наполняем список пользователями
users.close()

filtered_list = [] # Создание отфильрованого списка

i = 0 # Количество подходящих аккаунтов
j = 0 # Номер вывода в терминале
index = 0
# Цикл фильтрации данных
# Высокоинтелектуальная штука
# P.S. Работает через п#зду собаки
# P.S.S. Такое чувство, что этот код наговнякала упоротая обезъяна под спидами

for person in file_list:
	time.sleep(3)
	j += 1
	browser.get(person)
	time.sleep(1.5)

	# 1) Проверка аккаунта на закрытость 
	element = "//section/main/div/div/article/div[1]/div/h2"
	# Обращаемся к магической функции отлова ошибок
	if xpath_existance(element) == 1:
		try:
			# Проверка на закрытость 
			if browser.find_element_by_xpath(element).text == "Thi Account is Private" or "Это закрытый аккаунт":
				print(str(j) + " Приватный аккаунт")
				continue
		except StaleElementReferenceException:
			print(j, " Ошибка, код ошибки: 1")


	# 2) Проверка на допустимое число подписчиков аккаунта 
	element = "//section/main/div/header/section/ul/li[3]/a/span"
	# Обращаемся к магической функции отлова ошибок
	if xpath_existance(element) == 0:
		print(j, " Ошибка, код ошибки: 2")
		continue

	status = browser.find_element_by_xpath(element).text # Считиваем текст с элемента (Количество подписчиков)
	status = status.replace(" ", "") # Убираем пробелы с полченого числа

	if int(status) > acc_subscription: # Проверка на допустимое количество подписчиков
		print(j, " слишком много подписчиков")


	# 3) Проверка на наличие ссылки на сайт в профиле 
	element = "//section/main/div/header/section/div[2]/a"
	# Обращаемся к магической функции что бы проверить профиль на наличие ссылки
	if xpath_existance(element) == 1:
		print(j, " Есть ссылка на сайт")
		continue

	# 4) Проверка на наличие как минимум заданого числа публикаций
	element = "//section/main/div/header/section/ul/li[1]/span/span"
	# Обращаемся к магической функции отлова ошибок
	if xpath_existance(element) == 0:
		print(j, " Ошибка, код ошибки: 4")
		continue

	status = browser.find_element_by_xpath(element).text # Получаем текст с элемента (Количество публикаций)
	status = status.replace(" ", "") # Удаляем пробелы (На случай если их больше 999 штук. Это же какой упоротой инстасамкой нужно быть что бы иметь больше 999 публкаций?)

	if int(status) < publications: # Проверяем есть ли нужное количество публикаций на аккаунте
		print(j, " У аккаунта слишком мало публикаций")
		continue

	# 5) Проверка на наличие аватарки 
	element = "//section/main/div/header/div/div/span/img"
	# Обращаемся к магической функции отлова ошибок
	if xpath_existance(element) == 0:
		print(j, " Ошибка, код ошибки: 5")

	status = browser.find_element_by_xpath(element).get_attribute("src") #Получем данные с аватарки в нужном виде для проверки
	if status.find("s150x150") == -1: # Проверяем на наличие данной строки в полученых данных (Эти значения там есть только когда есть аватарка)
		print(j, " Профиль без аватарки")
		continue

	# 6) Проверка на дату последней публикации
	# САМАЯ УПОРОТАЯ ЧАСТЬ КОДА (По моему скромному мнению)
	element = "//a[contains(@href, '/p/')]" # Все посты в коде страницы имеют начало "/p/". Мы берем первый в списке (Последный пост)
	# Обращаемся к магической функции отлова ошибок
	if xpath_existance(element) == 0:
		print(j, " Ошибка, код ошибки: 6")
		continue

	status = browser.find_element_by_xpath(element).get_attribute("href") # Получаем ссылку на последный пост
	browser.get(status) # Переходим на последный пост

	post_date = browser.find_element_by_xpath("//time").get_attribute("datetime") # Получаем дату появления последнего поста с помощью поиска элемента "//time" на странице
	year = int(post_date[0:4]) # Делаем срез получая год
	month = int(post_date[5:7]) # Делаем срез получая месяц
	day = int(post_date[8:10]) # Делаем срез получая день
	post_date = datetime(year,month,day) # Подводим все в нужный вид
	period = today - post_date # Получаем разницу дней между сегодняшним днём и датой публикации

	if period.days > days: # Если последнему посту больше days дней - мы пропускаем этот профиль
		print(j, " Последняя публикация была слишком давно")
		continue

	# ДОБАВЛЕНИЕ ПОЛЬЗОВАТЕЛЯ В ОТФИЛЬТРОВАННЫЙ ФАЙЛ
	filtered_list.append(person)

	usr = person[26::]
	usr = ' '.join(usr)
	print("")
	print("--------------------------------------------------")
	print(j, " Добавлен новый пользователь", usr)

	user = filtered_list[index]

	filter_users.write(user)
	index += 1



# while True:
# 	Filter()









# filter_users = open("filter_users.txt", "a")
# for user in filtered_list:
# 	filter_users.write(user)
# filter_users.close()

# print("\nДобавлено", i , "пользователей")















# Запасной блок кода фильтрации. Проверка на закрытий аккаунт 

# # Берём людей со списка и проходимся по каждому 
# for user_link in users: # Итерационный цикл
#     browser.get(user_link) # Переход на страничку пользователя

#     # Фильтрация юзеров
#     try:
#     	# Проверка на закрытый аккаунт 
# 	    if browser.find_element_by_xpath('//section/main/div/div/article/div[1]/div/h2') == "Это закрытый аккаунт":
# 	        continue
#     except:
#     	filter_users.write(user_link) # Запись отфильтрированого пользователя в новый список
#     	schet += 1 # Дофига математичекое вычисление 
#     	print("Добавлен пользоатель № " + str(schet)) # Счётчик. Чисто для удобства
#     	time.sleep(1.5) # Ожидание 
#     users = users.replese(user_link, "") # Удаления пользователя со старого списка