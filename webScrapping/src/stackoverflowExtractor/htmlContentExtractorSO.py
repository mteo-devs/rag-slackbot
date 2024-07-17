from bs4 import BeautifulSoup

from webScrapping.src.main.htmlContentExtractor import htmlContentExtractor
import webScrapping.config.properties as p


class htmlContentExtractorSO(htmlContentExtractor):

    def __init__(self, url: str):
        super().__init__(url)
        self.outputPath = p.htmlContentExtractPathSO

    def parseData(self):
        soup = BeautifulSoup(self.response, "html.parser")

        titleExtract = soup.find_all("title")
        try:
            titleExtract = titleExtract[0].text
        except Exception as e:
            titleExtract = "Failed to extract title"

        bodyExtract = soup.find_all("div", class_="s-prose js-post-body")
        try:
            bodyExtractText = [elem.text for elem in bodyExtract]
            questionExtract, topAnswerExtract = bodyExtractText[0], bodyExtractText[1]
        except Exception as e:
            questionExtract, topAnswerExtract = "Failed to extract question", "Failed to extract answer"

        self.bean = self.generateBean(self.url, titleExtract, questionExtract, topAnswerExtract)

    def generateBean(self, url: str, title: str, question: str, answer: str) -> dict:
        return {
            "url": url
            , "title": title
            , "body": {
                "question": question
                , "topAnswer": answer
            }
        }
