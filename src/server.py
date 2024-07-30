import random

def rearrange_words(word_list):
  """Rearranges each word in a list to create a new list of jumbled words.

  Args:
    word_list: A list of words to be rearranged.

  Returns:
    A new list of words, each with the same letters as the corresponding word in the input list, but in a different order.
  """

  jumbled_words = []
  for word in word_list:
    letters = list(word)
    random.shuffle(letters)
    new_word = ''.join(letters)
    while new_word == word:
      random.shuffle(letters)
      new_word = ''.join(letters)
    jumbled_words.append(new_word)
  return jumbled_words

# Example usage:
words = ["hello", "world", "python"]
jumbled_words = rearrange_words(words)
print(jumbled_words)
