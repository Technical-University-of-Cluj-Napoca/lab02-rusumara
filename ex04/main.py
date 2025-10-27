from BST import BST
import random 
from search_engine import search_loop

def read_dictionary(filename: str) -> list[str]:
    """Reads a dictionary file and returns a list of words."""
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip().lower() for line in f if line.strip()]

def main():
    bst = BST()
    print("Loading dictionary...")
    words = read_dictionary("wordlist.txt")  
    random.shuffle(words)
    for w in words:
        bst.insert(w)
    print(f"Loaded {len(words)} words.")
    print("Start typing to see autocomplete suggestions.\n")
    search_loop(bst)

if __name__ == "__main__":
    main()
