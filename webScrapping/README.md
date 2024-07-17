Repository Documentation
========================

# What is this Repository doing?
1. Generate a list of URLs from stackoverflow and KX documentation.
2. Extract the HTML content from each of the URL extracted above.

---

# ETL Process Flow
(1) urlListExtractionMain.py\
&emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;&emsp;|-- urlExtractorSO\
&emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;&emsp;|-- urlExtractorKX\
&emsp;&emsp;&emsp;&emsp;|\
This script extract a list of stackoverflow and kx documentation URLs.
The extracted URL can be found in ~/data/{platform}/urlExtract.\
&emsp;&emsp;&emsp;&emsp;|\
(2) urlListCompiler.py \
&emsp;&emsp;&emsp;&emsp;|\
This script compiles the extracted URL into a single list. The compiled list of URL is located at ~/data/{platform}/compiledURL.\
&emsp;&emsp;&emsp;&emsp;|\
(3) htmlContentExtractionMain.py\
&emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;&emsp;|-- htmlContentExtractorSO\
&emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;&emsp;|-- htmlContentExtractorKX\
&emsp;&emsp;&emsp;&emsp;|\
This script takes in the compiled list of URLs as input and extract the html content of every URL in that list. 
The html extract can be found in ~data/{platform}/htmlContentExtract.\
&emsp;&emsp;&emsp;&emsp;|\
(4) htmlListCompiler.py\
&emsp;&emsp;&emsp;&emsp;|\
This script compiles the extract HTML content into a single file. The compiled list of HTML content is located at ~/data/{platform}/compiledHTML.\
&emsp;&emsp;&emsp;&emsp;|\
(5) dataProcessingForVectorDB.py \
&emsp;&emsp;&emsp;&emsp;|\
This script transform the compiled HTML content into the required schema to store in the vectorDB. The transformed data is located at ~/data/{platform}/toVectorDB\
\
\
{platform} can be stackoverflow or kxDocumentation.
---

