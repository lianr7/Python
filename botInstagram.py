from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from botcity.core import DesktopBot
import time
import random

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
        '''
        login_button = driver.find_element_by_xpath(
            "//a[@href='/accounts/login/?source=auth_switcher']"
        )
        login_button.click()
        '''
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
        agora_nao = driver.find_element_by_class_name("cmbtv")
        agora_nao.click()
        self.comente_nas_fotos_com_a_hashtag()

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        """ Este código irá basicamente permitir que você simule a digitação como uma pessoa """
        print("Digitando comentário...")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(0,2))

    def comente_nas_fotos_com_a_hashtag(self):
        a = 0
        while (1):
            #link do sorteio aqui
            postComentar = "https://www.instagram.com/p/CeMlcMkPWkH/"
            ##Nessa lista de sorteios, você insere todos as variáveis que você criou acima.
            sorteios = [
                postComentar
            ]
            sorteio_da_vez = random.choice(sorteios)
            driver = self.driver
            time.sleep(5)
            driver.get(sorteio_da_vez)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            try:
                comments = [
                    "Muito foda, mano!",
                    "Você é inspiração!",
                    "Meu sonho!",
                    "Muito foda, mano!",
                    "Projetinho 2025",
                    "Dinheiro é liberdade!",
                    "Ansioso pela 2a",
                    "Parabéns, mano!",
                    "Que Deus abençoe sempre!",
                    "Vcs merecem!",
                    "Que fodaaaa",
                    "Imagino o orgulho que ela tá sentindo de ti",
                ]
                driver.find_element(By.XPATH, '//*[@id="mount_0_0_Mg"]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea').click()
                comment_input_box = driver.find_element(By.XPATH, '//*[@id="mount_0_0_Mg"]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')
                time.sleep(random.randint(1, 20))

                comentarioDaVez = random.choice(comments)

                if sorteio_da_vez == postComentar:
                    self.type_like_a_person(comentarioDaVez, comment_input_box)
                    print("Comentei: ", comentarioDaVez, " no post: ", sorteio_da_vez, "")

                time.sleep(random.randint(2, 8))
                driver.find_element(By.XPATH,
                    "//*[@id='mount_0_0_Mg']/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button/div"
                ).click()
                a = a + 1
                '''Aqui ele te informará quantas vezes já comentou o todo, desde o momento do start do script'''
                print('Vezes comentadas:')
                print(a)
                for i in range(1, 3): driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.randint(20, 45)) 
            except Exception as e:
                print(e)
                time.sleep(5)

# Entre com o usuário e senha aqui
#Dica amiga: Crie um instagram só para concorrer a sorteios...

sandroLucasBot = InstagramBot("", "")
sandroLucasBot.login()