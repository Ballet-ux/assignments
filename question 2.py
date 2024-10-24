def word_frequencies (sentence):
    words = sentence.split()
    return {words[i]:i for i in range(len(words)) }

sentence = "This is a test sentence and this is another test"
print(word_frequencies(sentence))