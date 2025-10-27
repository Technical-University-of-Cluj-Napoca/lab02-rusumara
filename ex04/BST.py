
class Node:
    """A node in the binary search tree."""

    def __init__(self, word: str):
        self.word = word
        self.left = None
        self.right = None


class BST:
    """Binary Search Tree for storing words and suggesting completions."""

    def __init__(self):
        self.root = None

    def insert(self, word: str):
        """Insert a word into the BST."""
        if self.root is None:
            self.root = Node(word)
        else:
            self._insert_rec(self.root, word)

    def _insert_rec(self, node: Node, word: str):
        """Recursive helper for insert."""
        if word < node.word:
            if node.left is None:
                node.left = Node(word)
            else:
                self._insert_rec(node.left, word)
        elif word > node.word:
            if node.right is None:
                node.right = Node(word)
            else:
                self._insert_rec(node.right, word)
        else:
            return 
        # duplicates ignored

    def autocomplete(self, prefix: str) -> list[str]:
        """Return all words that start with the given prefix."""
        results = []
        self._autocomplete_rec(self.root, prefix, results)
        return results

    def _autocomplete_rec(self, node: Node, prefix: str, results: list[str]):
        """Recursive helper to collect words with given prefix."""
        if node is None:
            return
        
        # Search left subtree if prefix could be smaller
        if prefix <= node.word:
            self._autocomplete_rec(node.left, prefix, results)

        # If word matches prefix, add it
        if node.word.startswith(prefix):
            results.append(node.word)

        # Search right subtree if prefix could be larger
        if prefix >= node.word:
            self._autocomplete_rec(node.right, prefix, results)
