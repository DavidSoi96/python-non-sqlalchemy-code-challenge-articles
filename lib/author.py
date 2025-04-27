class Author:
    def __init__(self, name):
        if not isinstance(name, str) or not name:
            raise Exception("Name must be a non-empty string")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name 

    @property
    def articles(self):
        return self._articles 

    @property
    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        from classes.many_to_many import Article
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self._articles:
            return None
        return list({article.magazine.category for article in self._articles})
