from bs4 import BeautifulSoup

from webScrapping.src.main.htmlContentExtractor import htmlContentExtractor
import webScrapping.config.properties as p


class htmlContentExtractorKX(htmlContentExtractor):

    def __init__(self, url: str):
        super().__init__(url)
        self.outputPath = p.htmlContentExtractPathKX

    def parseData(self):
        soup = BeautifulSoup(self.response, "html.parser")
        dataExtract = soup.find_all("article", class_="md-content__inner md-typeset")

        try:
            titleExtract = [elem.attrs.get("id") for elem in dataExtract[0] if elem.name == "h1"][0]
        except Exception as e:
            titleExtract = "Failed to extract title"

        try:
            bodyExtractText = dataExtract[0].text
        except Exception as e:
            bodyExtractText = "Failed to extract body"

        self.bean = self.generateBean(self.url, titleExtract, bodyExtractText)

    def generateBean(self, url: str, title: str, body: str) -> dict:
        return {
            "url": url
            , "title": title
            , "body": {
                "documentation": body
            }
        }
