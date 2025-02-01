import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gdk
import subprocess
from data.vocabulary import VOCABULARY

class FlashcardsPage(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, spacing=10)
        
        # Current vocabulary index
        self.current_index = 0
        self.current_language = "en"
        
        # Create UI elements
        self.image = Gtk.Image()
        self.word_label = Gtk.Label()
        self.word_label.set_markup("<span size='xx-large'>Word</span>")
        
        # Navigation buttons
        nav_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        prev_button = Gtk.Button(label="Previous")
        next_button = Gtk.Button(label="Next")
        speak_button = Gtk.Button(label="🔊")
        
        # Language selection
        language_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        self.lang_buttons = {}
        for lang in ["en", "es", "fr"]:
            button = Gtk.ToggleButton(label=lang.upper())
            button.connect("toggled", self.on_language_change, lang)
            self.lang_buttons[lang] = button
            language_box.pack_start(button, True, True, 0)
        
        # Connect signals
        prev_button.connect("clicked", self.on_previous_clicked)
        next_button.connect("clicked", self.on_next_clicked)
        speak_button.connect("clicked", self.on_speak_clicked)
        
        # Pack widgets
        self.pack_start(language_box, False, False, 10)
        self.pack_start(self.image, True, True, 0)
        self.pack_start(self.word_label, False, False, 10)
        nav_box.pack_start(prev_button, True, True, 0)
        nav_box.pack_start(speak_button, False, False, 0)
        nav_box.pack_start(next_button, True, True, 0)
        self.pack_start(nav_box, False, False, 10)
        
        # Initialize first card
        self.lang_buttons["en"].set_active(True)
        self.update_flashcard()
    
    def update_flashcard(self):
        item = VOCABULARY[self.current_index]
        # Load image
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            item.image_path, 300, 300, True)
        self.image.set_from_pixbuf(pixbuf)
        # Update word
        self.word_label.set_markup(
            f"<span size='xx-large'>{item.translation[self.current_language]}</span>")
    
    def on_previous_clicked(self, button):
        self.current_index = (self.current_index - 1) % len(VOCABULARY)
        self.update_flashcard()
    
    def on_next_clicked(self, button):
        self.current_index = (self.current_index + 1) % len(VOCABULARY)
        self.update_flashcard()
    
    def on_language_change(self, button, language):
        if button.get_active():
            self.current_language = language
            for lang, btn in self.lang_buttons.items():
                if lang != language:
                    btn.set_active(False)
            self.update_flashcard()
    
    def on_speak_clicked(self, button):
        item = VOCABULARY[self.current_index]
        word = item.translation[self.current_language]
        subprocess.run(["espeak", "-v", self.current_language, word]) 