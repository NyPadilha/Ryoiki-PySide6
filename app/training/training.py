import os
import json
from typing import Dict
from interfaces import TrainingI, PartialTrainingI, TitlessTrainingI


class Training:
    def __init__(self):
        self.path = "database/training.json"
        self.training_list: Dict[str, TitlessTrainingI] = {}

    def create_training(self):
        with open(self.path, "w") as file:
            json.dump(self.training_list, file)

    def read_training(self):
        if os.path.exists(self.path):
            with open(self.path, "r") as file:
                self.training_list = json.load(file)
        else:
            self.create_training()
            with open(self.path, "r") as file:
                self.training_list = json.load(file)

    def add_training(self, training: TrainingI):
        self.training_list[training["title"]] = training
        self.create_training()

    def remove_training(self, training_title: str):
        del self.training_list[training_title]
        self.create_training()

    def update_training(self, training_title: str, new_data: PartialTrainingI):
        self.training_list[training_title].update(new_data)
        self.create_training()
