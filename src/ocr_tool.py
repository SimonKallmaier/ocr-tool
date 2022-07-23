import io
from google.cloud import vision


class OcrTextExtractor:

    def __init__(self, path) -> None:
        self.path = path

    def path_to_image(self):
        # TODO handle pdfs
        if self.path.endswith(".jpg"):
            return self.path
        else:
            raise ValueError("Currently only jpgs are supported")

    @staticmethod
    def load_image(image):
        with io.open(image, 'rb') as image_file:
            image_content = image_file.read()
        return image_content

    @staticmethod
    def apply_cloud_vision(content):
        client = vision.ImageAnnotatorClient()
        image = vision.Image(content=content)
        response = client.document_text_detection(image=image)
        return response

    @staticmethod
    def get_ocr_result(response) -> str:
        return response.text_annotations[0].description

    def run(self) -> str:
        content = self.load_image(self.path)
        response = self.apply_cloud_vision(content=content)
        return self.get_ocr_result(response=response)


if __name__ == '__main__':
    import os
    
    path = os.path.join(os.pardir, "pdfs", "test001.jpg")
    ocr_text_extractor = OcrTextExtractor(path=path)
    ocr_text = ocr_text_extractor.run()
    print(ocr_text)
