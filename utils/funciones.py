from playwright.sync_api import expect

class Funciones:

    def ingresar(self, locator, texto):
        locator.fill(texto)

    def click(self, locator):
        locator.click()

    def validar_visible(self, locator, timeout=10000):
        expect(locator).to_be_visible(timeout=timeout)