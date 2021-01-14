from selenium import webdriver as wd
from selenium.webdriver.common.action_chains import ActionChains

d = wd.Chrome()
d.get('https://sbis.ru/')

# Ищу кнопку "Поддержка"
support_field = d.find_element_by_css_selector("[href='/support']").click()

# Ищу кнопку "Скачать" поскролив экран
ActionChains(d).move_to_element(d.find_element_by_css_selector("[href='/download']")).perform()
d.find_element_by_css_selector("[href='/download']").click()

# Ищу кнопки на странице, чтобы записать в файл
x = d.find_element_by_css_selector("[href='https://update.sbis.ru/version25/sbis-setup-eo-inst.exe']")
x.get_attribute('href')

x_2 = d.find_element_by_css_selector("[href='https://update.sbis.ru/version25/sbis-update-eo.exe']")
x_2.get_attribute('href')

x_3 = d.find_element_by_css_selector("[href='https://update.sbis.ru/version25/jinneeupdate.exe']")
x_3.get_attribute('href')

x_4 = d.find_element_by_css_selector("[href='https://update.sbis.ru/download/pdf417/print_pdf417.msi']")
x_4.get_attribute('href')

x_5 = d.find_element_by_css_selector("[href='https://update.sbis.ru/download/shabl/shabl.zip']")
x_5.get_attribute('href')


# Открываю файл на запись и поочередно записываю
with open('file_for_links.txt', 'w', encoding='utf-8') as f:
    for i in x.get_attribute('href'):
        f.write(i)

    f.write('\n')

    for i in x_2.get_attribute('href'):
        f.write(i)

    f.write('\n')

    for i in x_3.get_attribute('href'):
        f.write(i)

    f.write('\n')

    for i in x_4.get_attribute('href'):
        f.write(i)

    f.write('\n')

    for i in x_5.get_attribute('href'):
        f.write(i)


