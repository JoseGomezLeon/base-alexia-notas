import os
import pytest
from utils.ai_helper import analizar_error


@pytest.fixture(scope="function")
def context_options():
    return {
        "viewport": {"width": 1280, "height": 720}
    }


# ✅ Playwright headless para GitHub Actions
@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {
        "headless": True
    }


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)

        # 📸 Screenshot
        if page:
            os.makedirs("screenshots", exist_ok=True)

            page.screenshot(
                path=f"screenshots/{item.name}.png"
            )

        # 🤖 IA análisis error
        error_msg = str(rep.longrepr)
        analisis = analizar_error(error_msg)

        print("\n🤖 ===== ANÁLISIS IA =====")
        print(analisis)
        print("🤖 =======================\n")