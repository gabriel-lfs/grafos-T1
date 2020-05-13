"""
Gabriel Luís Fernando de Souza
"""

from src.second_question import COLOR


class Vertex:
    def __init__(self, title: int):
        self.title = title
        self.color = COLOR.WHITE
        self.discovery_time = -1
        self.closing_time = -1
        self.parent = None
        self.level = 0
        self.__relation_titles = set()

    @property
    def relation_titles(self):
        return self.__relation_titles

    @relation_titles.setter
    def relation_titles(self, relation):
        self.__relation_titles.add(relation.title)