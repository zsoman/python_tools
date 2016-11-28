
# coding: utf-8

# # Excercises for Day 4: Sequences
# 
# [4.1 Strings](#4.1)
# 
# [4.2 Lists](#4.2)
# 
# [4.3 Dictionaries](#4.3)
# 
# [4.4 The _collections_ module](#4.4)

# ## 4.1 Strings
# <a id='4.1'></a>

# ### 4.1.1
# Define a function that splits a text into sentences (on ".", "!", "?", etc.)

def split_to_sentences(text):
    return text.replace('!', '.').replace('?', '.').split('.')


# Define a function that splits sentences into words, and strips punctuation marks (",", ";", etc.) from edges of words.

def split_sentences_to_words(sentence):
    words = []
    for word in sentence.split():
        words.append(word.strip(',;:'))
    return words


# Use the last two functions in one that takes a filename as its argument and returns the text in the file as a list of lists. Test it on the file "data/sample_text.txt"

def splitter(file='data/sample_text.txt'):
    all_words = []
    
    f = open(file)
    text = f.read()
    for sentence in split_to_sentences(text):
        all_words += split_sentences_to_words(sentence)
    f.close()
    return all_words
        
result=splitter()
for a, b, c, d in zip(result[::4], result[1::], result[2::4], result[3::4]):
    print("{:<30}{:<30}{:<30}{:<}".format(a, b, c, d))


# ### 4.1.2
# Use the functions defined in __4.1.1__ and define a function that goes through a text and replaces all proper names (capitalized words not at the beginning of a sentence) with "Joe". Print the first few sentences to test your solution.

def change_names(text, name='Joe'):
    sentence_list=split_to_sentences(text)
    all_words = []
    for sentence in sentence_list:
        words=split_sentences_to_words(sentence)
        if len(words)>0:
            all_words.append(words[0])
        for word in words[1:]:
            if word[0].isupper():
                word=name
            all_words.append(word)
    return all_words

with open('data/sample_text.txt') as f:
    text=f.read()
    result=change_names(text, 'Joe')
    for a, b, c, d in zip(result[::4], result[1::], result[2::4], result[3::4]):
        print("{:<30}{:<30}{:<30}{:<}".format(a, b, c, d))


# ### 4.1.3
# Load the sample text using your function from __4.1.1__ and create a game where the user is shown a half of a word in a small context (e.g. "_Many solu\*\*\*\*\* were suggested_") and has to guess the full word (don't worry about randomization, your solution can come up with the same questions every time).

from random import randint
def word_randomizer(words_to_randomize_from):
    random_number = randint(0, len(words_to_randomize_from)-2)
    return '{} {} {}'.format(words_to_randomize_from[random_number-1], words_to_randomize_from[random_number],
                            words_to_randomize_from[random_number+1])

def half_word(word, character='*'):
    return word.replace(word.split()[1], word.split()[1][:len(word.split()[1])/2]+character*(len(word.split()[1])/2))

def word_game(words=splitter('data/sample_text2.txt')):
    guess='start'
    while guess != 'end game':
        random_word=word_randomizer(words)
        print(half_word(random_word))
        guess = raw_input("Your guess is:")
        while guess != random_word.split()[1] and guess != 'new game' and guess != 'end game':
            guess = raw_input("Your new guess is:")
        if guess == random_word.split()[1]:
            print("Correct!")
        elif guess != 'new game':
            print("I hope you enjoyed it!")
            
word_game()            


# ## 4.2 Lists
# <a id='4.2'></a>

# ### 4.2.1
# Define a function that takes as its input a list of $n$ lists of $n$ numbers (a square matrix) and decides if it is symmetric (i.e. $A[i,j] == A[j,i]$ for all $i, j$).

# In[ ]:

def is_symetric_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True
            
matrix=[[1, 7, 3, 9],
       [7, 4, -5, 0],
       [3, -5, 6, -1],
       [9, 0, -1, 10]]
print(is_symetric_matrix(matrix))


# ### 4.2.2
# Define a function that takes a list containing lists of equal length (i.e. a table of size $n\times k$) and "transposes" it, creating a table of size $k\times n$.

# In[ ]:

from sys import stdout

def transpose_matrix(matrix):
    new_matrix=[]
    for j in range(len(matrix[0])-1,-1,-1):
        row=[]
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        new_matrix.append(row)
    return new_matrix

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            stdout.write("{:^5}".format(matrix[i][j]))
        print("")
matrix=[[1, 7, 3, 9],
       [7, 4, -5, 0],
       [3, -5, 6, -1]]
print_matrix(transpose_matrix(matrix))


