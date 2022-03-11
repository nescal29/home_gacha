import random

def get_link(area1: str, area2: str ='') -> str:
  hokkaido: dict[str, str] = {
    '道央': 'https://suumo.jp/library/tf_01/sc/?sc%5B%5D=01101&sc%5B%5D=01102&sc%5B%5D=01103&sc%5B%5D=01104&sc%5B%5D=01105&sc%5B%5D=01106&sc%5B%5D=01107&sc%5B%5D=01108&sc%5B%5D=01109&sc%5B%5D=01110&sc%5B%5D=01203&sc%5B%5D=01205&sc%5B%5D=01209&sc%5B%5D=01210&sc%5B%5D=01213&sc%5B%5D=01215&sc%5B%5D=01216&sc%5B%5D=01217&sc%5B%5D=01218&sc%5B%5D=01222&sc%5B%5D=01224&sc%5B%5D=01225&sc%5B%5D=01226&sc%5B%5D=01227&sc%5B%5D=01228&sc%5B%5D=01230&sc%5B%5D=01231&sc%5B%5D=01233&sc%5B%5D=01234&sc%5B%5D=01235&sc%5B%5D=01300&sc%5B%5D=01360&sc%5B%5D=01365&sc%5B%5D=01370&sc%5B%5D=01375&sc%5B%5D=01380&sc%5B%5D=01385&sc%5B%5D=01390&sc%5B%5D=01395&sc%5B%5D=01400&sc%5B%5D=01410&sc%5B%5D=01415&sc%5B%5D=01420&sc%5B%5D=01430&sc%5B%5D=01500&sc%5B%5D=01505&sc%5B%5D=01510&sc%5B%5D=01515&sc%5B%5D=01520&sc%5B%5D=01525&sc%5B%5D=01530&sc%5B%5D=01535',
    '道東': 'https://suumo.jp/library/tf_01/sc/?sc%5B%5D=01206&sc%5B%5D=01207&sc%5B%5D=01208&sc%5B%5D=01211&sc%5B%5D=01219&sc%5B%5D=01223&sc%5B%5D=01435&sc%5B%5D=01480&sc%5B%5D=01485&sc%5B%5D=01490&sc%5B%5D=01495&sc%5B%5D=01540&sc%5B%5D=01545&sc%5B%5D=01550&sc%5B%5D=01555&sc%5B%5D=01560&sc%5B%5D=01565&sc%5B%5D=01570&sc%5B%5D=01575&sc%5B%5D=01580&sc%5B%5D=01585&sc%5B%5D=01590&sc%5B%5D=01595&sc%5B%5D=01600',
    '道南': 'https://suumo.jp/library/tf_01/sc/?sc%5B%5D=01202&sc%5B%5D=01236&sc%5B%5D=01305&sc%5B%5D=01310&sc%5B%5D=01315&sc%5B%5D=01320&sc%5B%5D=01325&sc%5B%5D=01330&sc%5B%5D=01335&sc%5B%5D=01340&sc%5B%5D=01345&sc%5B%5D=01350&sc%5B%5D=01355',
    '道北': 'https://suumo.jp/library/tf_01/sc/?sc%5B%5D=01204&sc%5B%5D=01212&sc%5B%5D=01214&sc%5B%5D=01220&sc%5B%5D=01221&sc%5B%5D=01229&sc%5B%5D=01405&sc%5B%5D=01425&sc%5B%5D=01440&sc%5B%5D=01445&sc%5B%5D=01450&sc%5B%5D=01455&sc%5B%5D=01460&sc%5B%5D=01465&sc%5B%5D=01470&sc%5B%5D=01475&sc%5B%5D=01605&sc%5B%5D=01610&sc%5B%5D=01615&sc%5B%5D=01620&sc%5B%5D=01625'
  }

  datas = {
    '北海道': hokkaido
  }

  link: str = ''
  if area2 == '':
    link = datas[area1]
  else:
    link = datas[area1][area2]

  if type(link) is dict:
    link = random.choice(list(link.items()))[1]


  return link


if __name__ == '__main__':
  get_link('北海道')
