from selenium import webdriver 

def main():
  urls = ["matchpremierhd","matchtvhd","matchfootball1hd","matchfootball2hd","matchfootball3hd"]
  print("\n 1:Матч Премьер \n 2:Матч ТВ \n 3:Матч Футбол 1 \n 4:Матч Футбол 2 \n 5:Матч Футбол 3")
  chanelnumber = int(input("Какой канал открыть?:"))
  
  print("\n1:На компьютере \n2:На apple tv")
  numberdevice = int(input("Открыть трансляцию на:"))
  devices = ['https://www.m3u8play.com/en','http://192.168.1.58/']
  sourceurl = devices[numberdevice-1]

  driver = webdriver.Chrome()  
  url = "https://www.tvplusonline.ru/getsignedurlcdnv3.php?c=" + urls[int(chanelnumber-1)] + "&q=1"
  driver.get(url)
  url = driver.find_element_by_tag_name('body').text

  if numberdevice == 1:
    driver.get(sourceurl)
    inputURL = driver.find_element_by_id('video-url')
    inputURL.click()
    inputURL.send_keys(url)
    button = driver.find_element_by_class_name('btn-dark')
    button.click()
    driver.wait()
  else:
    driver.get(sourceurl)
    inputURL = driver.find_element_by_css_selector("body > div.main > form > div > input[type=text]")
    inputURL.click()
    inputURL.send_keys(url)
    button = driver.find_element_by_css_selector("body > div.main > form > div > button")
    button.click()
    driver.wait()
if __name__ == "__main__":
  main()