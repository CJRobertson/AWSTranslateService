# translate.py

# AWS' python SDK.
import boto3
import os

# Define the translate service.
translate = boto3.client(service_name='translate', region_name='us-west-2', use_ssl=True)


class TranslateText(object):
    def __init__(self) -> None:
        try:
            self.aws_region = os.environ['AWS_REGION']
        except KeyError as e:
            self.aws_region = 'us-west-2'

        try:
            self.service_name = os.environ['SERVICE_NAME']
        except KeyError as e:
            self.service_name = 'translate'

        self.translate = boto3.client(service_name=self.service_name, region_name=self.aws_region, use_ssl=True)

    def process_text(self, text: str, source_lang: str, target_lang: str) -> str:
        result = self.translate.translate_text(Text=text,
                                               SourceLanguageCode=source_lang,
                                               TargetLanguageCode=target_lang,
                                               )
        return result.get('TranslatedText')
