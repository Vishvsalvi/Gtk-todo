import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from data.vocabulary import SENTENCES
import random

class SentenceBuilderPage(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, spacing=10)
        
        self.current_sentence = 0
        self.current_language = "en"
        
        # Create word container
        self.word_container = Gtk.FlowBox()
        self.word_container.set_selection_mode(Gtk.SelectionMode.NONE)
        self.word_container.set_max_children_per_line(5)
        
        # Create target sentence area
        self.target_label = Gtk.Label()
        self.target_label.set_markup("<span size='large'>Build the sentence:</span>")
        
        # Create answer box
        self.answer_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        
        # Pack widgets
        self.pack_start(self.target_label, False, False, 10)
        self.pack_start(self.answer_box, False, False, 10)
        self.pack_start(Gtk.Separator(), False, False, 10)
        self.pack_start(self.word_container, True, True, 10)
        
        # Set up drag and drop
        self.setup_drag_and_drop()
        
        # Load first sentence
        self.load_sentence()
    
    def setup_drag_and_drop(self):
        self.word_container.drag_source_set(
            Gdk.ModifierType.BUTTON1_MASK, [], Gdk.DragAction.MOVE)
        self.answer_box.drag_dest_set(
            Gtk.DestDefaults.ALL, [], Gdk.DragAction.MOVE)
    
    def load_sentence(self):
        sentence = SENTENCES[self.current_sentence]
        words = sentence.words.copy()
        random.shuffle(words)
        
        # Clear existing words
        for child in self.word_container.get_children():
            self.word_container.remove(child)
        
        # Add shuffled words
        for word in words:
            label = Gtk.Label(label=word)
            self.word_container.add(label)
        
        self.target_label.set_markup(
            f"<span size='large'>{sentence.sentence[self.current_language]}</span>") 