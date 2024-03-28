import os
import json
from typing import List
from interfaces import TrainingI


class Training:
    def __init__(self):
        self.path = "database/training.json"
        self.training_list: List[TrainingI] = []

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
        self.training_list.append(training)
        self.create_training()

    def remove_training(self, training_title: str):
        self.training_list = [
            training
            for training in self.training_list
            if training["title"] != training_title
        ]
        self.create_training()

    def update_training(self, training_title: str, new_data: TrainingI):
        for training in self.training_list:
            if training["title"] == training_title:
                training.update(new_data)
                break

        self.create_training()
