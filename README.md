# QA Automation Framework – Playwright (Python)

---

[![Playwright Tests](https://github.com/robertMartin123/qa-automation-playwright/actions/workflows/playwright.yml/badge.svg)](https://github.com/robertMartin123/qa-automation-playwright/actions/workflows/playwright.yml)

## 👤 Author

Robert Martin  
Senior QA Engineer (Automation | Playwright | Python)

---

## 📌 Overview
This project is a professional-grade UI test automation framework built using Playwright and Pytest.

It demonstrates:
- Page Object Model (POM)
- Fixture-based architecture
- Test stability and debugging strategies
- CI/CD integration with GitHub Actions

---

## 🚀 Tech Stack
- Python
- Pytest
- Playwright
- GitHub Actions (CI/CD)

---

## 🧪 Features
- Modular Page Object Model design
- Reusable fixtures (browser, page, config)
- Automatic screenshots on failure
- Playwright tracing and video recording
- Parallel-ready structure
- CI pipeline with artifact collection

---
## 📊 Test Reporting  

The framework generates HTML test reports:

```bash
pytest --html=report.html --self-contained-html




## ⚡ Parallel Execution

The framework supports parallel test execution using pytest-xdist to improve performance and reduce runtime.

Run tests in parallel:

```bash
pytest -n auto





## 📊 Data-Driven Testing

The framework supports data-driven testing using Pytest parameterization.

Example:

```python
@pytest.mark.parametrize("username,password", get_login_data())





## 🔌 API Testing

The framework includes API testing using Playwright's request context:

- Supports REST API validation
- Integrated with Pytest markers
- Can be executed independently from UI tests

Run API tests:

```bash
pytest -m api


## ⚙️ How to Run Tests Locally

```bash
pip install -r requirements.txt
playwright install
pytest
