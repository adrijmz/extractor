This repository aims to provide a Python script for extracting and analyzing information from scientific articles in PDF format. The rationale behind this project is to facilitate the analysis of multiple scientific articles, aiding researchers and practitioners in comprehensively understanding and extracting valuable insights from academic literature.

## Goals

The main goals of this project are:

- Efficient Text Extraction: To streamline the process of extracting text from PDF documents, enabling further analysis of the content without manual effort.
- Visual Representation: To provide visual representations of key information extracted from the articles, such as keyword clouds and figures per article.
- Enhanced Research Resources: To extract links within the PDF documents, particularly references cited in the articles, providing additional resources for research and exploration.

## Features Overview

- PDF Text Extraction: Utilizes Grobid, an open-source tool, to extract text from PDF documents.
- Keyword Cloud Generation: Generates keyword clouds based on the abstracts of the articles, offering a visual representation of the most common words.
- Figure Counting: Counts the number of figures in each article, aiding in understanding the visual content of the research presented.
- Link Extraction: Attempts to extract links within the PDF documents, particularly references cited in the articles, to provide additional resources for research.

## Technical Approach

- Dockerized Environment: The project provides Docker images for easy deployment and reproducibility of the extraction and analysis process.
- Dependency Management: Utilizes Python virtual environments and dependency management tools to ensure consistent and reproducible execution across different environments.

## Potential Impact

- Research Efficiency: By automating the extraction and analysis process, researchers can save time and effort in analyzing multiple scientific articles, leading to increased efficiency in literature review and research exploration.
- Knowledge Discovery: The visual representations generated by the script, such as keyword clouds and figure counts, can provide valuable insights and facilitate knowledge discovery in academic literature.
