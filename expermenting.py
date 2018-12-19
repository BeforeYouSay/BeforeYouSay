import nltk
from nltk.tokenize import sent_tokenize
simple_conversions = {'Can I': 'May I'}
with open('bad_words.txt', 'r') as f:
    bad_words = [word.strip() for word in f.readlines()[13:]]

def convert_simple_stuff(content):
    for simple_conversion in simple_conversions:
        content = content.replace(simple_conversion, simple_conversions[simple_conversion])
    return content

def add_please(content):
    sentences = sent_tokenize(content)
    new_sentences = sentences
    print 'sentences', sentences

    for sentence in sentences:
        tokenized_words = nltk.word_tokenize(sentence)
        tags_with_words = nltk.pos_tag(tokenized_words)
        new_tags_with_words = tags_with_words[:]
        n = 0

        for i, tag_with_word in enumerate(tags_with_words):
            if tag_with_word[1] in ['VBP', 'VB'] and not tags_with_words[i][0] == 'please':
                new_tags_with_words.insert(i+n, ('please', ''))
                n += 1
            if tag_with_word[1] == 'NNP' and not tag_with_word[0] in ['May']:
                new_tags_with_words[i+n] = (tag_with_word[0].lower(), tag_with_word[1])
                new_tags_with_words.insert(i+n, ('Please', ''))
                n += 1
        sentence = ' '.join([x[0] for x in new_tags_with_words])
        indices = [i for i, x in enumerate(content) if x in ['.', '!', '?']]
        for n, i in enumerate(indices):
            sentence = sentence[:i-1-n]+sentence[i-n:]
        new_sentences.append(sentence)
        print sentence
    return ' '.join(new_sentences)

def clean_content(content):
    content = convert_simple_stuff(content)
    content = add_please(content)
    return content

def is_it_safe_to_say(content):
    for bad_word in bad_words:
        if bad_word in content:
            return False
    return True

def flag_bad_words(content):
    for bad_word in bad_words:
        if bad_word in content:
            content = content.replace(bad_word, '<badword>'+bad_word+'</badword>')
    return content


print flag_bad_words('I hate you, fuck you!')
print clean_content('Can I go to the mall? Can I drive to the mall? Run to the mall. I want to go to the mall.')
