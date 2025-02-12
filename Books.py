class Book:
    def __init__(self, name, price, category, description, stars, stock):
        self.name = name
        self.price = price
        self.category = category
        self.description = description
        self.stars = stars
        self.stock = stock
    def toDict(self):
        return {
            "name" : self.name,
            "price" : self.price,
            "category": self.category,
            "description": self.description,
            "stars": self.stars,
            "stock" : self.stock
        }