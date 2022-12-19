from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

email = ""
password = ""
phone_number = "0944123456"
url = "https://www.linkedin.com"
chrome_driver = "/Users/jano/chromedriver"
driver = webdriver.Chrome(chrome_driver)
driver.get(url)

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()
time.sleep(5)

email_field = driver.find_element(By.ID, "username")
email_field.send_keys(email)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(password)
password_field.send_keys(Keys.ENTER)
time.sleep(5)

phone_field = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
if phone_field == "":
    phone_field.send_keys(phone_number)
submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
submit_button.click()

driver.quit()
#news_tags = soup.findAll("a", href=True)
#news = [tag.getText() for tag in news_tags]

#article_upvotes = [int(score.getText().split()[0]) for score in soup.findAll("span", class_="score")]

# with open("website.html") as file:
#     contents = file.read()
# soup = BeautifulSoup(contents, "html.parser")
# all_anchors = soup.findAll(name="a")
# print(all_anchors)
# for anchor in all_anchors:
#     print(anchor.get("href"))
