import os
from itertools import chain
from webScrapping.src.utils import utils
from webScrapping.config import properties as p

if __name__ == "__main__":

    # compile URLs for Stackoverflow
    filenamesSO = os.listdir(p.urlExtractPathSO)
    allFullPathsSO = [os.path.join(p.urlExtractPathSO, elem) for elem in filenamesSO]
    allJSONSO = [utils.readJSON(elem) for elem in allFullPathsSO]
    allExtractedURLSO = [elem.get("extractedURL") for elem in allJSONSO]
    allExtractedURLSO = list(chain(*allExtractedURLSO))
    beanSO = {"extractedURL": allExtractedURLSO}
    utils.writeJSON(filename=p.urlCompiledPathSO, jsonObj=beanSO)

    # compile URLs for KX Documentations
    filenamesKX = os.listdir(p.urlExtractPathKX)
    allFullPathsKX = [os.path.join(p.urlExtractPathKX, elem) for elem in filenamesKX]
    allJSONKX = [utils.readJSON(elem) for elem in allFullPathsKX]
    allExtractedURLKX = [elem.get("extractedURL") for elem in allJSONKX]
    allExtractedURLKX = list(chain(*allExtractedURLKX))
    beanKX = {"extractedURL": allExtractedURLKX}
    utils.writeJSON(filename=p.urlCompiledPathKX, jsonObj=beanKX)
