from services.similarity import SimilarityService


def main(reference, target):
    similarity_service = SimilarityService()
    return similarity_service.calculate(reference, target)


# if __name__ == "__main__":
#     result = main('caneta azul', 'azul caneta')
#     print(result)
