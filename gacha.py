from get_link import get_link
import random

def gacha():
  area: str = input('エリアを入力してください。　例）北海道　道央\n')
  areas: list[str] = area.split('　')

  link: str = ''
  if len(areas) == 1:
    link = get_link(areas[0])
  else:
    link = get_link(areas[0], areas[1])

  print(link)


if __name__ == '__main__':
  gacha()
