import json
import random
from dataclasses import dataclass
from typing import List, Set, Dict, Tuple
from settings import *

@dataclass
class Character:
    name: str
    family: str
    gender: str
    status: Set[str]
    first_game: str
    release_year: int
    playable: bool

def load_data(file_path: str) -> Tuple[Dict[str, Character], List[str]]:
    character_map: Dict[str, Character] = {}

    with open(file_path, "r", encoding = "utf-8") as f:
        raw_data = json.load(f)

    for item in raw_data:
        char = Character(
            name = item["name"],
            family = item["family"],
            gender = item["gender"],
            status = set(item["status"]),
            first_game = item["first_game"],
            release_year = item["release_year"],
            playable = item["playable"]
        )

        character_map[char.name] = char
    
    all_names = list(character_map.keys())

    return (character_map, all_names)

def select_secret_character(data: Dict[str, Character]) -> Character:
    char = list(data.values())
    ans = random.choice(char)
    return ans

def check(guess: Character, ans: Character) -> List:
    color = [RED] * 5

    if guess.name == ans.name:
        color[0] = GREEN
    elif guess.family == ans.family:
        color[0] = YELLOW

    if guess.gender == ans.gender:
        color[1] = GREEN

    if guess.status == ans.status:
        color[2] = GREEN
    elif not guess.status.isdisjoint(ans.status):
        color[2] = YELLOW

    if guess.first_game == ans.first_game:
        color[3] = GREEN
    elif guess.release_year == ans.release_year:
        color[3] = YELLOW

    if guess.playable == ans.playable:
        color[4] = GREEN

    return color