# ### 4.2.3
# Redo 4.2.3 using nested list comprehension!

# In[ ]:

matrix=[[1, 7, 3, 9],
       [7, 4, -5, 0],
       [3, -5, 6, -1]]
new_matrix=[[row[i] for row in matrix] for i in range(len(matrix[0])-1, -1, -1)]
print_matrix(new_matrix)


# ### 4.2.4

# Define a function that takes a list and string, then returns all elements that start with the string, along with their indices in the list.

# In[ ]:

def elements_that_stat_with(elements, string):
    result=[]
    for i, element in enumerate(elements):
        if element.startswith(string):
            result.append((element, i))
    return result

elements=['aaaab', 'aaaas', 'ssb', 'aab', 'a', 'sssb', 'bbbbaaaaa']
print(elements_that_stat_with(elements,'a'))


# ## 4.3 Dictionaries
# <a id='4.3'></a>

# ### 4.3.1
# Use a dictionary to count words in our sample text (use your text processing functions!). Then print the most common words, along with their frequencies!

# In[ ]:

def count_words(words=splitter()):
    nr_of_words={}
    for word in words:
        if word in nr_of_words:
            nr_of_words[word]+=1
        else:
            nr_of_words[word]=1
    return nr_of_words

print(count_words())


# ### 4.3.2

# Define function that performs the factorial operation ($n!$) but caches all results so that each call requires the least possible number of multiplications.

# In[ ]:

store_factorial={0:1, 1:1}    

def cached_factorial(n):
    if n in store_factorial:
        return store_factorial[n]
    else:
        maximum=max(store_factorial.keys())
        for i in range(maximum+1,n+1):
            store_factorial[i]=store_factorial[i-1]*i
        return store_factorial[n]

readed=1
while readed!=0:
    try:
        readed = int(raw_input())
        print("{}! = {}".format(readed, cached_factorial(readed)))
    except TypeError:
        pass


# ### 4.3.3
# Read the dataset in "data/movies.tsv" and store it in a dictionary whose keys are genres and the values are list of tuples of title and year

# In[ ]:

def store_movies(file='data/movies.tsv'):
    movies_map={}
    with open(file) as f:
        for line in f:
            title, year, generes = line.split('\t')
            splitted_generes = generes.split(',')
            for genere in splitted_generes:
                genere=genere.strip()
                if genere in movies_map:
                    movies_map[genere].append((title, year))
                else:
                    movies_map[genere]=[(title, year)]
    return movies_map

for genere_key, movies_value in store_movies().items():
    print("{} - {}".format(genere_key, movies_value))


# ### 4.3.4
# Process the movies dataset (the original file or the dictionary built in __4.3.3__) and build a dictionary that indexes movies by the first letter of the title. Then create a small interface for querying (using the input function)

# In[ ]:

movies={}
def movies_by_letter(file='data/movies.tsv'):
    movies_map={}
    with open(file) as f:
        for line in f:
            title, _, _ = line.split('\t')
            if title[0].lower() in movies_map:
                movies_map[title[0].lower()].append(title.strip())
            else:
                movies_map[title[0].lower()]=[title.strip()]
    return movies_map

def get_movies_by_letter(movies, leter):
    leter = leter.lower()
    if leter in movies:
        str_movies=''
        for movie in movies[leter]:
            str_movies+=str(movie)+', '
        print("Movie names starting with {}:\n{}".format(leter.upper(), str_movies[:-2]))
        
movies=movies_by_letter()
leter='A'
while leter != 'stop':
    leter = raw_input('Give me a leter: ')
    while 0 < len(leter) > 1 and leter != 'stop':
        leter = raw_input('Give me a leter or stop! ')
    if leter != 'stop':
        get_movies_by_letter(movies, leter)


# ### 4.3.5
# Build an incremental search of movie titles: users should be able to narrow the set of movies with every character they type. You may create deeply nested dictionaries beforehand or process the data on-the-fly.

# In[4]:

def build_index(data):
    for movie in data:
        title = movie[0]
        try:
            a, b, c = title[:3]
        except ValueError:
            print("skipping {}".format(title))
        a=a.lower()
        b=b.lower()
        c=c.lower()
        if a not in letter_index:
            letter_index[a]={}
        if b not in letter_index[a]:
            letter_index[a][b]={}
        if c not in letter_index[a][b]:
            letter_index[a][b][c]={}
        letter_index[a][b][c].append(movie)
    return letter_index
        
