from webScrapping.src.stackoverflowExtractor.htmlContentExtractorSO import htmlContentExtractorSO
from webScrapping.src.kxDocumentationExtractor.htmlContentExtractorKX import htmlContentExtractorKX


if __name__ == "__main__":

    inputURL = r"https://code.kx.com/q/cloud/aws/"
    #inputURL = r"https://code.kx.com/q/ref/sv/"
    #inputURL = r"https://code.kx.com/q/wp/permissions/"

    if "stackoverflow.com" in inputURL:
        extractorSO = htmlContentExtractorSO(inputURL)
        extractorSO.beginDataExtractionProcess()

    elif "code.kx.com" in inputURL:
        extractorSO = htmlContentExtractorKX(inputURL)
        extractorSO.beginDataExtractionProcess()

    print("Extraction Completed")
