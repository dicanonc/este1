import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from pprint import pprint
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from kivymd.app import MDApp
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from kivymd.uix.screen import Screen
from kivy.lang import  Builder
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import kivy
kivy.require('2.0.0') # replace with your current kivy version !


username_helper = """
MDTextField:
 hint_text : "Usuario"
 helper_text: "Ingresa el usuario con el que ingresas al SIA"
 helper_text_mode:"on_focus"
 pos_hint : {'center_x' : 0.5, 'center_y': 0.7}
 size_hint_x:None
 width:300
 
"""
password_helper="""
MDTextField:    
 hint_text : "Contraseña"
 helper_text: "Ingresa la contraseña con la que ingresas al SIA"
 helper_text_mode:"on_focus"
 password: True
 pos_hint : {'center_x' : 0.5, 'center_y': 0.6}
 size_hint_x:None
 width:300
"""



class FirstKivy(MDApp):

    def build(self):
        screen = Screen()
        self.username = Builder.load_string(username_helper)
        self.password = Builder.load_string(password_helper)
        submit = MDRaisedButton(text=" Iniciar Sesion ", pos_hint={'center_x' : 0.5, 'center_y': 0.5}, size_hint=(0.15,0.055), on_press=self.printpress, on_release=self.printrelease)
        screen.add_widget(self.username)
        screen.add_widget(self.password)
        screen.add_widget(submit)
        return screen

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def close_dialog1(self, obj):
        self.dialog1.dismiss()

    def printpress(self, obj):
        user = self.username.text

    def printrelease(self, obj):
        pas = self.password.text
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        pag = webdriver.Chrome(executable_path=r"C:\Users\diego\Documents\chromedriver.exe",chrome_options=options)
        pag.get("https://sia.unal.edu.co/ServiciosApp")

        # variables de llenado y busqueda de campos
        pin = pag.find_element_by_name("password")
        pin.clear()
        pin.send_keys(self.password.text)
        user = pag.find_element_by_name("username")
        user.clear()
        user.send_keys(self.username.text)
        acceder = pag.find_element_by_name("submit")
        acceder.click()
        #busqueda de informacion
        wait = WebDriverWait(pag, 5)
        try:
         wait.until(EC.presence_of_element_located((By.ID, 'pt1:men-portlets:sdi::head')))
        except:
           close_button=MDFlatButton(text="cerrar", on_release=self.close_dialog)
           self.dialog=MDDialog(title="Error en las credenciales de incio",text="Deja de ser huevon y escribe bien esa monda"
                           ,size_hint=(0.7,1), buttons=[close_button])
           self.dialog.open()
        else:
            dat = pag.find_element_by_id("pt1:men-portlets:sdi::head")
            dat.click()
            element = wait.until(EC.element_to_be_clickable((By.ID, 'pt1:men-portlets:sdi')))
            element.click()
            name = wait.until(EC.presence_of_element_located((By.ID, 'pt1:r1:1:ot4::content')))
            name = pag.find_element_by_id("pt1:r1:1:ot4::content").text
            print(name)
            cc = pag.find_element_by_id("pt1:r1:1:ot1::content").text
            print(cc)
            dat = pag.find_element_by_id("pt1:men-portlets:j_idt1::head")
            dat.click()
            element = wait.until(EC.element_to_be_clickable((By.ID, 'pt1:men-portlets:j_idt8')))
            element.click()

        finally:
            close_button1 = MDFlatButton(text="cerrar", on_release=self.close_dialog1)
            self.dialog1 = MDDialog(title="Datos",
                                   text=name + cc
                                   , size_hint=(0.7, 1), buttons=[close_button1])
            self.dialog1.open()







FirstKivy().run()

