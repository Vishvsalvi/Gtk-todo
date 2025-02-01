import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf
from data.vocabulary import VOCABULARY
import random

class MemoryGame(Gtk.Grid):
    def __init__(self):
        Gtk.Grid.__init__(self)
        self.set_row_spacing(5)
        self.set_column_spacing(5)
        
        self.cards = []
        self.first_choice = None
        self.can_click = True
        
        # Create pairs of words and images
        items = random.sample(VOCABULARY, 6)  # 6 pairs = 12 cards
        self.setup_game(items)
    
    def setup_game(self, items):
        # Create pairs of cards (word + image)
        pairs = []
        for item in items:
            pairs.extend([
                ("word", item.translation["en"]),
                ("image", item.image_path)
            ])
        
        random.shuffle(pairs)
        
        # Create grid of cards
        for i, (card_type, content) in enumerate(pairs):
            button = Gtk.Button()
            button.card_type = card_type
            button.content = content
            button.revealed = False
            button.connect("clicked", self.on_card_clicked)
            
            # Add to grid
            row = i // 4
            col = i % 4
            self.attach(button, col, row, 1, 1)
            self.cards.append(button) 