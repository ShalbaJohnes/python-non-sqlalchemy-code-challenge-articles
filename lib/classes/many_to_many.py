class Article:
    all = []   # A shared list that keeps track of every Article ever created

    def __init__(self, author, magazine, title):
        # Title must be a proper string within a realistic length range
        if not isinstance(title, str):
            raise Exception("Title must be a string.")
        if not (5 <= len(title) <= 50):
            raise Exception("Title must be between 5 and 50 characters.")

        # Confirm that author and magazine are the correct object types
        if type(author).__name__ != 'Author':
            raise Exception("Author must be of type Author.")
        if type(magazine).__name__ != 'Magazine':
            raise Exception("Magazine must be of type Magazine.")

        self._title = title
        self._author = author
        self._magazine = magazine

        # Add this article to the global registry of all articles
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        pass  # Title never changes after the article is created

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        # A different author can be reassigned but must still be an Author object
        if type(value).__name__ != 'Author':
            raise Exception("Author must be of type Author.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        # A new magazine can be set but must still be a Magazine object
        if type(value).__name__ != 'Magazine':
            raise Exception("Magazine must be of type Magazine.")
        self._magazine = value


class Author:
    def __init__(self, name):
        # Name must exist and actually be text the user typed
        if not isinstance(name, str):
            raise Exception("Name must be a string.")
        if len(name) == 0:
            raise Exception("Name must be longer than 0 characters.")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        pass  # Authors never change their names once stored

    def articles(self):
        # Return only the articles written by this author
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        # Return a unique list of magazines this author has written for
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        # Shortcut for creating a new Article tied to this author
        return Article(self, magazine, title)

    def topic_areas(self):
        # Show the unique list of magazine categories the author has written for
        articles = self.articles()
        if not articles:
            return None
        return list(set([article.magazine.category for article in articles]))


class Magazine:
    def __init__(self, name, category):
        # Magazine name must be short and clear (like real magazine brands)
        if not isinstance(name, str):
            raise Exception("Name must be a string.")
        if not (2 <= len(name) <= 16):
            raise Exception("Name must be between 2 and 16 characters.")
        self._name = name

        # Category tells the type of magazine (e.g., Tech, Fashion, Sports)
        if not isinstance(category, str):
            raise Exception("Category must be a string.")
        if len(category) == 0:
            raise Exception("Category must be longer than 0 characters.")
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Silent fail if the update isn't valid — avoids breaking the program
        if not isinstance(value, str):
            return
        if not (2 <= len(value) <= 16):
            return
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        # Silent fail if the update isn't suitable
        if not isinstance(value, str):
            return
        if len(value) == 0:
            return
        self._category = value

    def articles(self):
        # Returns every article that belongs to this magazine
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        # Returns all unique authors who wrote in this magazine
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        # Shows the titles of the articles in this magazine, or None if none exist
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        # Returns authors who have written more than 2 articles for this magazine
        from collections import Counter
        authors = [article.author for article in self.articles()]
        author_counts = Counter(authors)
        result = [author for author, count in author_counts.items() if count > 2]
        return result if result else None