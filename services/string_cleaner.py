class StringCleaner:
    auxiliary_verbs = [' o ', ' a ', ' c ', ' d ', ' lhe ', ' se ', ' si ', ' os ', ' as ', ' lhes ', ' um ', " por ", ' pelo ', ' per ',
                       ' pelo ', ' pelos ', ' pela ', ' pelas ', ' no ', ' nos ', ' do ', ' dos ', ' de ', ' em ', ' ao ', ' aos ', " com "]
    stop_words = [
        "faixa",
        "cor",
        "larg fita",
        "espes",
        "diametro",
        "dimensao",
        "tipo",
        ",", ".", ":", "-", ";", "(", ")", "referencia", "p/", "parte", " / ", " + "
    ] + auxiliary_verbs

    def remove_stop_words(self, target_string):
        for stop_word in self.stop_words:
            target_string = target_string.lower()
            target_string = target_string.replace(stop_word, " ")
            target_string = target_string.replace('á', 'a')
            target_string = target_string.replace('ã', 'a')
            target_string = target_string.replace('â', 'a')
            target_string = target_string.replace('õ', 'o')
            target_string = target_string.replace('ö', 'o')
            target_string = target_string.replace('ô', 'o')
            target_string = target_string.replace('ó', 'o')
            target_string = target_string.replace('ç', 'c')
            target_string = target_string.replace('é', 'e')
            target_string = target_string.replace('ê', 'e')
            target_string = target_string.replace('ú', 'u')
            target_string = target_string.replace('û', 'u')
        return target_string
