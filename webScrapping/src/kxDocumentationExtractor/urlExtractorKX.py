from bs4 import BeautifulSoup

from webScrapping.src.main.urlExtractor import urlExtractor
import webScrapping.config.properties as p


class urlExtractorKX(urlExtractor):

    def __init__(self, url: str):
        super().__init__(url)
        self.baseURL = "https://code.kx.com/q"
        self.outputPath = p.urlExtractPathKX

    def parseData(self):
        soup = BeautifulSoup(self.response, "html.parser")

        urlExtract = soup.find_all("a", class_="md-nav__link")
        try:
            urlExtract = [elem.attrs.get("href") for elem in urlExtract]
            urlExtract = [elem.replace("../..", self.baseURL) for elem in urlExtract]
            urlExtract = [elem for elem in urlExtract if "code.kx.com" in elem]
        except Exception as e:
            urlExtract = "Failed to extract URL"

        self.bean = self.generateBean(self.url, urlExtract)
