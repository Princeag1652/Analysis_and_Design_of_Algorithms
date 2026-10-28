
import heapq
from typing import Dict, Optional


class Node:
    def __init__(
        self,
        char: Optional[str],
        frequency: int,
        left=None,
        right=None
    ):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right

    # Allows heapq to compare nodes by frequency
    def __lt__(self, other):
        return self.frequency < other.frequency


class HuffmanCoder:
    def __init__(self):
        self.root = None

    def build_tree(self, frequencies: Dict[str, int]) -> Node:
        if not frequencies:
            raise ValueError("Frequency dictionary cannot be empty")

        if any(freq <= 0 for freq in frequencies.values()):
            raise ValueError("Frequencies must be positive")

        # Create a min-heap containing leaf nodes
        heap = [
            Node(char, freq)
            for char, freq in frequencies.items()
        ]
        heapq.heapify(heap)

        # Repeatedly combine the two least-frequent nodes
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)

            merged = Node(
                char=None,
                frequency=left.frequency + right.frequency,
                left=left,
                right=right
            )

            heapq.heappush(heap, merged)

        self.root = heapq.heappop(heap)
        return self.root

    def generate_codes(self) -> Dict[str, str]:
        if self.root is None:
            raise ValueError("Build the Huffman tree first")

        codes = {}

        def traverse(node, code):
            if node is None:
                return

            # Leaf node represents a character
            if node.char is not None:
                codes[node.char] = code if code else "0"
                return

            traverse(node.left, code + "0")
            traverse(node.right, code + "1")

        traverse(self.root, "")
        return codes


# ---------------- MAIN PROGRAM ----------------

if __name__ == "__main__":
    frequencies = {
        "A": 5,
        "B": 9,
        "C": 12,
        "D": 13,
        "E": 16,
        "F": 45
    }

    coder = HuffmanCoder()

    root = coder.build_tree(frequencies)
    codes = coder.generate_codes()

    print("Character Frequencies:")
    for char, freq in frequencies.items():
        print(f"{char}: {freq}")

    print("\nHuffman Codes:")
    for char in sorted(codes):
        print(f"{char}: {codes[char]}")

    print("\nRoot Frequency:", root.frequency)