def search(fn):
    data = [(title.strip(), int(year), genres.split(','))
           for title, year, genres in [line.strip().split('\t') 
                                       for line in open(fn)]]
    letter_index = build_index(data)
    letter1 = raw_input().lower()
    print(letter_index[letter1])
    letter2 = raw_input().lower()
    print(letter_index[letter1][letter2])
    letter3 = raw_input().lower()
    print(letter_index[letter1][letter2][letter3])
    
search('data/movies.tsv')
    


# In[12]:

def unify_dicts(dict1, dict2):
    dict3={}
    dict3.update(dict1)
    for key, value in dict2.items():
        if key not in dict3:
            dict3[key]=value
        else:
            if not isinstance(dict3[key], dict):
                dict3[key]=value
            else:
                dict3[key] = unify_dicts(dict3[key], value)
    return dict3

def get_letter_dict(title, movie):
    if not title:
        return {'@':movie}
    else:
        return {title[0]: get_letter_dict(title[1:], movie)}

def build_index(data):
    letter_index={}
    for movie in data:
        title = movie[0]
        d = get_letter_dict(title, movie)
        letter_index=unify_dicts(letter_index,d)
        letter_index.update(d)
    return letter_index
        
def search(fn):
    data = [(title.strip(), int(year), genres.split(','))
           for title, year, genres in [line.strip().split('\t') 
                                       for line in open(fn)]]
    letter_index = build_index(data)
    letter = raw_input()
    curr_dict = letter_index[letter]
    while True:
        print(curr_dict)
        if '@' in curr_dict:
            print(curr_dict['@'])
            break
        else:
            letter=raw_input()
            if letter not in curr_dict:
                print("Not found!")
                break
            curr_dict=curr_dict[letter]
search('data/movies.tsv')


# ## 4.4 The _collections_ module
# <a id='4.4'></a>

# ### 4.4.1
# Modify the word counter in __4.3.1__ so that it uses a defaultdict.

# In[ ]:

from collections import defaultdict
def count_words(words=splitter()):
    nr_of_words=defaultdict(int)
    for word in words:
        nr_of_words[word]+=1
    return nr_of_words

print(count_words())


# ### 4.4.2
# Modify the word counter in __4.4.1__ so that it uses a Counter.

# In[ ]:

from collections import Counter
def count_words(words=splitter()):
    nr_of_words=Counter()
    for word in words:
        nr_of_words[word]+=1
    return nr_of_words

print(count_words())


# ### 4.4.3
# Define a function that queries users for their last name, first name, year of birth, and hobby, and populates an OrderedDict whose keys are the last names and values are dictionaries with four keys each. If a second person with the same last name is encountered, both should now have keys of the form "lastname_firstname". If the same person is encountered multiple times, his/her data should be updated. Then test the solution of someone else and ask her to test yours.

# In[13]:

from collections import OrderedDict

peoples= OrderedDict()

def add_people(data):
    global peoples
    name=data[0]+'_'+data[1]
    if name in peoples:
        peoples[name]={'last_name': data[0],'frist_name': data[1], 'year_of_brth': data[2], 'hobby': data[3]}
    elif data[0] in peoples:
        new_name=peoples[data[0]]['last_name']+'_'+peoples[data[0]]['frist_name']
        peoples[new_name]=peoples[data[0]]
        del peoples[data[0]]
        peoples[name]={'last_name': data[0],'frist_name': data[1], 'year_of_brth': data[2], 'hobby': data[3]}
    else:
        peoples[data[0]]={'last_name': data[0],'frist_name': data[1], 'year_of_brth': data[2], 'hobby': data[3]}
        
readed = 'start'
while readed != 'stop':
    readed = raw_input('People: ')
    if readed!='stop':
        add_people(readed.split(';'))
        print(peoples)


# ### 4.4.4
# Convert the database built in __4.4.3__ into a list of namedtuples.

# In[ ]:

from collections import namedtuple
from collections import OrderedDict

peoples= OrderedDict()
People = namedtuple('People', ['last_name','frist_name','year_of_brth','hobby'])

def add_people(data):
    global peoples
    name=data[0]+'_'+data[1]
    if name in peoples:
        peoples[name]=People(data[0], data[1], data[2], data[3])
    elif data[0] in peoples:
        new_name=peoples[data[0]].last_name+'_'+peoples[data[0]].frist_name
        peoples[new_name]=peoples[data[0]]
        del peoples[data[0]]
        peoples[name]=People(data[0], data[1], data[2], data[3])
    else:
        peoples[data[0]]=People(data[0], data[1], data[2], data[3])
        
readed = 'start'
while readed != 'stop':
    readed = raw_input('People: ')
    if readed!='stop':
        add_people(readed.split(';'))
        print(peoples)


# In[ ]:



