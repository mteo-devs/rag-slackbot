import requests, os
from datetime import datetime

from webScrapping.src.utils import utils


class urlExtractor:

    def __init__(self, url: str):
        self.url = url
        self.baseFileName = "urlExtract"

    def extractData(self):
        self.response = requests.get(self.url)
        # todo: error catching for error code != 200
        self.response = self.response.text

    def generateBean(self, url: str, urlExtract: str) -> dict:
        return {
            "url": url
            , "extractedURL": urlExtract
        }

    def exportBean(self):
        currDatetime = datetime.now()
        currDatetime = currDatetime.strftime("%Y%m%d_%H%M%S")
        exportPath = os.path.join(self.outputPath, f"{self.baseFileName}_{currDatetime}.json")
        utils.writeJSON(filename=exportPath, jsonObj=self.bean)

    def beginExtractionProcess(self):
        self.extractData()
        self.parseData()
        self.exportBean()


