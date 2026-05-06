from pages.login_page import LoginPage
from playwright.sync_api import expect
import time

class LoginFlow:

    def __init__(self, page):
        self.login_page = LoginPage(page)

    def login(self, url, username, password):
        self.login_page.navigate(url)
        self.login_page.login(username, password)

    def validar_login_exitoso(self, nombre):
        expect(self.login_page.user_logged_label(nombre)).to_be_visible(timeout=10000)

    def ir_a_pruebas(self, nombre):
        expect(self.login_page.user_logged_label(nombre)).to_be_visible(timeout=10000)
        self.login_page.click_pruebas()

    def contar_aprobadas(self):
        cantidad = self.login_page.contar_notas_aprobadas()
        print(f"Se encontraron {cantidad} registros")
        return cantidad

    