"""
from rich import print
from rich.console import Console

def count_words_and_occureces(file_path):
    console = Console()

    try:
        with open(file_path, 'r', encoding='utf-8') as file :
            text = file.read()
            words = text.split()
            total_word_count = len(words)

            keyword = console.input("[yellow] Entrez un mot clé pour compter")
            keyword_count = words.count(keyword)

            return total_word_count, keyword_count
    except FileNotFoundError:
        console.print("[red] Fichier non trouvé. [/]")
        return None, None
    
#Utilisation 
file_path = "test.txt"
total_words, keyword_occurences = count_words_and_occureces(files_path)
print (f"[blue] Nombre total de mots : [/] {total_words}")
print (f" ")
"""

