from services.similarity import SimilarityService


def main(reference, target):
    similarity_service = SimilarityService()
    return similarity_service.calculate(reference.lower(), target.lower())


# if __name__ == "__main__":
#     result = main('CAneta azul', 'azul caneta')
#     print(result)
