def compute_jaccard_similarity_score(element_x, element_y):
    ex = set(element_x.split())
    ey = set(element_y.split())
    result = len(ex.intersection(ey)) / ( (len(ex) + len(ey))  - len(ex.intersection(ey)) ) 
    similarity = result * 100
    return similarity