from webScrapping.src.stackoverflowExtractor.htmlContentExtractorSO import htmlContentExtractorSO
from webScrapping.src.kxDocumentationExtractor.htmlContentExtractorKX import htmlContentExtractorKX

from webScrapping.config import properties as p
from webScrapping.src.utils import utils


if __name__ == "__main__":

    # Extraction for Stackoverflow
    urlListSO = utils.readJSON(filename=p.urlCompiledPathSO).get("extractedURL")

    for url in urlListSO:
        print(f"Extracting html content from {url}")
        extractorSO = htmlContentExtractorSO(url)
        extractorSO.beginDataExtractionProcess()

    # Extraction for KX Documentation
    urlListKX = utils.readJSON(filename=p.urlCompiledPathKX).get("extractedURL")

    for url in urlListKX:
        print(f"Extracting html content from {url}")
        extractorSO = htmlContentExtractorKX(url)
        extractorSO.beginDataExtractionProcess()

    print("Extraction Completed")
