import re
from unidecode import unidecode
from number_parser import parse_ordinal
from synthesizer.utils.amh_num import num_to_word

# text = 'fiftieth, thirty-two one million, two hundred fifty-two thousand, two hundred thirty-two twenty-first birthday'

def eng_ordinal_to_amh_ordinal(text:str):
    '''Recieves a ordinal text of numbers in english and translates them to amharic ordinals, 
    it also removes punctuations
    example:
    input: fiftieth, thirty-two one million, two hundred fifty-two thousand, two hundred thirty-two twenty-first birthday
    ...
    return: ኃምሳኛ ሰላሳ ሁለት አንድ ትሪሊዮን ሁለት መቶ ኃምሳ ሁለት ሺህ ሁለት መቶ ሰላሳ ሁለት ሃያ አንድኛ birthday
    '''
    words = text.replace('-',' ')

    pattern = r'\b\w+(?:st|nd|rd|th)\b' # rank suffixes in word not digits
    matches = re.findall(pattern, words)

    words = [re.sub(r'[^a-zA-Z]', '', word) for word in words.split(" ")]

    ordinals = [parse_ordinal(word) for word in words]

    for idx,items in enumerate(ordinals):
        if (items != None):
            amh_word = num_to_word(items).strip().split(' ')[-1]
            if words[idx] in matches and words[idx] != 'thousand':
                amh_word += 'ኛ'
            words[idx] = amh_word

    return ' '.join(words)

def english_ordinal_correction(text):
    text = eng_ordinal_to_amh_ordinal(text)
    return unidecode(text)
    
    

