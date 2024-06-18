import time
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from chrome_driver_utils import chrome_with_extension, click_element, login_and_waitF, enter_text, verify_element_present, verify_element_not_present, verify_text_in_element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import var
import pyperclip
from colorama import init, Fore, Style

expected_text_login = "Найти задание/вакансию"
expected_unauthorized_text = "Вы не авторизованы, авторизируйтесь"


# Добавление плагина в браузер
def setup_driver():
    return chrome_with_extension(var.pathToPlagin)
def navigate_and_login(driver):
    driver.get(var.urlFreelancer)
    driver.refresh()
    login_and_waitF(driver)  # Вход под менеджером


# Тест - Автовход
def C3538_auto_enter():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        expected_dashboard_url = "https://www.freelancer.com/dashboard"
        actual_url = driver.current_url
        assert actual_url == expected_dashboard_url, (f"URL после автовхода не соответствует ожидаемому.")
        print(Fore.GREEN + "C3538 успешно выполнен - Пользователь может войти в аккаунт биржи нажав на кнопку 'Автовход'" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3538 failed: {e}")
    finally:
        driver.quit()
# Тест - Автовход по сессии
def C3539_auto_enter_session():
    driver = setup_driver()
    try:
        driver.get(var.urlFreelancer)
        driver.refresh()
        time.sleep(2)
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.LinkElement[href='/login']"))
        )
        login_button.click()
        time.sleep(5)
        # Клик по автовходу по сессии
        click_element(driver, "XPATH", var.sessionLogin)
        time.sleep(5)
        expected_dashboard_url = "https://www.freelancer.com/dashboard"
        actual_url = driver.current_url
        assert actual_url == expected_dashboard_url, (f"URL после автовхода не соответствует ожидаемому.")
        print(Fore.GREEN + "C3539 успешно выполнен - Пользователь может войти в аккаунт биржи нажав на кнопку 'Автовход по сессии'" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3539 failed: {e}")
    finally:
        driver.quit()
# Тест - При нажатии на колокольчик открывается панель уведомлений
def C3482_notification_open():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        #Открытие колокольчика
        click_element(driver, "CSS_SELECTOR", var.alertBellBut)
        #Проверка наличия панели уведомлений
        verify_element_present(driver, "CLASS_NAME", var.bellForm)
        # Закрытие колокольчик
        click_element(driver, "CSS_SELECTOR", var.alertBellBut)
        print(Fore.GREEN + "C3482 успешно выполнен - При нажатии на колокольчик открывается панель уведомлений" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3482 failed: {e}")
    finally:
        driver.quit()
# Тест - Пользователь может посмотреть информацию о клиенте
def C3542_client():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlFreelancerRegMe)
        click_element(driver, "ID", var.clientInfoBtn, "5")
        verify_element_present(driver, "CLASS_NAME", var.clientIcon, "5")
        print(Fore.GREEN + "C3542 успешно выполнен - Пользователь может посмотреть информацию о клиенте" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3542 failed: {e}")
    finally:
        driver.quit()
# Тест - В информации о клиенте - отображается количество активных переписок
def C3568_client_act_mess():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlFreelancerRegMe)
        click_element(driver, "ID", var.clientInfoBtn, "5")
        verify_element_present(driver, "XPATH", var.reqStestProgress)
        print(Fore.GREEN + "C3568 успешно выполнен - В информации о клиенте - отображается количество активных переписок" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3568 failed: {e}")
    finally:
        driver.quit()
# Тест - В информации о клиенте - отображается количество успешных сделок
def C3569_client_comp():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlFreelancerRegMe)
        click_element(driver, "ID", var.clientInfoBtn, "5")
        verify_element_present(driver, "XPATH", var.compByDeal)
        print(Fore.GREEN + "C3569 успешно выполнен - В информации о клиенте - отображается количество успешных сделок" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3569 failed: {e}")
    finally:
        driver.quit()
# Тест - В информации о клиенте - отображается количество не успешных сделок
def C3570_client_close():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlFreelancerRegMe)
        click_element(driver, "ID", var.clientInfoBtn, "5")
        verify_element_present(driver, "XPATH", var.closedReason)
        print(Fore.GREEN + "C3570 успешно выполнен - В информации о клиенте - отображается количество не успешных сделок" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3570 failed: {e}")
    finally:
        driver.quit()
# Тест - Информация о клиенте скрыта для существующего клиента - если нет комментария
def C3566_info_hidden_without_comment():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlFreelancerRegMe)
        click_element(driver, "ID", var.clientInfoBtn, "5")
        verify_element_present(driver, "CLASS_NAME", var.clientIcon, "5")
        print(Fore.GREEN + "C3566 успешно выполнен - Информация о клиенте скрыта для существующего клиента - если нет комментария" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3573 failed: {e}")
    finally:
        driver.quit()
# Тест - Менеджер не может заполнить комментарий к заказчику пробелами
def C3586_client_comment_cannot_with_spaces():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlFreelancerRegMe)
        click_element(driver, "ID", var.clientInfoBtn)
        click_element(driver, "CLASS_NAME", var.commentBtn)
        enter_text(driver, "ID", var.commentForm, "     ")
        # Проверяем что кнопка "Сохранить" задизейблена
        usp_send_button = driver.find_element(By.CLASS_NAME, var.saveClient)
        assert not usp_send_button.is_enabled(), "Кнопка 'Сохранить' должна быть неактивна"
        print(Fore.GREEN + "C3586 успешно выполнен - Менеджер не может заполнить комментарий к заказчику пробелами" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3586 failed: {e}")
    finally:
        driver.quit()
# Тест - Менеджер при нажатии на карандаш может добавить описание
def C3573_client_comment():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlFreelancerRegMe)
        click_element(driver, "ID", var.clientInfoBtn, "5")
        click_element(driver, "CLASS_NAME", var.commentBtn)
        enter_text(driver, "ID", var.commentForm, "Comment 1")
        click_element(driver, "CLASS_NAME", var.saveClient)
        # Проверяем что введенный текст отображается правильно
        entered_text = driver.find_element(By.ID, var.commentForm).get_attribute("value")
        assert entered_text == "Comment 1", "Введенный текст не соответствует ожидаемому"
        print(Fore.GREEN + "C3573 успешно выполнен - Менеджер при нажатии на карандаш может добавить описание" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3573 failed: {e}")
    finally:
        driver.quit()
# Тест - Информация о клиенте раскрытая для существующего клиента - если есть комментарий
def C3567_info_disclosed_with_comment():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlFreelancerRegMe)
        verify_element_present(driver, "CLASS_NAME", var.clientIcon)
        print(Fore.GREEN + "C3567 успешно выполнен - Информация о клиенте раскрытая для существующего клиента - если есть комментарий" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3567 failed: {e}")
    finally:
        driver.quit()
# Тест - Менеджер может редактировать описание
def C3574_client_comment_redact():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlFreelancerRegMe)
        click_element(driver, "CLASS_NAME", var.commentBtn)
        enter_text(driver, "ID", var.commentForm, "Comment Redact")
        click_element(driver, "CLASS_NAME", var.saveClient)
        # Проверяем что введенный текст отображается правильно
        entered_text = driver.find_element(By.ID, var.commentForm).get_attribute("value")
        assert entered_text == "Comment Redact", "Введенный текст не соответствует ожидаемому"
        print(Fore.GREEN + "C3574 успешно выполнен - Менеджер может редактировать описание" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3574 failed: {e}")
    finally:
        driver.quit()
# Тест - Менеджер может удалить описание
def C3575_client_comment_del():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlFreelancerRegMe)
        click_element(driver, "CLASS_NAME", var.commentBtn)
        enter_text(driver, "ID", var.commentForm, "1")
        enter_text(driver, "ID", var.commentForm, "")
        click_element(driver, "CLASS_NAME", var.saveClient)
        entered_text = driver.find_element(By.ID, var.commentForm).get_attribute("value")
        assert entered_text == "", "Текст в поле для ввода не был удален"
        print(Fore.GREEN + "C3575 успешно выполнен - Менеджер может удалить описание" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3575 failed: {e}")
    finally:
        driver.quit()
# Тест - При нажатии на глазик открывается форма отправки УТП для проверки дежурному
def C3466_usp_Moderation():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlFreelancerRegMe)
        click_element(driver, "ID", var.uspModeration)
        # Поиск формы для отправки УТП
        verify_element_present(driver, "ID", var.uspForm)
        enter_text(driver, "ID", var.uspForm, "УТП на проверку")
        click_element(driver, "CLASS_NAME", var.uspSend)
        print(Fore.GREEN + "C3466 успешно выполнен - При нажатии на глазик открывается форма отправки УТП для проверки дежурному" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3466 failed: {e}")
    finally:
        driver.quit()
# Тест - Кнопка "Отправить" задизейбленна пока не введутся символы в форму
def C3467_usp_Moderation_btn():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlFreelancerRegMe)
        click_element(driver, "ID", var.uspModeration)
        usp_send_button = driver.find_element(By.CLASS_NAME, var.uspSend)
        assert not usp_send_button.is_enabled(), "Кнопка отправки должна быть неактивна"
        enter_text(driver, "ID", var.uspForm, "Тест УТП на модерацию")
        click_element(driver, "CLASS_NAME", var.uspSend)
        print(Fore.GREEN + "C3467 успешно выполнен - Кнопка 'Отправить' задизейбленна пока не введутся символы в форму" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3467 failed: {e}")
    finally:
        driver.quit()
# Тест - После отправки УТП глазик пропадает, становится недоступным
def C3469_usp_not_available():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlFreelancerRegNotMeSendUSP)
        time.sleep(5) #Пауза чтобы закрыть уведомление
        verify_element_not_present(driver, "ID", var.uspModeration)
        print(Fore.GREEN + "C3469 успешно выполнен - После отправки УТП глазик пропадает, становится недоступным" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3469 failed: {e}")
    finally:
        driver.quit()
# Тест - Когда кнопка сообщения обведена красным кругом - есть не прочитанное сообщение от клиента
def C3470_mess_btn_red():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlFreelancerRegNotMeSendUSP)
        time.sleep(5)  # Пауза чтобы закрыть уведомление
        button = driver.find_element(By.ID, var.messegeBtn)
        style = button.get_attribute("style")
        assert "border-color: red" in style, "Кнопка не обведена красным кругом"
        print(Fore.GREEN + "C3470 успешно выполнен - Когда кнопка сообщения обведена красным кругом - есть не прочитанное сообщение от клиента" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3470 failed: {e}")
    finally:
        driver.quit()
# Тест - Палец вверх отображается в чате с клиентом, для отметки что сообщение не требует ответа
def C3476_message_thumb_up():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlFreelancerRegNotMeSendUSP)
        time.sleep(5)
        click_element(driver, "ID", var.messegeBtn)
        driver.switch_to.window(driver.window_handles[-1])
        # Находим елемент "Палец вверх"
        verify_element_present(driver, "ID", var.msgThumbUp)
        # Нажимаем на палец вверх
        click_element(driver, "ID", "btn-message-without-answer")
        print(Fore.GREEN + "C3476 успешно выполнен - Палец вверх отображается в чате с клиентом, для отметки что сообщение не требует ответа" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3476 failed: {e}")
    finally:
        driver.quit()
# Тест - Когда кнопка сообщения обведена зеленым - на все сообщения есть ответ , при клике по ней - переход в переписку по проекту
def C3472_mess_btn_green():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlFreelancerRegNotMeSendUSP)
        time.sleep(5)  # Пауза чтобы закрыть уведомление
        button = driver.find_element(By.ID, var.messegeBtn)
        style = button.get_attribute("style")
        assert "border-color: green" in style, "Кнопка не обведена зеленым кругом"
        click_element(driver, "ID", var.messegeBtn)
        # Переключение на новую вкладку
        driver.switch_to.window(driver.window_handles[-1])
        assert "messages" in driver.current_url, "URL не содержит текст 'messages'"
        print(Fore.GREEN + "C3470 успешно выполнен - Когда кнопка сообщения обведена зеленым - на все сообщения есть ответ, при клике по ней - переход в переписку по проекту" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3470 failed: {e}")
    finally:
        driver.quit()
# Тест - При нажатии на карандаш, открывается форма модерации сообщения
def C3473_message_moderation_form():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlFreelancerRegNotMeSendUSP)
        time.sleep(5)
        click_element(driver, "ID", var.messegeBtn)
        # Переключение на новую вкладку
        driver.switch_to.window(driver.window_handles[-1])
        click_element(driver, "ID", var.msgSendForm)
        verify_element_present(driver, "ID", var.msgForm)
        print(Fore.GREEN + "C3473 успешно выполнен - При нажатии на карандаш, открывается форма модерации сообщения" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3473 failed: {e}")
    finally:
        driver.quit()
# Тест - Кнопка "Отправить" задизейбленна пока не заполнена форма карандаша для отправки дежурному
def C3474_message_moderation_btn():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlFreelancerRegNotMeSendUSP)
        time.sleep(5)
        click_element(driver, "ID", var.messegeBtn)
        # Переключение на новую вкладку
        driver.switch_to.window(driver.window_handles[-1])
        click_element(driver, "ID", var.msgSendForm)
        # Проверяем что кнопка "Отправить" задизейблена
        usp_send_button = driver.find_element(By.CLASS_NAME, var.msgSendModerate)
        assert not usp_send_button.is_enabled(), "Кнопка отправки должна быть неактивна"
        enter_text(driver, "ID", var.msgForm, "Текст сообщения для проверки дежурному")
        # Проверяем что кнопка "Отправить" активна
        assert usp_send_button.is_enabled(), "Кнопка отправки должна быть активна"
        print(Fore.GREEN + "C3474 успешно выполнен - Кнопка 'Отправить' задизейбленна пока не заполнена форма карандаша для отправки дежурному" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3474 failed: {e}")
    finally:
        driver.quit()
# Тест - При отправке сообщения на модерацию оно приходит дежурному менеджеру
def C3475_message_moderation_send():
    driver = setup_driver()
    try:
        navigate_and_login(driver)
        driver.get(var.urlFreelancerRegNotMeSendUSP)
        time.sleep(5)
        click_element(driver, "ID", var.messegeBtn)
        # Переключение на новую вкладку
        driver.switch_to.window(driver.window_handles[-1])
        click_element(driver, "ID", var.msgSendForm)
        enter_text(driver, "ID", var.msgForm, "Текст сообщения для проверки дежурному")
        click_element(driver, "CLASS_NAME", var.msgSendModerate)
        print(Fore.GREEN + "C3475 успешно выполнен - При отправке сообщения на модерацию оно приходит дежурному менеджеру" + Style.RESET_ALL)
    except NoSuchElementException as e:
        print(f"Test C3475 failed: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    try:
        C3538_auto_enter()
    except Exception as e:
        print(Fore.RED + f"Error running C3538: {e}" + Style.RESET_ALL)

    try:
        C3539_auto_enter_session()
    except Exception as e:
        print(Fore.RED + f"Error running C3539: {e}" + Style.RESET_ALL)

    try:
        C3482_notification_open()
    except Exception as e:
        print(Fore.RED + "Error running C3482: {e}" + Style.RESET_ALL)

    try:
        C3542_client()
    except Exception as e:
        print(Fore.RED + f"Error running C3542: {e}" + Style.RESET_ALL)

    try:
        C3568_client_act_mess()
    except Exception as e:
        print(Fore.RED + f"Error running C3568: {e}" + Style.RESET_ALL)

    try:
        C3569_client_comp()
    except Exception as e:
        print(Fore.RED + f"Error running C3569: {e}" + Style.RESET_ALL)

    try:
        C3570_client_close()
    except Exception as e:
        print(Fore.RED + f"Error running C3570: {e}" + Style.RESET_ALL)

    try:
        C3566_info_hidden_without_comment()
    except Exception as e:
        print(Fore.RED + f"Test C3566 failed: {e}" + Style.RESET_ALL)

    try:
        C3586_client_comment_cannot_with_spaces()
    except Exception as e:
        print(Fore.RED + f"Test C3586 failed: {e}" + Style.RESET_ALL)

    try:
        C3573_client_comment()
    except Exception as e:
        print(Fore.RED + f"Error running C3573: {e}" + Style.RESET_ALL)

    try:
        C3567_info_disclosed_with_comment()
    except Exception as e:
        print(Fore.RED + f"Test C3567 failed: {e}" + Style.RESET_ALL)

    try:
        C3574_client_comment_redact()
    except Exception as e:
        print(Fore.RED + f"Error running C3574: {e}" + Style.RESET_ALL)

    try:
        C3575_client_comment_del()
    except Exception as e:
        print(Fore.RED + f"Error running C3575: {e}" + Style.RESET_ALL)

    try:
        C3466_usp_Moderation()
    except Exception as e:
        print(Fore.RED + f"Test C3466 failed: {e}" + Style.RESET_ALL)

    try:
        C3467_usp_Moderation_btn()
    except Exception as e:
        print(Fore.RED + f"Test C3467 failed: {e}" + Style.RESET_ALL)

    try:
        C3469_usp_not_available()
    except Exception as e:
        print(Fore.RED + f"Test C3469 failed: {e}" + Style.RESET_ALL)

    try:
        C3470_mess_btn_red()
    except Exception as e:
        print(Fore.RED + f"Test C3470 failed: {e}" + Style.RESET_ALL)

    try:
        C3476_message_thumb_up()
    except Exception as e:
        print(Fore.RED + f"Test C3476 failed: {e}" + Style.RESET_ALL)

    try:
        C3472_mess_btn_green()
    except Exception as e:
        print(Fore.RED + f"Test C3472 failed: {e}" + Style.RESET_ALL)

    try:
        C3473_message_moderation_form()
    except Exception as e:
        print(Fore.RED + f"Test C3473 failed: {e}" + Style.RESET_ALL)

    try:
        C3474_message_moderation_btn()
    except Exception as e:
        print(Fore.RED + f"Test C3474 failed: {e}" + Style.RESET_ALL)

    try:
        C3475_message_moderation_send()
    except Exception as e:
        print(Fore.RED + f"Test C3475 failed: {e}" + Style.RESET_ALL)
