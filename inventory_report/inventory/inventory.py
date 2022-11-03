from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @classmethod
    def openFile(cls, filePath):
        if filePath.endswith(".csv"):  # endswith pegar o fim do paramentro
            with open(filePath, "r") as file:
                inventory = list(csv.DictReader(file))
                return inventory

        if filePath.endswith(".json"):
            with open(filePath, "r") as file:
                inventory = list(json.load(file))
                return inventory

        if filePath.endswith(".xml"):
            with open(filePath, "r") as file:
                inventory = xmltodict.parse(file.read())["dataset"]["record"]
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
