def compute_jaccard_similarity_score(element_x, element_y):
    intersection_cardinality = len(set(element_x).intersection(set(element_y)))
    union_cardinality = len(set(element_x).union(set(element_y)))
    return 100 * (intersection_cardinality / float(union_cardinality))

