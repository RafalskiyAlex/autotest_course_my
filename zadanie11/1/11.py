# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
sbis_site = 'https://test.sbis.ru/'
tensor_site = 'https://tensor.ru/about'
try:
    driver.get(sbis_site)
    contact_btn = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item [href="/contacts"]')
    contact_btn.click()
    sleep(3)
    baner_btn =driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor[title = "tensor.ru"]')
    assert baner_btn.is_displayed()
    baner_btn.click()
    driver.switch_to.window(driver.window_handles[1])
    new_btn=driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content')
    assert new_btn.is_displayed()
    sleep(4)
    news_block = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-Index__card-title')
    news_block_txt = 'Сила в людях'
    assert news_block.text == news_block_txt
    assert news_block.is_displayed()
    detailed_btn = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-link')
    driver.execute_script("return arguments[0].scrollIntoView(true);", detailed_btn)
    detailed_btn.click()
    sleep(3)
    assert driver.current_url == tensor_site, 'Неверно открыт сайт'
    sleep(3)
finally:
    driver.quit()