from src.services import JsonLoader
from PySide6.QtWidgets import QMessageBox
from src.view import Ui_Widget
from src.model import MapNpcId

class NpcController:
    def __init__(self, view):
        self.view = view
        self.connect_events()
    
    def connect_events(self):
        self.view.npclist.activated.connect(self.on_combobox_npclist_activated)
        self.view.pushButton.clicked.connect(self.on_button_pushButton_activated)
    
    def on_combobox_npclist_activated(self, index):
        # get selected text
        selected_text = self.view.npclist.itemText(index)
        # update image
        page_url = "https://nosapki.com/fr/npcs/monsters/" + str(selected_text.split()[0])
        image_url = "https://nosapki.com" + JsonLoader.get_image_url(self, page_url)
        JsonLoader.fetch_and_display_image(self, image_url, self.view)
    
    def on_button_pushButton_activated(self, index):

        Ui_Widget.show_message_box(self, "texte de test", "texte informatif de test", "Test")
        npc_index = self.view.npclist.currentIndex()
        npc_id = self.view.npclist.itemText(npc_index).split()[0]
        npc_name = self.view.npcinput.text()
        map_index = self.view.maplist.currentIndex()
        map_id = self.view.maplist.itemText(map_index).split()[0]
        pos_x = self.view.inputposx.text()
        pos_y = self.view.inputposy.text()
        direction = self.view.inputpos.text()

        mapnpc = MapNpcId(0, 9, 0, 4750, 0, 0, 0, map_id, pos_x, pos_y, npc_name, npc_id, direction, "", 0)