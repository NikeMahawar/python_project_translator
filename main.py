import requests
from bs4 import BeautifulSoup
from mtranslate import translate
import webbrowser
lang= input("English: 'en' \n"
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
"Please write the code of suitable language from the above: ")
# Function to translate website
def translate_website(file_path, target_language):
    # Read the HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

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

    # Save the translated HTML to a file
    translated_html = soup.prettify()
    translated_file = "D:\\web_development\\translated.html"
    with open(translated_file, "w", encoding="utf-8") as f:
        f.write(translated_html)

    # Open the translated file in Chrome
    webbrowser.open('file://' + translated_file)

# Usage example
file_path = r'D:\web_development\my_website.html'
translate_website(file_path, lang)

