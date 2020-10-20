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

    def is_match(self, result):
        if result['similarity'] >= self.similarity_percentage_accepted:
            return True
        if result['jaccard'] >= self.jaccard_percentage_accepted:
            return True
        return False

    def calculate(self, reference, target):
        result = {}
        clear_reference = self._clear_string(reference)
        clear_target = self._clear_string(target)

        distance_result = distance(clear_reference, clear_target)
        divisor = _get_divisor(clear_reference, clear_target)

        similarity_result = _calculate_similarity(distance_result, divisor)
        result['similarity'] = round(similarity_result, 2)

        jaccard_result = compute_jaccard_similarity_score(reference, target)
        result['jaccard'] = round(jaccard_result, 2)

        result['matched'] = self.is_match(result)
        return result





