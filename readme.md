# Запуск проекта на Selenium с использованием Python

Этот проект демонстрирует пример запуска тестов с использованием Selenium и Python.

## Установка

1. Убедитесь, что у вас установлен Python и pip.
2. Клонируйте репозиторий:

    ```sh
    git clone https://github.com/Vovashhh/plaginfortest.git
    ```

3. Создайте и активируйте виртуальное окружение (необязательно, но рекомендуется):

    ```sh
    python -m venv .venv
    source .venv/bin/activate  # для Linux/Mac
    .venv\Scripts\activate      # для Windows
    ```

4. Установите Selenium и другие зависимости (если они необходимы) с помощью pip:

    ```sh
    pip install selenium
    ``` 

5. Установить вспомогательный библиотеки
   ```sh
   pip install pyperclip
   pip install colorama
   ```

5. #### В файле var.py - можно задать переменные, в том числе для пути к плагину
   ### Для запуска нажать на Run в IDE 

___
### Блокеры:
1. Weblancer - блокер (капча)

---
### Шаблон проверки с учетом логина
```sh
def name_check():
driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlHabrNew)
        #тут проверка
    except NoSuchElementException as e:
        print(f"Test № failed: {e}")
    finally:
        driver.quit()
#Проверка 
```
### Конструкция для запуска тестов в случае их провала 

```sh 
if __name__ == "__main__":
    try:
        C3446_dzen_cyrkle_only_with_register()
    except Exception as e:
        print(f"Error running C3446: {e}")
```
### Конструкция для запуска тестов без постоянной логинизации
```sh
def C3467_usp_Moderation_btn(driver):
    try:
        # Проверка
    except NoSuchElementException as e:
        # Исключение
    return driver
```
```sh
if __name__ == "__main__":
    driver = None
    try:
        if driver is None:
            driver = setup_driver() #Если driver не был найден то выполняется логинизация
            navigate_and_login(driver)
        C3467_usp_Moderation_btn(driver)
    except Exception as e:
        print(Fore.RED + "Error running C3467: {e}" + Style.RESET_ALL)
```

#### Использование команды для ввода текста
<code>
    enter_text(driver, "ID", var.uspForm, "var.uspForm")
</code>

#### Использование команды для нажатия на селектор
<code>
    click_element(driver, "ID", var.uspModeration)
</code>

#### Использование команды для проверки формы на соответсвие
<code>
    verify_text_in_element(driver, "XPATH", var.regProjByMe, "Тут текст")
</code>

#### Использование команды для проверки что элемент пристутсвует на странице
<code>
      verify_element_present(driver, "CLASS_NAME", var.dzenHistoryTab)
</code>

#### Использование команды для проверки что элемент отсутсвует на странице
<code>
      verify_element_not_present(driver, "ID", var.uspModeration)
</code>
