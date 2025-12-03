from typing import TypedDict

def count_words(book: str) -> int:
    word_list = book.split()
    return len(word_list)

def repetition_count(book: str) -> dict[str, int]:
    count: dict[str,int] = {}
    for char in book:
        lower_case_char = char.lower()
        if lower_case_char in count:
            count[lower_case_char] += 1
        else:
            count[lower_case_char] = 1;
    return count

class CharacterCount(TypedDict):
    char: str
    num: int

def get_num_key(count: CharacterCount) -> int:
    return count['num']

def character_sort(character_count: dict[str, int]) -> list[CharacterCount]:
    new_list: list[CharacterCount] = []
    for char in character_count:
        count = character_count[char]
        new_list.append({'char': char, 'num': count})
    new_list.sort(reverse=True, key=get_num_key)
    return new_list

