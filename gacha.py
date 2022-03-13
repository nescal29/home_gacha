from get_area_link import get_area_link
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup, ResultSet
import random

class WebDriverConfig:
  def __init__(self):
    options = Options()
    options.add_argument('--headless')
    self.driver = webdriver.Chrome("chromedriver.exe", options=options)

  def get(self, link: str, link_format: str) -> str:
    tmp_link = link.format(link_format)
    self.driver.get(link.format(link_format))
    self.driver.implicitly_wait(10)
    return self.driver.page_source

  def quit(self) -> None:
    self.driver.quit()


def get_input_areas() -> list[str]:
  area: str = input('エリアを入力してください。　例）北海道　道央\n')
  return area.split('　')

def get_link(areas: list[str]) -> str:
  if len(areas) == 1:
    return get_area_link(areas[0])
  
  return get_area_link(areas[0], areas[1])

def get_elements(html: str, selector: str) -> ResultSet:
  soup: BeautifulSoup = BeautifulSoup(html, 'html.parser')
  return soup.select(selector)

def gacha():
  areas: list[str] = get_input_areas()
  link: str = get_link(areas)

  driver: WebDriverConfig = WebDriverConfig()
  html: str = driver.get(link, '')

  count_elements: ResultSet = get_elements(html,'#contents>div.mT20>span')
  count_str: str = count_elements[0].text
  count: int = int(count_str.replace('件', ''))
  page_num = count//20+1
  
  page_index: int = random.randint(1, page_num)

  link_format: str = ''
  if page_index != 1:
    link_format = 'p_' + str(page_index) + '/'

  html = driver.get(link, link_format)
  driver.quit()

  home_elements: ResultSet = get_elements(html, '[class="fs16"]>a')
  home_index: int = random.randint(0, len(home_elements)-1)
  home_name: str = home_elements[home_index].text
  home_link: str = home_elements[home_index].attrs['href']

  print(home_name, 'https://suumo.jp/' + home_link)



if __name__ == '__main__':
  gacha()