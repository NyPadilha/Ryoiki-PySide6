from typing import TypedDict, List


class ExerciseI(TypedDict):
    name: str
    sets: int
    reps: int
    weight: int


class TrainingI(TypedDict):
    title: str
    rest_time: str
    rounds: int
    exercises: List[ExerciseI]


class PartialTrainingI(TypedDict, total=False):
    title: str
    rest_time: str
    rounds: int
    exercises: List[ExerciseI]


class TitlessTrainingI(TypedDict):
    rest_time: str
    rounds: int
    exercises: List[ExerciseI]
