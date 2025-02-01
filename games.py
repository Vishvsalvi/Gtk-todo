import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, GLib
from data.vocabulary import VOCABULARY
import random

class MemoryGame(Gtk.Grid):
    def __init__(self):
        Gtk.Grid.__init__(self)
        self.set_row_spacing(5)
        self.set_column_spacing(5)
        
        # Center the grid in the window
        self.set_halign(Gtk.Align.CENTER)
        self.set_valign(Gtk.Align.CENTER)
        
        self.cards = []
        self.first_choice = None
        self.can_click = True
        self.matches_found = 0
        
        # Score label
        self.score_label = Gtk.Label()
        self.score_label.set_markup("<span size='large'>Matches Found: 0</span>")
        self.attach(self.score_label, 0, 0, 4, 1)
        
        # New Game button
        self.new_game_button = Gtk.Button(label="New Game")
        self.new_game_button.connect("clicked", self.start_new_game)
        self.attach(self.new_game_button, 0, 1, 4, 1)
        
        # Start the game
        num_pairs = min(6, len(VOCABULARY))
        items = random.sample(VOCABULARY, num_pairs)
        self.setup_game(items)
    
    def setup_game(self, items):
        # Clear existing cards if any
        for card in self.cards:
            self.remove(card)
        self.cards.clear()
        
        # Reset game state
        self.first_choice = None
        self.can_click = True
        self.matches_found = 0
        self.score_label.set_markup("<span size='large'>Matches Found: 0</span>")
        
        # Create pairs of cards (word + image)
        pairs = []
        for item in items:
            pairs.extend([
                ("word", item.translation["en"], item),
                ("image", item.image_path, item)
            ])
        
        random.shuffle(pairs)
        
        # Create grid of cards
        for i, (card_type, content, item) in enumerate(pairs):
            button = Gtk.Button(label="?")
            button.set_size_request(100, 100)
            
            # Store card information
            button.card_type = card_type
            button.content = content
            button.item = item
            button.revealed = False
            button.connect("clicked", self.on_card_clicked)
            
            # Add to grid (offset by 2 rows for score and new game button)
            row = (i // 4) + 2
            col = i % 4
            self.attach(button, col, row, 1, 1)
            self.cards.append(button)
        
        self.show_all()
    
    def on_card_clicked(self, button):
        if not self.can_click or button.revealed:
            return
        
        # Reveal card
        self.reveal_card(button)
        
        # First card of the pair
        if self.first_choice is None:
            self.first_choice = button
            return
        
        # Second card of the pair
        self.can_click = False
        
        # Check if cards match
        if (self.first_choice.item == button.item and 
            self.first_choice != button):
            # Match found
            self.matches_found += 1
            self.score_label.set_markup(
                f"<span size='large'>Matches Found: {self.matches_found}</span>")
            self.first_choice = None
            self.can_click = True
            
            # Check if game is complete
            if self.matches_found == len(VOCABULARY):
                dialog = Gtk.MessageDialog(
                    transient_for=self.get_toplevel(),
                    message_type=Gtk.MessageType.INFO,
                    buttons=Gtk.ButtonsType.OK,
                    text="Congratulations!"
                )
                dialog.format_secondary_text("You've found all the matches!")
                dialog.run()
                dialog.destroy()
        else:
            # No match
            first_choice = self.first_choice
            GLib.timeout_add(1000, self.hide_cards, first_choice, button)
    
    def reveal_card(self, button):
        if button.card_type == "word":
            button.set_label(button.content)
        else:
            # For image cards, you might want to show a small image
            # For now, we'll just show "Image"
            button.set_label("Image")
        button.revealed = True
    
    def hide_cards(self, card1, card2):
        card1.set_label("?")
        card2.set_label("?")
        card1.revealed = False
        card2.revealed = False
        self.first_choice = None
        self.can_click = True
        return False
    
    def start_new_game(self, button):
        num_pairs = min(6, len(VOCABULARY))
        items = random.sample(VOCABULARY, num_pairs)
        self.setup_game(items) 