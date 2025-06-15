class ValueChecker:

    @classmethod
    def check(cls, value):
        if value >= 0:
            return value
        else:
            raise ValueError("Отрицательное значение параметра")
