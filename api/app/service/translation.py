import asyncio
import boto3


class Translation:

    def __init(self):
        polly = boto3.client("polly")

    async def translate(self, src_text: str, src_language: str, target_language: str):
        print(f'Translating text {src_text} in language {src_language} to {target_language}')
        asyncio.gather(self.create_src_audio(), self.create_translaiton_and_audio())

    async def create_translation_and_audio(self, src_text: str, src_language: str, target_language: str):
        print(f'Creating audio and translation for text {src_text} in language {src_language}')

    async def create_src_audio(self, src_text: str, src_language: str):
        print(f'Creating audio for text {src_text} in language {src_language}')

    @staticmethod
    async def translate(src_text: str, src_language: str, target_language: str):
        t = Translation()
        print(f'Translating text {src_text} in language {src_language} to {target_language}')
        asyncio.gather(t.create_src_audio(src_text, src_language   ),
                       t.create_translation_and_audio(src_text, src_language, target_language))


if __name__ == "__main__":
    asyncio.run(Translation.translate("Hello world", "EN", "ES"))