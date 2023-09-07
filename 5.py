import heapq
 
 
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''
    def __lt__(self, nxt):
        return self.freq < nxt.freq
def printNodes(node, val=''):
    newVal = val + str(node.huff)
    if node.left :
        printNodes(node.left, newVal)
    if(node.right):
        printNodes(node.right,newVal)
    if(not node.left and not node.right):
        print(f"{node.symbol} -> {newVal}")
     def encode_text(text, huffman_tree):
    encoding_map = {}

    def traverse_tree(node, code=''):
        if node.left:
            traverse_tree(node.left, code + '0')
        if node.right:
            traverse_tree(node.right, code + '1')
        if not node.left and not node.right:
            encoding_map[node.symbol] = code

    traverse_tree(huffman_tree)

    encoded_text = ''
    for char in text:
        encoded_text += encoding_map[char]

    return encoded_text

def decode_text(encoded_text, huffman_tree):
    decoded_text = ''
    current_node = huffman_tree

    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if not current_node.left and not current_node.right:
            decoded_text += current_node.symbol
            current_node = huffman_tree

    return decoded_text
chars = []
for x in range(6):
    k=input("enter char:")
    chars.append(k)
freq = []
for y in range(6):
    z=int(input("enter freq:"))
    freq.append(z)
nodes = []
for x in range(len(chars)):
    heapq.heappush(nodes, node(freq[x], chars[x]))
while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
    left.huff = 0
    right.huff = 1
    newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
    heapq.heappush(nodes, newNode)
printNodes(nodes[0])
