#DAILY CHALLENGE
class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items if items else []  #liste des éléments
        self.pageSize = int(pageSize)  #NB d'element  par page
        self.totalPages = max(1, (len(self.items) + self.pageSize - 1) // self.pageSize)  # Nombre total de pages
        self.currentPage = 1 