

# МОДЕРНИЗАЦИЯ НИКОВ В ВИД ССЫЛКИ НА ПРОФИЛЬ
old_list = open("person.txt", 'r')
new_list = open("users.txt", "w")
for i in old_list:
	user_link = ("https://www.instagram.com/" + i)
	new_list.write(user_link)