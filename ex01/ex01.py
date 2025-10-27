def group_anagrams(str_list: list[str]) -> list[list[str]]:
    anagrams = {}
    
    for word in str_list:
        sorted_word = ''.join(sorted(word))
        
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    
    return list(anagrams.values())

if __name__ == "__main__":
    input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(input_list)
    print(result)