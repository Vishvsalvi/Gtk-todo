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
    VocabularyItem(
        word="cat",
        translation={"en": "cat", "es": "gato", "fr": "chat"},
        image_path="assets/images/cat.png"
    ),
    VocabularyItem(
        word="dog",
        translation={"en": "dog", "es": "perro", "fr": "chien"},
        image_path="assets/images/dog.png"
    ),
    VocabularyItem(
        word="house",
        translation={"en": "house", "es": "casa", "fr": "maison"},
        image_path="assets/images/house.png"
    ),
    VocabularyItem(
        word="book",
        translation={"en": "book", "es": "libro", "fr": "livre"},
        image_path="assets/images/book.png"
    ),
    VocabularyItem(
        word="tree",
        translation={"en": "tree", "es": "árbol", "fr": "arbre"},
        image_path="assets/images/tree.png"
    ),
    VocabularyItem(
        word="sun",
        translation={"en": "sun", "es": "sol", "fr": "soleil"},
        image_path="assets/images/sun.png"
    ),
    VocabularyItem(
        word="moon",
        translation={"en": "moon", "es": "luna", "fr": "lune"},
        image_path="assets/images/moon.png"
    )
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
    SentenceItem(
        sentence={
            "en": "The cat and dog play",
            "es": "El gato y el perro juegan",
            "fr": "Le chat et le chien jouent"
        },
        words=["The", "cat", "and", "dog", "play"]
    ),
    SentenceItem(
        sentence={
            "en": "I read a book at home",
            "es": "Leo un libro en casa",
            "fr": "Je lis un livre à la maison"
        },
        words=["I", "read", "a", "book", "at", "home"]
    )
] 