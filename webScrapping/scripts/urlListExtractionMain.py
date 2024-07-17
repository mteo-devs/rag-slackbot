from webScrapping.src.stackoverflowExtractor.urlExtractorSO import urlExtractorSO
from webScrapping.src.kxDocumentationExtractor.urlExtractorKX import urlExtractorKX

def extractURLSO():
    pageSize = 50
    for i in range(1, 49):
        url = f"https://stackoverflow.com/questions/tagged/kdb?tab=newest&page={i}&pagesize={pageSize}"
        print(f"Extracting URL from {url}")
        extractor = urlExtractorSO(url)
        extractor.beginExtractionProcess()

def extractURLKX():
    url = r"https://code.kx.com/q/cloud/aws/"
    extractor = urlExtractorKX(url)
    extractor.beginExtractionProcess()


if __name__ == "__main__":
    extractURLSO()
    extractURLKX()

