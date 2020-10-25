class StringCleaner:
    auxiliary_verbs = [' o ', ' a ', ' c ', ' d ', ' lhe ', ' se ', ' si ', ' os ', ' as ', ' lhes ', ' um ', " por ", ' pelo ', ' per ',
                       ' pelo ', ' pelos ', ' pela ', ' pelas ', ' no ', ' nos ', ' do ', ' dos ', ' de ', ' em ', ' ao ', ' aos ', " com "]
    stop_words = [
        "faixa",
        "cor",
        "larg fita",
        "espes",
        "diametro",
        "tipo",
        ",", ".", ":", "-", ";", "(", ")", "referencia", "p/", "parte", " / ", " + "
    ] + auxiliary_verbs

    def remove_stop_words(self, target_string):
        for stop_word in self.stop_words:
            target_string = target_string.lower()
            target_string = target_string.replace(stop_word, " ")

        return target_string
