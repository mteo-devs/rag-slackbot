import pandas as pd

from webScrapping.config import properties as p
from webScrapping.src.utils import utils

if __name__ == "__main__":
    documentSO = utils.readJSON(p.htmlCompiledPathSO)
    documentSO = [elem.get("bean") for elem in documentSO]
    dfSO = pd.DataFrame(documentSO)
    dfSO["body"] = dfSO["body"].apply(lambda x: "\n".join([x.get("question"), x.get("topAnswer")]))
    dfSO = dfSO[["title", "body"]].rename(columns={"title": "document_id", "body": "text"})
    utils.writeJSON(p.toVectorDBPathSO, dfSO.to_dict(orient="records"))

    documentKX = utils.readJSON(p.htmlCompiledPathKX)
    documentKX = [elem.get("bean") for elem in documentKX]
    dfKX = pd.DataFrame(documentKX)
    dfKX["body"] = dfKX["body"].apply(lambda x: x.get("documentation"))
    dfKX = dfKX[["title", "body"]].rename(columns={"title": "document_id", "body": "text"})
    utils.writeJSON(p.toVectorDBPathKX, dfKX.to_dict(orient="records"))


