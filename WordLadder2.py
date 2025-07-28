#Given two words, beginWord and endWord, and a dictionary wordList, find all the shortest transformation sequences from beginWord to endWord.

from collections import defaultdict, deque

def findLadders(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return []

    layer = {}
    layer[beginWord] = [[beginWord]]
    res = []

    while layer:
        new_layer = defaultdict(list)
        for word in layer:
            if word == endWord:
                return layer[word]
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in wordSet:
                        new_layer[new_word] += [j + [new_word] for j in layer[word]]
        wordSet -= set(new_layer.keys())
        layer = new_layer
    return res

#Test
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(findLadders(beginWord, endWord, wordList))
