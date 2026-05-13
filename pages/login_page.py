from utils.funciones import Funciones
import re

class LoginPage:

    def __init__(self, page):
        self.page = page
        self.funciones = Funciones()

    def navigate(self, url):
        self.page.goto(url)

    def username_input(self):
        return self.page.locator("#txtUsuario")

    def password_input(self):
        return self.page.locator("#txtPassword")

    def btn_ingresar(self):
        return self.page.locator("#btnAceptar")

    def user_logged_label(self, nombre):
        return self.page.get_by_text(nombre)

    def login(self, username, password):
        self.funciones.ingresar(self.username_input(), username)
        self.funciones.ingresar(self.password_input(), password)
        self.funciones.click(self.btn_ingresar())

    def menu_pruebas(self):
        return self.page.get_by_text("PRUEBAS", exact=False)
    
    def click_pruebas(self):
        self.funciones.click(self.menu_pruebas())

    def notas_aprobadas(self):
        return self.page.locator("em.nota_seguimiento.suspenso")


    def contar_notas_aprobadas(self):

        elementos = self.page.locator(".nota_seguimiento.suspenso")
        textos = elementos.all_inner_texts()
        numeros = [t for t in textos if re.match(r'^\d+(\.\d+)?$', t.strip())]
        return len(numeros)