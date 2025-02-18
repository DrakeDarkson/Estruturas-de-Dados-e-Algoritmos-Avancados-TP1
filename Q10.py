class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def autocomplete(self, prefix):
        node = self.search_prefix(prefix)
        if node is None:
            return []
        
        words = []
        self._dfs(node, prefix, words)
        return words

    def _dfs(self, node, prefix, words):
        if node.is_end_of_word:
            words.append(prefix)

        for char, child_node in node.children.items():
            self._dfs(child_node, prefix + char, words)

# Exemplo:

trie = Trie()
trie.insert("casa")
trie.insert("carro")
trie.insert("cachorro")
trie.insert("caminhão")
trie.insert("cadeira")

print(trie.autocomplete("ca"))

print(trie.autocomplete("cam"))
