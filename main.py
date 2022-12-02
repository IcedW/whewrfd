import fake_useragent
import requests
from bs4 import BeautifulSoup
url = "https://allo.ua/ua/roboty-pylesosy/"
user = fake_useragent.UserAgent().random
headers = {"user-agent": user}
response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.text, "lxml")
all_product = soup.find("div", class_ ="products-layout__container products-layout--grid")
product_list = all_product.find_all("div", class_ ='product-card')
for i in range(len(product_list)):
    product_tittle = product_list[i].find("a", class_='product-card__title')
    try:
        product_cost = product_list[i].find("div", class_="v-pb__old")
        product_cost_with_discount = product_list[i].find("div", class_="v-pb__cur discount")
        with open("roombas.txt", "a", encoding="utf-8") as file:
            file.write(f"  {product_tittle.text} {product_cost.text} {product_cost_with_discount.text} '\n' ")
    except AttributeError:
        print("no sale for that crap")