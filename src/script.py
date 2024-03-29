import os
import re
import PyPDF2
import requests
import argparse
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# Función para llamar a la API de Grobid y extraer el texto del documento PDF
def extract_text_with_grobid(pdf_path):
    url = 'http://server:8070/api/processFulltextDocument'
    files = {'input': open(pdf_path, 'rb')}
    response = requests.post(url, files=files)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to extract text from {pdf_path}")
        return ''


# Función para crear una nube de palabras clave basada en la información del abstract
def generate_keyword_cloud(abstracts, output_directory):
    text = ' '.join(abstracts)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    wordcloud.to_file(os.path.join(output_directory, 'keyword_cloud.png'))


# Función para contar el número de figuras por artículo
def count_figures(articles, output_directory):
    fig_counts = [len(re.findall(r'\bfigure\b|\bfig\b', article, flags=re.IGNORECASE)) for article in articles]
    plt.bar(range(1, len(articles) + 1), fig_counts)
    plt.xlabel('Article')
    plt.ylabel('Number of Figures')
    plt.title('Number of Figures per Article')
    # Guardar el gráfico de figuras por articulo en un fichero en la carpeta de salida
    plt.savefig(os.path.join(output_directory, 'figure_counts.png'))


# Función para extraer los enlaces de un artículo
def extract_links(pdf_path):
    links = []
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text = page.extract_text()
            page_links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                                    text)
            links.extend(page_links)

    # Guardar los enlaces en un archivo de texto en la carpeta de salida
    with open(os.path.join(output_directory, 'links.txt'), 'a') as f:
        f.write('-' * 40 + '\n')
        f.write(f"Links found in {pdf_path}:" + '\n')
        for link in links:
            f.write(link + '\n')
        f.write('-' * 40 + '\n')
    return links


# Función para limpiar el archivo de enlaces
def clear_links_file(output_directory):
    with open(os.path.join(output_directory, 'links.txt'), 'w') as f:
        f.write('')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='script.py',
        description='Process some PDFs.')

    parser.add_argument(
        '--INPUT',
        default='./papers',
        type=str,
        help='Directory containing PDFs')

    parser.add_argument(
        '--OUTPUT',
        default='./output',
        type=str,
        help='Directory to save the output files')

    args = parser.parse_args()
    pdf_directory = args.INPUT
    output_directory = args.OUTPUT

    # Crear la carpeta de salida si no existe
    os.makedirs(output_directory, exist_ok=True)

    abstracts = []
    articles = []

    # Extraer texto de archivos PDF y llenar las listas abstracts y articles utilizando Grobid
    for filename in os.listdir(pdf_directory):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_directory, filename)
            text = extract_text_with_grobid(pdf_path)
            abstracts.append(text[:1000])  # Tomar solo los primeros 1000 caracteres como abstracto
            articles.append(text)

    # Llamadas a las funciones para realizar las tareas
    generate_keyword_cloud(abstracts, output_directory)
    count_figures(articles, output_directory)
    clear_links_file(output_directory)

    for filename in os.listdir(pdf_directory):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_directory, filename)
            links = extract_links(pdf_path)
