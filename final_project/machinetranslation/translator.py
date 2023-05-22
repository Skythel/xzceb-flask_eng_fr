"""
Translation functions
"""

import os
# import json
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)

try:
    # Invoke a method
    print()
except ApiException as ex:
    print("Method failed with status code " + str(ex.code) + ": " + ex.message)

def englishToFrench(englishText):
    """
    English to French
    """
    if englishText == "":
        return "Input cannot be null"
    frenchText = language_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()["translations"][0]["translation"]
    print(frenchText)
    return frenchText


def frenchToEnglish(frenchText):
    """
    French to English
    """
    if frenchText == "":
        return "Input cannot be null"
    englishText = language_translator.translate(
    text=frenchText,
    model_id='fr-en').get_result()["translations"][0]["translation"]
    return englishText
