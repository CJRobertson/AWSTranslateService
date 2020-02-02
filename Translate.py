# Translate.py

# AWS' python SDK.
import boto3

# Define the translate service.
translate = boto3.client(service_name='translate', region_name='us-west-2', use_ssl=True)


# Process text that needs to be translated by AWS Translate.
def process_text(text_to_translate, source_lang, target_lang):
    result = translate.translate_text(Text=text_to_translate, SourceLanguageCode=source_lang,
                                      TargetLanguageCode=target_lang)
    return result.get('TranslatedText')
