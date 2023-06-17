import requests
from bs4 import BeautifulSoup
from mtranslate import translate
import webbrowser

lang = input("English: 'en' \n"
             "Spanish: 'es' \n"
             "French: 'fr' \n"
             "German: 'de' \n"
             "Italian: 'it' \n"
             "Portuguese: 'pt' \n"
             "Russian: 'ru' \n"
             "Japanese: 'ja' \n"
             "Chinese (Simplified): 'zh-cn' "
             "Chinese (Traditional): 'zh-tw' "
             "Korean: 'ko' \n"
             "Arabic: 'ar' \n"
             "Dutch: 'nl' \n"
             "Swedish: 'sv' \n"
             "Danish: 'da' \n"
             "Norwegian: 'no' \n"
             "Finnish: 'fi' \n"
             "Greek: 'el' \n"
             "Turkish: 'tr' \n"
             "Please write the code of the suitable language from the above: ")

def translate_website(url, target_language):
    # Fetch the HTML content from the URL
    response = requests.get(url)
    html_content = response.text

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Specify CSS selector for elements containing text to translate
    css_selector = 'p, h1, h2, h3, h4, h5, h6, span, div, nav, footer, link'

    # Find elements using the CSS selector
    text_elements = soup.select(css_selector)

    # Translate each text element
    for element in text_elements:
        original_text = element.get_text()
        translated_text = translate(original_text, target_language)
        element.string = translated_text

    # Get the translated HTML content
    translated_html = soup.prettify()

    # Open the translated content in a new browser tab
    webbrowser.open_new_tab(f"data:text/html;charset=utf-8,{translated_html}")

# Usage example
url = input("Enter the URL of the website to translate: ")
translate_website(url, lang)
