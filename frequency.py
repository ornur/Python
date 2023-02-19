def frequency_dictionary(words):
    freq_dict = {}
    for word in words:
        if word not in freq_dict.keys():
            freq_dict[word] = 1
        else:
            freq_dict[word] += 1
    return freq_dict


sentence = "Ski-bi dibby dib yo da dub dub Yo da dub dub"
l_sen = sentence.lower()
sen_list = l_sen.split()
if len(sen_list)<3:
    print("None")
else:
    result_dict = {}
    full_dict = frequency_dictionary(sen_list)
    for i in range(2):
        for x, y in list(full_dict.items()):
            if max(full_dict.values()) == y:
                result_dict.update({x: y})
                del full_dict[x]

    print(result_dict)