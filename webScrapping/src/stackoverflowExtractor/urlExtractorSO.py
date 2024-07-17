from bs4 import BeautifulSoup

from webScrapping.src.main.urlExtractor import urlExtractor
import webScrapping.config.properties as p


class urlExtractorSO(urlExtractor):

    def __init__(self, url: str):
        super().__init__(url)
        self.baseURL = "https://stackoverflow.com"
        self.outputPath = p.urlExtractPathSO

    def parseData(self):
        soup = BeautifulSoup(self.response, "html.parser")

        urlExtract = soup.find_all("h3", class_="s-post-summary--content-title")
        try:
            urlExtract = [elem.contents[1] for elem in urlExtract]
            urlExtract = ["".join([self.baseURL, elem.get("href")]) for elem in urlExtract]
        except Exception as e:
            urlExtract = "Failed to extract URL"

        self.bean = self.generateBean(self.url, urlExtract)

