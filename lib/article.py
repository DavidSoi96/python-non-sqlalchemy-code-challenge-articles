class Article:
    all = []

    def __init__(self, author, magazine, title):
        from classes.many_to_many import Author, Magazine

        if not isinstance(author, Author):
            raise Exception("Author must be an Author object")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be a Magazine object")
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise Exception("Title must be between 5 and 50 characters")

        self._author = author
        self._magazine = magazine
        self._title = title

        author._articles.append(self)
        magazine._articles.append(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        from classes.many_to_many import Author
        if not isinstance(new_author, Author):
            raise Exception("Author must be an Author object")
        self._author._articles.remove(self)
        new_author._articles.append(self)
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        from classes.many_to_many import Magazine
        if not isinstance(new_magazine, Magazine):
            raise Exception("Magazine must be a Magazine object")
        self._magazine._articles.remove(self)
        new_magazine._articles.append(self)
        self._magazine = new_magazine


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        from classes.many_to_many import Article
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list({article.magazine.category for article in self._articles})