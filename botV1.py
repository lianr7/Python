from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

# Fiz algumas modificações


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path=r"C:\Users\Lian Rodrigues\Desktop\geckodriver.exe"
        )

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        user_element = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(3)
        password_element = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(3)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        self.comenteNoPost(
            "calisteniabrasil"
        )  # Altere aqui para a hashtag que você deseja usar.

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 5) / 30)

    def comente_nas_fotos_com_a_hashtag(self):
        driver = self.driver
        driver.get("https://www.instagram.com/p/CeMi3jQAs6S/")

        try:
            comments = [
                "Muito foda, mano!",
                "Você é inspiração!",
                "Meu sonho fazer isso um dia! Projetinho 2025",
                "Muito foda, mano!",
                "Dinheiro é liberdade!",
                "Tô ansioso pela aula 2",
                "Parabéns, mano! Que Deus abençoe muito",
                "Vocês merecem!",
                "Que fodaaaa",
                "Imagino o orgulho que ela tá sentindo de ti",
                "Parece que todo sofrimento valeu a pena, hein! Dando um orgulho enorme",
            ]  # Remova esses comentários e insira os seus comentários aqui
            driver.find_element_by_class_name("Ypffh").click()
            comment_input_box = driver.find_element_by_class_name("Ypffh")
            time.sleep(random.randint(8, 15))
            self.type_like_a_person(
                random.choice(comments), comment_input_box)
            time.sleep(random.randint(3, 5))
            driver.find_element_by_link_text('Publicar'
            ).click()
            time.sleep(random.randint(3, 5))
        except Exception as e:
            print(e)
            time.sleep(5)


# Entre com o usuário e senha aqui
jhonatanBot = InstagramBot("", "")
jhonatanBot.login()