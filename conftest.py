import pytest
from utils.ai_helper import analizar_error  # 👈 nuevo

@pytest.fixture(scope="function")
def context_options():
    return {
        "viewport": {"width": 1280, "height": 720}
    }

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)

        # 📸 Screenshot (lo que ya tenías)
        if page:
            page.screenshot(path=f"screenshots/{item.name}.png")

        # 🤖 IA - análisis del error
        error_msg = str(rep.longrepr)
        analisis = analizar_error(error_msg)

        print("\n🤖 ===== ANÁLISIS IA =====")
        print(analisis)
        print("🤖 =======================\n")

def pytest_playwright_browser_type_launch_args():
    return {
        "headless": True
    }