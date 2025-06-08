from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from urllib.parse import urljoin

# Set up Selenium with Chrome
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

# options.add_argument("--headless")  # Run in headless mode
driver = webdriver.Chrome(options=options)

# Open Google News
driver.get("https://news.google.com/")

# Wait until the main news articles are loaded
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article")))

# Extract article containers
articles = driver.find_elements(By.CSS_SELECTOR, "article")

print("Top Google News Articles:\n")

for idx, article in enumerate(articles[:10], start=1):  # Limit to first 10
    try:
        # Headline
        headline_elem = article.find_element(By.CSS_SELECTOR, "h3, h4")
        headline = headline_elem.text

        # Link (partial, needs base URL)
        link_elem = headline_elem.find_element(By.TAG_NAME, "a")
        partial_link = link_elem.get_attribute("href")
        full_link = urljoin("https://news.google.com/", partial_link)
        # Description (if available)
        try:
            description = article.find_element(By.CSS_SELECTOR, "span").text
        except:
            description = "No description available"

        print(f"{idx}. {headline}\n   🔗 {full_link}\n   📝 {description}\n")

    except Exception as e:
        print(f"Error parsing article {idx}: {e}")

    # Close the browser
    driver.quit()
