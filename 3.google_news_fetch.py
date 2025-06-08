from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


def get_google_news():
    # Set up Selenium WebDriver
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")  # Run in headless mode
    driver = webdriver.Chrome(options=options)

    try:
        # Open Google News
        driver.get("https://news.google.com/")
        time.sleep(10)  # Allow time for page to load

        # Find news headlines
        headlines = driver.find_elements(By.XPATH, "//h3")
        articles = driver.find_elements(By.CSS_SELECTOR, "article")

        article_headlines = [article.text for article in articles if article.text.strip() != ""]
        print(article_headlines)
        # Extract and print news headlines
        news_list = [headline.text for headline in headlines if headline.text.strip() != ""]

        # Extract headlines
        headlines = driver.find_elements(By.CSS_SELECTOR, 'h4, h3')

        # Print the first 10 headlines
        print("Top Headlines:\n")
        for idx, headline in enumerate(headlines[:10], start=1):
            print(f"{idx}. {headline.text}")

        print(len(news_list))
        return news_list
    finally:
        driver.quit()


if __name__ == "__main__":
    news = get_google_news()
    for idx, headline in enumerate(news, start=1):
        print(f"{idx}. {headline}")
