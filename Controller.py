import csv
import pandas as pd
from BotSpread import Bot

from Model import Model
from View import View


class Controller:

    def __init__(self):
        self.view = View(self)
        self.model = Model()

    def main(self):
        self.view.main()

if __name__ == '__main__':

    controller_instance = Controller()
    controller_instance.main()