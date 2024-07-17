import os

# to change the projectPath accordingly
projectPath = r"...\rag-slackbot\webScrapping"

dataFolder = r"data"
dataPath = os.path.join(projectPath, dataFolder)
htmlContentExtractFolder = r"htmlContentExtract"
urlExtractFolder = r"urlExtract"
htmlCompiledFolder = r"compiledHTML"
urlCompiledFolder = r"compiledURL"
toVectorDBFolder = r"toVectorDB"

dataFolderKX = r"kxDocumentation"
dataPathKX = os.path.join(dataPath, dataFolderKX)
htmlContentExtractPathKX = os.path.join(dataPathKX, htmlContentExtractFolder)
urlExtractPathKX = os.path.join(dataPathKX, urlExtractFolder)
htmlCompiledPathKX = os.path.join(dataPathKX, htmlCompiledFolder, "htmlCompiledList.json")
urlCompiledPathKX = os.path.join(dataPathKX, urlCompiledFolder, "urlCompiledList.json")
toVectorDBPathKX = os.path.join(dataPathKX, toVectorDBFolder, "kxDocumentationData.json")

dataFolderSO = r"stackoverflow"
dataPathSO = os.path.join(dataPath, dataFolderSO)
htmlContentExtractPathSO = os.path.join(dataPathSO, htmlContentExtractFolder)
urlExtractPathSO = os.path.join(dataPathSO, urlExtractFolder)
htmlCompiledPathSO = os.path.join(dataPathSO, htmlCompiledFolder, "htmlCompiledList.json")
urlCompiledPathSO = os.path.join(dataPathSO, urlCompiledFolder, "urlCompiledList.json")
toVectorDBPathSO = os.path.join(dataPathSO, toVectorDBFolder, "stackoverflowData.json")






