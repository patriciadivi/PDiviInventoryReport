from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    @classmethod
    def openFile(cls, filePath):
        if filePath.endswith(".csv"):  # endswith pega o fim do paramentro
            with open(filePath, "r") as file:
                inventory = list(csv.DictReader(file))
                return inventory

        if filePath.endswith(".json"):
            with open(filePath, "r") as file:
                inventory = list(json.load(file))
                return inventory

    @classmethod
    def import_data(cls, filePath, typePath):
        filePathFinsh = cls.openFile(filePath)

        if typePath == "simples":
            resFinsh = SimpleReport.generate(filePathFinsh)
            return resFinsh

        if typePath == "completo":
            resFinsh = CompleteReport.generate(filePathFinsh)
            return resFinsh
