def encodeWordByWord(current, previous):
  i = 0
  similar_chars = 0
  while (i <len(previous)) and (previous[i] == current[i]):
    similar_chars +=1
    i += 1 

  new_current = str(similar_chars) + ' ' + current[similar_chars:len(current)]
  return new_current  

def encoding(str):
  words = str.split('\n')
  current = ''
  previous = ''
  new_words = []
  for word in words:
    current = word
    new_words.append( encodeWordByWord(current, previous) )
    previous = word
  return '\n'.join(new_words)


def decodeWordByWord(current, previous):
  similar_chars = int(current.split(' ')[0])
  new_current = previous[0:int(similar_chars)] + current.split(' ')[1]
  return new_current

def decoding(str):
  words = str.split('\n')
  current = ''
  previous = ''
  new_words = []

  for word in words:
    current = word
    new_current = decodeWordByWord(current, previous)
    new_words.append(new_current)
    previous = new_current

  return '\n'.join(new_words)

if __name__ == '__main__':

  # encoding process
  with open('words_alpha.txt', 'r') as f:
    data = f.read()
  f.close()
  encoded_data = encoding(data)

  # decoding process
  with open('encoded_temp.txt', 'w') as f:
    f.write(encoded_data)
  f.close()
  decoded_data = decoding(encoded_data)
   
  # comparing the original with the decoded temp
  print decoded_data == data