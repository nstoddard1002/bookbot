def main():
    f = open("books/frankenstein.txt","r")
    text = f.read()
    words = text.split()
    word_count = len(words)
    letters = {}
    sorted_letters = []

    for word in words:
        lword = word.lower()
        word_length = len(lword)
        i = 0
        while i < word_length:
            letter = lword[i]
            if letter in letters:
                j = letters[letter]
                j += 1
                letters[letter] = j
            else:
                letters[letter] = 1
            i += 1
    
    for item in letters:
        temp_new = {}
        dummy_string = ""
        temp_new["character"] = item
        temp_new["num"] = letters[item]
        dummy_string = str(item)
        if dummy_string.isalpha():
            sorted_letters.append(temp_new)
    
    def sort_on(dict):
        return dict["num"]

    sorted_letters.sort(reverse=True, key=sort_on)

    
  
            
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("")
    
    
    for sorted_item in sorted_letters:
        print(f"The \'{sorted_item["character"]}\' character was found {sorted_item["num"]} times")



    print("--- End report ---")
    


main()
