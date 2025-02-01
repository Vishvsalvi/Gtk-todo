from typing import Dict, List, NamedTuple

class VocabularyItem(NamedTuple):
    word: str
    translation: Dict[str, str]
    image_path: str

class SentenceItem(NamedTuple):
    sentence: Dict[str, str]
    words: List[str]

VOCABULARY = [
    VocabularyItem(
        word="apple",
        translation={"en": "apple", "es": "manzana", "fr": "pomme"},
        image_path="assets/images/apple.png"
    ),
    # Add more vocabulary items
]

SENTENCES = [
    SentenceItem(
        sentence={
            "en": "I like to eat apples",
            "es": "Me gusta comer manzanas",
            "fr": "J'aime manger des pommes"
        },
        words=["I", "like", "to", "eat", "apples"]
    ),
    # Add more sentences
] 