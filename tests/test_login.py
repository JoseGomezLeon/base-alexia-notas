from business.login_flow import LoginFlow
from data.login_data import login_data

def test_login_exitoso(page):

    flow = LoginFlow(page)

    flow.login(login_data["url"],login_data["user"],login_data["password"])
    flow.validar_login_exitoso(login_data["expected_user"])
    flow.ir_a_pruebas(login_data["expected_user"])
    cantidad = flow.contar_aprobadas()
    assert cantidad > 0