from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient("xoxb-3675368677831-3713737011296-NYUb4In4SV1F9KL0TkD1kjsT")

chorme_options = Options()
chorme_options.add_argument('--profile-directory=Default')
chorme_options.add_argument("--incognito")
chorme_options.add_argument('--headless')
chorme_options.add_argument('--no-sandbox')
chorme_options.add_argument("--disable-plugins-discovery")
chorme_options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", chrome_options=chorme_options)
url = ""
pagename = ""
# 오늘의 QT 본문말씀 페이지 저장
def setUrl_biblePage():
    pagename = 'bible'
    url = "https://www.duranno.com/qt/view/bible.asp?qtDate="
    capture(url, pagename)
    

# 오늘의 QT 본문해설 페이지 저장
def setUrl_explainPage():
    pagename = 'explain'
    url = "https://www.duranno.com/qt/view/explain.asp?qtDate="
    capture(url, pagename)

# 오늘의 QT 이미지 캡쳐
def capture(url, pagename):
    driver.get(url)
    original_size = driver.get_window_size()
    required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    driver.set_window_size(required_width, required_height)
    element = driver.find_element_by_css_selector('body > div > div > div.contents.right.last-div')
    element_png = element.screenshot_as_png
    with open('TodayQT_{0}.png'.format(pagename), "wb") as file:
        file.write(element_png)

setUrl_biblePage()
setUrl_explainPage()
#SlackAPI.get_channel_id(channel_name='todayqt')


