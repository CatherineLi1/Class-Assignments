# Catherine Li


# Enhancement: Comparing changes in time and percent of questions answered correctly when
    # running different parts of the book:

# When running book1.txt:
    # If 100% of the file is run, 60.00% of the questions were answered correctly.
    #    It took 241.69788479804993 seconds to run.
    # If 50% of the file is run, 60.00% of the questions were answered correctly.
    #    It took 230.7342209815979 seconds to run.
    # If 20% of the file is run, 60.00% of the questions were answered correctly.
    #    It took 243.91933226585388 seconds seconds to run.
    # If 5% of the file is run, 60.00% of the questions were answered correctly.
    #    It took 258.40948700904846 seconds to run.

# When running book2.txt:
    # If 100% of the file is run, 67.50% of the questions were answered correctly.
    #    It took 169.84760189056396 seconds to run.
    # If 50% of the file is run, 67.50% of the questions were answered correctly.
    #    It took 166.83350706100464 seconds to run.
    # If 20% of the file is run, 67.50% of the questions were answered correctly.
    #    It took 164.86534118652344 seconds to run.
    # If 5% of the file is run, 67.50% of the questions were answered correctly.
    #    It took 172.18406701087952 seconds to run.


import math, time

# Please do not alter this function.
def norm(vec):
    '''Return the norm of a vector stored as a dictionary.'''    
    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    return math.sqrt(sum_of_squares)


# Please do not alter this function.
def cosine_similarity(vec1, vec2):
    '''Return the cosine similarity of sparse vectors (dictionaries) vec1 and vec2.'''
    dot_product = 0.0
    for x in vec1:
        if x in vec2:
            dot_product += vec1[x] * vec2[x]
    return dot_product / (norm(vec1) * norm(vec2))


def get_sentence_lists(text):
    '''
    Parameter: text (string)
    Return: a list of list of words, inner list contains words of a different sentence of text
    Note: sentences are separated by ".", "!", and "?".
    '''
    #check the parameter is a string
    if not isinstance(text, str):
        raise ValueError("Parameter text must be a string")
      
    #continue with rest of code
    text = text.lower()
    for i in range(len(text)):
        #change all ! and ? into periods
        if text[i] == "!" or "?":
            text = text.replace("!", ".")
            text = text.replace("?", ".")
        #period separates text into list with elements
        if text[i] == ".":
            delimiter = "."
            list_text = text.split(delimiter)
        
    #delete all empty strings
    while '' in list_text:
        list_text.remove('')
        
    #separate string of words into several strings, one word long
    separate_to_strings = []
    for string in list_text:
        for i in range(len(string)):
            #check if the character is a punctuation mark
            if string[i] in (",-_:;!?.'" or '"'):
                a = string[i]
                string = string.replace(a,' ')
        #now, only letters and spaces are present
        #split the string by spaces
        for i in range(len(string)):
            new = string.split()
            separate_to_strings.append(new)
            break
    return separate_to_strings


def get_sentence_lists_from_files(filenames):
    '''
    Parameter: filenames (list of strings)
    Return: a list of list of words, inner list contains words of a different sentence of text
    Note: same function as get_sentence_lists(text), but need to load file first
    '''
    #check parameter validity
    if not isinstance(filenames, list):
        raise ValueError('Parameter filenames must be a list of strings.')
    for string in filenames:
        if not isinstance(string, str):
            raise ValueError("Parameter filenames must be a list of strings.")
    
    #continue with code
    list_of_list_of_strings = []
    for name_of_file in filenames:
        separate_to_strings = []
        #open file, read its content in lowercase letters, and then close file
        fobj = open(name_of_file, "r")
        content = fobj.read()
        content = content.lower()
        fobj.close()
        
        #convert content into list of list of words
        for i in range(len(content)):
            #change all ! and ? into periods
            if content[i] == "!" or "?":
                content = content.replace("!", ".")
                content = content.replace("?", ".")
            #period separates text into list with elements
            list_content = content #actual words in the file
            if content[i] == ".":
                delimiter = "."
                list_content = content.split(delimiter)
                separate_to_strings.append(list_content) #now separate_to_strings is a list of many strings
                break
        
        #delete all empty strings
        while '' in separate_to_strings:
            list_text.remove('')
        
        #now separate_to_strings is a list of the sentence-lists, there are no empty lists
            #every sentence-list is a list with strings of one word length long
            
        #separate string of words into several strings, one word long each
        for a_list in separate_to_strings:
            for string in a_list:
                for i in range(len(string)):
                    #check if the character is a punctuation mark
                    
                    #change punctuation marks into '-'
                    if string[i] in (",-_:;!?.'" or '"'):
                        a = string[i]
                        string = string.replace(a,' ')
                    '''
                    #now delete all '-' characters
                    if string[i] in "-":
                        word = string.replace('-','')
                    '''
                #split into strings of length one word, add to final list of strings
                list_of_strings = string.split()
                list_of_list_of_strings.append(list_of_strings)
                
    #delete any empty lists
    for list_of_strings in list_of_list_of_strings:
        if list_of_strings == []:
            list_of_list_of_strings.remove(list_of_strings)
            
    return list_of_list_of_strings


