stack = []
def push(text):
    feats = find_features(text)
    return voted_classifier.classify(feats),voted_classifier.confidence(feats)
def pop(text):
    feats = find_features(text)
    return voted_classifier.classify(feats),voted_classifier.confidence(feats)
def top(text):
    feats = find_features(text)
    return voted_classifier.classify(feats),voted_classifier.confidence(feats)