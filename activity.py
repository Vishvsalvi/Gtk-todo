from gettext import gettext as _
from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityToolbarButton, StopButton
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

class LanguageLearnerActivity(activity.Activity):
    def __init__(self, handle):
        activity.Activity.__init__(self, handle)

        # Create toolbar
        toolbar_box = ToolbarBox()
        self.set_toolbar_box(toolbar_box)
        
        activity_button = ActivityToolbarButton(self)
        toolbar_box.toolbar.insert(activity_button, 0)
        
        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar_box.toolbar.insert(separator, -1)
        
        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        
        # Main container
        self.main_container = Gtk.Notebook()
        self.set_canvas(self.main_container)
        
        # Add tabs for different activities
        self.flashcards_page = FlashcardsPage()
        self.main_container.append_page(
            self.flashcards_page,
            Gtk.Label(label=_('Flashcards'))
        )
        
        self.sentence_builder_page = SentenceBuilderPage()
        self.main_container.append_page(
            self.sentence_builder_page,
            Gtk.Label(label=_('Sentence Builder'))
        )
        
        self.games_page = GamesPage()
        self.main_container.append_page(
            self.games_page,
            Gtk.Label(label=_('Games'))
        )
        
        self.show_all()

class FlashcardsPage(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL)
        # Flashcard implementation will go here
        label = Gtk.Label(label=_('Flashcards Coming Soon'))
        self.pack_start(label, True, True, 0)

class SentenceBuilderPage(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL)
        # Sentence builder implementation will go here
        label = Gtk.Label(label=_('Sentence Builder Coming Soon'))
        self.pack_start(label, True, True, 0)

class GamesPage(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL)
        # Games implementation will go here
        label = Gtk.Label(label=_('Games Coming Soon'))
        self.pack_start(label, True, True, 0) 