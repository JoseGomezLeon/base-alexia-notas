import pytest

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
        if page:
            page.screenshot(path=f"screenshots/{item.name}.png")