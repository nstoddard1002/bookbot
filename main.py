def main():
    f = open("books/frankenstein.txt","r")
    text = f.read()
#this splits the string into words, and then counts them
    words = text.split()
    word_count = len(words)

#these are used to count the letters and then sort them later on
    letters = {}
    sorted_letters = []


    for word in words:
        #this first lowers the case of all the letters in the word
        lword = word.lower()
        #this determines how many letters are in the word
        word_length = len(lword)
        i = 0
        #this runs through the letters in the word
        while i < word_length:
            #this sets letter to each character in the word 
            letter = lword[i]
            #this tests if there is already an entry for the character
            #if no entry, it adds the entry and sets the counter to 1
            if letter in letters:
                j = letters[letter]
                j += 1
                letters[letter] = j
            else:
                letters[letter] = 1
            i += 1
    #this goes through each item in the letters dictionary
    for item in letters:
        #this is the blank dictionary that we will be adding to our list
        temp_new = {}
        dummy_string = ""
        temp_new["character"] = item
        temp_new["num"] = letters[item]
        dummy_string = str(item)
        #this only adds the dictionary entry to the sorted list if it's alphabetic
        if dummy_string.isalpha():
            sorted_letters.append(temp_new)
    
    #this is the sort method recommended by boots
    def sort_on(dict):
        return dict["num"]
    #this sorts the list of dictionarys based on the "num" id
    sorted_letters.sort(reverse=True, key=sort_on)

    
  
            
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("")
    
    
    for sorted_item in sorted_letters:
        print(f"The \'{sorted_item["character"]}\' character was found {sorted_item["num"]} times")



    print("--- End report ---")
    


main()
