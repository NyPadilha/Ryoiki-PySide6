from typing import TypedDict, List, Literal, Union


class ExerciseI(TypedDict, total=False):
    name: str
    type: Literal["endurance", "reps"]
    config: Union[int, str]
    video: str
    image: str


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
