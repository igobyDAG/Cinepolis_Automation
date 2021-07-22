from random import randint
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class CinepolisChrome:
    def __init__(self, base_url):
        self.base_url = base_url

    def setup_method(self):
        self.driver = webdriver.Chrome('../drivers/chromedriver')
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def open_page(self):
        print('Opening webpage: ',self.base_url)
        self.driver.get(self.base_url)

    def pop_up_wait_and_reload_method(self):
        sleep(2)
        self.driver.refresh()

    def select_ciudad(self):
        print('found xpath element - Ciudades')
        self.ciudades = self.driver.find_element(By.ID, "cmbCiudades")
        self.select_ciudades = Select(self.ciudades)
        options_ciudades = self.select_ciudades.options
        a_random_int = randint(1,len(options_ciudades)-1)
        print('Selecting City: ',options_ciudades[a_random_int].text)
        self.select_ciudades.select_by_index(a_random_int)

    def select_cine(self):
        cines = self.driver.find_element_by_id('cmbComplejos')
        select_cines = Select(cines)
        length_of_select_cines = len(select_cines.options)
        a_random_int = randint(1,length_of_select_cines-1)
        print('Selecting Movie Theater: ',select_cines.options[a_random_int].text)
        select_cines.select_by_index(a_random_int)
        sleep(3)

    def specify_horario(self):
        sliders = self.driver.find_elements_by_css_selector('a[class="ui-slider-handle ui-state-default ui-corner-all"]')
        print('Adjusting slider...')
        box1 = sliders[0]
        box2 = sliders[1]
        box_targets = self.driver.find_elements_by_css_selector('span[class*=ui-slider-pip]')
        box1_rand_index = randint(1, len(box_targets)-1)
        box1_target = box_targets[box1_rand_index]
        ActionChains(self.driver).drag_and_drop(box1, box1_target).perform()

        box2_rand_index = box1_rand_index + randint(1, (len(box_targets)-1 - box1_rand_index))
        box2_target = box_targets[box2_rand_index]
        ActionChains(self.driver).drag_and_drop(box2, box2_target).perform()
        sleep(5)


def main():
    tests = ['fullpage', 'slider']
    testing = tests[0]
    if testing == 'slider':
        cinepolis = CinepolisChrome('https://cinepolis.com/cartelera/monterrey-sur/cinepolis-nuevo-sur')
        cinepolis.setup_method()
        cinepolis.open_page()
        cinepolis.specify_horario()
    else:
        cinepolis = CinepolisChrome('https://cinepolis.com/')
        cinepolis.setup_method()
        cinepolis.open_page()
        cinepolis.pop_up_wait_and_reload_method()
        cinepolis.select_ciudad()
        cinepolis.select_cine()
        cinepolis.specify_horario()

    cinepolis.teardown_method()


if __name__ == "__main__":
    main()

# TODO Primera parte (llegar hasta el drag and drop de la selección de horario)
#  abrir pag de cinepolis.
#  cerrar la ventana inicial.
#  Seleccionar una ubicación del drop down al azar.
#  Seleccionar un cine del drop down al azar.
#  Seleccionar un horario con la barra slider.

#TODO Segunda  Parte
# En la pagina de la pelicula:
# validar los horarios
# Sinopsis
# que haya trailer
# y que tenga la seccion de recomendaciones
