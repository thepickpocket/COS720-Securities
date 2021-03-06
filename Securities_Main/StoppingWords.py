# COS 720 Securities
# Assignment by Jason R. Evans 13032608 & Vivian L. Venter 13238435
# Project 14

class StopWords:
    Words = [
        "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't", "arent",
        "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can't",
        "cant", "cannot", "could", "couldn't", "couldnt", "did", "didn't", "didn't", "do", "does", "doesn't", "doesnt", "doing", "don't", "dont", "down",
        "during", "each", "few", "for", "from", "further", "had", "hadn't", "hadnt", "has", "hasn't", "hasnt", "have", "haven't", "havent", "having",
        "he", "he'd", "hed", "he'll", "hell", "he's", "hes", "her", "here", "here's", "heres", "hers", "herself", "him", "himself", "his", "how",
        "how's", "hows", "i", "i'd", "id", "i'll", "ill", "i'm", "im", "i've", "ive", "if", "in", "into", "is", "isn't", "isnt", "it", "it's", "its", "itself",
        "let's", "lets", "me", "more", "most", "mustn't", "mustnt", "my", "myself", "no", "nor", "not", "of", "off", "on", "once", "only",
        "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "shant", "she", "she'd", "shed",
        "she'll", "shell", "she's", "shes", "should", "shouldn't", "shouldnt", "so", "some", "such", "than", "that", "that's", "thats", "the", "their",
        "theirs", "them", "themselves", "then", "there", "there's", "theres", "these", "they", "they'd", "theyd", "they'll", "theyll", "they're", "theyre",
        "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we",
        "we'd", "wed", "we'll", "well", "we're", "were", "we've", "weve", "were", "weren't", "werent", "what", "what's", "whats", "when", "when's", "whens", "where", "where's", "wheres",
        "which", "while", "who", "who's", "whos", "whom", "why", "why's", "whys", "with", "won't", "wont", "would", "wouldn't", "wouldnt", "you", "you'd", "youd",
        "you'll", "youll", "you're", "youre", "you've", "youve", "your", "yours", "yourself", "yourselves", "get", "via", "just",
        "new", "like", "can", "day", "go", "see", "now", "will", "know", "got", "going", "getting", "one", "good", "u", "i", "want",
        "much", "us", "come", "check", "first", "really", "say", "need", "make", "look"
    ]

    Punctuation = [".", "!", "?", ":", ";", ",", "-", "(", ")", "'", '"', '\\', '/', '&']