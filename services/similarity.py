from services.string_cleaner import StringCleaner
from services.jaccard import compute_jaccard_similarity_score
from Levenshtein import distance


def _calculate_similarity(distance_num, divisor):
    similarity = 100.00 - ((distance_num * 100.00) / divisor)
    return similarity


def _get_divisor(reference, target):
    if len(reference) > len(target):
        return float(len(reference))
    else:
        return float(len(target))


class SimilarityService:

    def __init__(self):
        self.similarity_percentage_accepted = 70.00
        self.jaccard_percentage_accepted = 70.00
        self.string_cleaner = StringCleaner()

    def _clear_string(self, target):
        return self.string_cleaner.remove_stop_words(target)

    def match(self, result):
        if result['similarity'] >= 85.00 or result['jaccard'] >=85.00:
            return 'match'
        if result['similarity'] >= 65.00 and result['similarity'] <= 84.99 or result['jaccard'] >= 65.00 and result['jaccard'] <= 84.99:
            return 'inconclusive'      
        return 'no_match'

    def calculate(self, reference, target):
        result = {}
        clear_reference = self._clear_string(reference).lower()
        clear_target = self._clear_string(target).lower()

        distance_result = distance(clear_reference, clear_target)
        divisor = _get_divisor(clear_reference, clear_target)

        similarity_result = _calculate_similarity(distance_result, divisor)
        result['similarity'] = round(similarity_result, 2)

        jaccard_result = compute_jaccard_similarity_score(reference, target)
        result['jaccard'] = round(jaccard_result, 2)

        result['matched'] = self.match(result)
        return result





