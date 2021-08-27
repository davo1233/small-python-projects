from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Category(ABC):
    """an abstract representation of each category in a budget notebook"""
    @abstractmethod
    def deposit_funds(self, deposit):
        """deposit funds to each category"""

    @abstractmethod
    def withdraw_funds(self, withdraw):
        """withdraw funds from the relevant category"""

    @abstractmethod
    def get_funds(self) -> float:
        """gets the amount of funds in each class"""


@dataclass
class Food(Category):
    """A representation of the budget of food"""
    category: Category
    food_funds: float = 0

    def deposit_funds(self, deposit):
        self.food_funds += deposit

    def withdraw_funds(self, withdraw):
        self.food_funds -= withdraw

    def get_funds(self) -> float:
        return self.food_funds

    def transfer_funds_between_categories(self,category,amount:float):
        self.food_funds -= amount
        category.deposit_funds(amount)


@dataclass
class Clothing(Category):
    """A class representation of the budget of clothing"""
    category: Category
    clothing_funds: float = 0

    def deposit_funds(self, deposit):
        self.clothing_funds += deposit

    def withdraw_funds(self, withdraw):
        self.clothing_funds -= withdraw

    def get_funds(self) -> float:
        return self.clothing_funds

    def transfer_funds_between_categories(self,category,amount:float):
        self.clothing_funds -= amount
        category.deposit_funds(amount)


@dataclass
class Entertainment(Category):
    """A class representation of the class for entertainment"""
    category: Category
    entertainment_funds: float = 0

    def deposit_funds(self, deposit):
        self.entertainment_funds += deposit

    def withdraw_funds(self, withdraw):
        self.entertainment_funds -= withdraw

    def get_funds(self) -> float:
        return self.entertainment_funds

    def transfer_funds_between_categories(self,category,amount:float):
        self.entertainment_funds -= amount
        category.deposit_funds(amount)


@dataclass
class Budget:
    category: Category
    balance: float = 0

    def deposit_funds_to_category(self, balance):
        self.category.deposit_funds(balance)

    def withdraw_funds_from_category(self, balance):
        self.category.withdraw_funds(balance)

    def deposit_funds(self, deposit):
        self.balance += deposit

    def withdraw_funds(self, withdraw):
        self.balance -= withdraw

    def get_budget(self) -> float:
        return self.balance


def main():
    food = Food()
    budget = Budget(food)
    budget.deposit_funds(10)
    print(budget.balance)


if __name__ == '__main__':
    main()
