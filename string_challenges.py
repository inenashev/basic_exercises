# Вывести последнюю букву в слове
word = 'Архангельск'
# ???
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.count('а'))
print(word.lower().count('а')) #если привести к регистру
# ???


# Вывести количество гласных букв в слове
word = 'Архангельск'
#v_string = "«а» «у» «о» «и» «э» «ы» «я» «ю» «е» «ё»"
#vowels = v_string.replace("«", "").replace("»", "").split(" ")
lower_case_word = word.lower()
vowels = ['а', 'у', 'о', 'и', 'э', 'ы', 'я', 'ю', 'е', 'ё']
#print(len(set(lower_case_word) & set(vowels)))
vowel_count = 0
for char in lower_case_word:
    if char in vowels:
        vowel_count +=1
print(f'Число гласных букв: {vowel_count}')
# ???

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split(" ")))
# ???


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split(" "):
    print(word[0])
# ???


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words_len = []
for word in sentence.split(" "):
    words_len.append(len(word))

print(sum(words_len)/len(sentence.split(" ")))
# ???