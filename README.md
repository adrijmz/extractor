# Repository Overview

This repository contains a Python script for extracting and analyzing information from scientific articles in PDF format. The script performs various tasks to facilitate the analysis of multiple articles located in the directory /papers.

## Features
### Extraction of PDF Text: 
Utilizes Grobid to extract text from PDF documents, enabling further analysis of the content.
### Generation of Keyword Cloud: 
Creates a keyword cloud based on the abstracts of the articles, providing a visual representation of the most common words.
### Counting Figures per Article: 
Counts the number of figures in each article, aiding in understanding the visual content of the research presented.
### Extraction of Article Links: 
Attempts to extract links within the PDF documents, particularly references cited in the articles, providing additional resources for research.


## Docker Container GROBID
To install the GROBID image, execute the following command:
- docker pull lfoppiano/grobid:0.7.2

To run the container, execute the following command: 
- docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2

To access the GROBID service, go to the following URL:
- http://localhost:8070/