# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys,ActionChains
from time import sleep

driver = webdriver.Chrome()
test_site = 'https://fix-online.sbis.ru/'
try:
    driver.get(test_site)
    sleep(1)
    assert driver.title == 'Вход в личный кабинет'
    print('Авторизоваться на сайте https://fix-online.sbis.ru/')
    user_login, user_password = 'wawa', '112255GiG'
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(user_login, Keys.ENTER)
    assert login.get_attribute('value') == user_login
    sleep(1)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password, Keys.ENTER)
    sleep(6)
    print('Перейти в реестр Контакты')
    kontact_el = driver.find_element(By.CSS_SELECTOR, '[name="item-contacts"] .NavigationPanels-Accordion__title')
    kontact_el.click()
    sleep(6)
    kontact_el1 = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle')
    kontact_el1.click()
    sleep(6)
    plus_el = driver.find_element(By.CSS_SELECTOR, '[data-name="sabyPage-addButton"]')
    plus_el.click()
    sleep(3)
    poisk_el = driver.find_element(By.CSS_SELECTOR, '[name="ws-input_2023-06-21"]')
    FIO = "Рафальский"
    poisk_el.send_keys(FIO, Keys.ENTER)
    sleep(3)
    print('Отправить сообщение самому себе')
    kontact_el4 = driver.find_element(By.CSS_SELECTOR, '.msg-addressee-selector__addressee')
    kontact_el4.click()
    sleep(3)
    vvod_txt = driver.find_element(By.CSS_SELECTOR, '[role="textbox"]')
    sms ='Привет Саня'
    vvod_txt.send_keys(sms)
    sleep(3)
    otpr_btn = driver.find_element(By.CSS_SELECTOR, '[title="Отправить"]')
    otpr_btn.click()
    sleep(4)
    messages = driver.find_elements(By.CSS_SELECTOR, '.msg-entity-text')
    assert messages[0].text == sms
    print('Поиск сообщения на странице')
    action_chains = ActionChains(driver)
    action_chains.move_to_element(messages[0])
    action_chains.context_click(messages[0])
    action_chains.perform()
    sleep(2)
    delete_btn = driver.find_element(By.CSS_SELECTOR, '.controls-Menu__row [title="Перенести в удаленные"]')
    delete_btn.click()
    sleep(2)
    print('Убедиться, что сообщение удалилось')
    assert driver.find_elements(By.CSS_SELECTOR, '.msg-entity-text')[0].text != sms, 'Сообщение не удалили'
    print('Все ок')
finally:
    driver.quit()
sleep(5)