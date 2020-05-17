class StringCleaner:
    stop_words = [
        "faixa",
        "larg fita",
        "espes",
        "acabamento",
        "diametro",
        ",", ".", ":", "-"
    ]

    def remove_stop_words(self, target_string):
        for stop_word in self.stop_words:
            target_string = target_string.replace(stop_word, "")
        return target_string