def build_semantic_descriptors(sentences):
    '''
    Parameter: sentences (a list which contains lists of sentences)
    Return: a dictionary d for every word w.
    '''
    #check parameter validity
    if not isinstance(sentences, list):
        raise ValueError('Parameter sentences must be a list of lists.')
    
    #let d bet the final dictionary
    #let w be the word
    
    d = {} #create an empty dictionary to represent semantic_descriptor
    new_d = {}
    for sentence_list in sentences:
        for phrase in sentence_list: #phrase is the sentence within the list
            phrase = phrase.split() #now phrase is a list of strings, every string is one word
            for w in phrase:
                if w in d: #continue if word is in dictionary
                    for phrase in sentence_list:
                        phrase = phrase.split()
                        for check_word in phrase:
                            if check_word != w:
                                #add new word or add one count to existing word
                                if check_word in d[w]:
                                    d[w][check_word] += 1 #add one to the value
                                else:
                                    d[w][check_word] = 1 #new key added, set to 1
                else: #word is not in dictionary
                    dict_case2 = {}
                    for phrase in sentence_list:
                        phrase = phrase.split()
                        for check_word in phrase:
                            if check_word != w:
                                if check_word in dict_case2:
                                    dict_case2[check_word] += 1
                                else:
                                    dict_case2[check_word] = 1
                            d[w] = dict_case2
    #delete empty dicitonaries
    new_d = dict(d)
    for word in d:
        if d[word] == {}:
            del new_d[word]
    
    #now, the full dictionary is created
    return new_d


def most_similar_word(word, choices, semantic_descriptors):
    '''
    Parameters: word (string), choices (list), semantic_descriptors (dictionary)
    Return: element in choices list with highest similarity to word.
    Note: if semantic similarity between words cannot be computed, it is -1.
    For ties, use the smaller index in choices.
    '''
    #check parameter validities
    if (not isinstance(word, str)) or (not isinstance(choices, list)) or (not isinstance(semantic_descriptors, dict)):
        raise ValueError('One or more of the parameters are not the correct type.')
    
    #continue with code
    word = word.lower()
    most = 0 #most is the similarity ratio between word and choices
    final = choices[0] #set final as the first element in choices, update as needed
    similarity = most
    
    for string in choices:
        if string not in semantic_descriptors:
            similarity = -1
        else:
            for word in semantic_descriptors:
                if string != word:
                    vec1 = semantic_descriptors[word]
                    vec2 = semantic_descriptors[string]
                    similarity = cosine_similarity(vec1, vec2)
        
        #update the final if another element has higher similarity
        #note: if most is equal to similarity, nothing is changed
            #ie: lower index is kept.
        if most < similarity:
            most = similarity
            final = string
    
    #final is now the word with most similarity in choices
    return final


def run_similarity_test(filename, semantic_descriptors):
    '''
    Parameter: filename (string), semantic_descriptors (dictionary)
    Return: percentage of questions in given file that are correctly guessed by
            most_similar_word().
    '''
    #check parameter validities
    if not isinstance(semantic_descriptors, dict):
        raise ValueError('Parameter semantic_descriptors must be a dictionary.')
    
    #get text inside the file and close file
    fobj = open(filename)
    text = fobj.read()
    fobj.close()
    
    text = text.split("\n") #split file by every new line
    number_total = len(text) #total number used to divide by later
    
    number_correct = 0
    
    for i in range(len(text)):
        text[i] = text[i].split() #split text by spaces
        
        word = most_similar_word(text[i][0], text[i][2:], semantic_descriptors)
        if text[i][1] == word:
            number_correct += 1
            
    decimal = number_correct/number_total
    return decimal


# Please do not alter anything below this line.
if __name__ == '__main__':
    time_start = time.time()
    
    sentences = get_sentence_lists_from_files(["book1.txt", "book2.txt"])
    descriptors = build_semantic_descriptors(sentences)
    percentage = run_similarity_test("test.txt", descriptors)
    print("Percentage of questions correctly answered: {:.2f}%".format(percentage*100))
    
    time_end = time.time()
    time_total = time_end - time_start
    print("The time it took to run the code is: {} seconds.".format(time_total))