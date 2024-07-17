import os
from webScrapping.src.utils import utils
from webScrapping.config import properties as p

if __name__ == "__main__":

    # compile HTMLs for Stackoverflow
    filenamesSO = os.listdir(p.htmlContentExtractPathSO)
    allFullPathsSO = [os.path.join(p.htmlContentExtractPathSO, elem) for elem in filenamesSO]
    allJSONSO = [utils.readJSON(elem) for elem in allFullPathsSO]
    allExtractedHTMLSO = [{"row": i, "bean": elem} for i, elem in enumerate(allJSONSO)]
    utils.writeJSON(filename=p.htmlCompiledPathSO, jsonObj=allExtractedHTMLSO)

    # compile HTMLs for KX Documentations
    filenamesKX = os.listdir(p.htmlContentExtractPathKX)
    allFullPathsKX = [os.path.join(p.htmlContentExtractPathKX, elem) for elem in filenamesKX]
    allJSONKX = [utils.readJSON(elem) for elem in allFullPathsKX]
    allExtractedHTMLKX = [{"row": i, "bean": elem} for i, elem in enumerate(allJSONKX)]
    utils.writeJSON(filename=p.htmlCompiledPathKX, jsonObj=allExtractedHTMLKX)
