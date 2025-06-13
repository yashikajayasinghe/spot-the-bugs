# spot-the-bugs

## Instructions to RUN in a Codespace:

- Create a Codespace on main
- `python3 -m venv .venv_playwright`
- `source .venv_playwright/bin/activate`
- `pip install -r requirements.txt`
- `playwright install` 
- `python -m pytest`

## CI Github Actions
- `.github/workflows/playwright.yaml`

### Issues Are Listed in: `issues.md`

### references:
- https://playwright.dev/python/docs/intro
- https://playwright.dev/python/docs/ci-intro
- https://playwright.dev/python/docs/locators 
- https://playwright.dev/python/docs/api/class-browsercontext
- https://playwright.dev/python/docs/ci-intro
- https://docs.pytest.org/en/6.2.x/fixture.html
