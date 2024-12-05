from typing import List
import collections

def ladderlen(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    if beginWord == endWord or not wordList or endWord not in wordList:
        return 0
    graph = collections.defaultdict(list)

    for word in wordList:
        for i in range(len(word)):
            transform = word[:i] + "*" + word[i+1:]
            graph[transform].append(word)

    queue = collections.deque([(beginWord, 1)])
    visited = set()

    while queue:
        word, distance = queue.popleft()

        if word == endWord:
            return distance
        
        visited.add(word)

        for i in range(len(word)):
            transformed = word[:i] + "*" + word[i+1:]
            potential_words = graph.get(transformed, None)
            if potential_words:
                for potential_word in potential_words:
                    if potential_word not in visited:
                        queue.append(potential_word, distance + 1)  
    return 0





