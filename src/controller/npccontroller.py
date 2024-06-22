from src.services import JsonLoader

class NpcController:
    def __init__(self, view):
        self.view = view
        self.connect_events()
    
    def connect_events(self):
        self.view.npclist.activated.connect(self.on_combobox_npclist_activated)
    
    def on_combobox_npclist_activated(self, index):
        # get selected text
        selected_text = self.view.npclist.itemText(index)
        # update image
        page_url = "https://nosapki.com/fr/npcs/monsters/" + str(selected_text.split()[0])
        image_url = "https://nosapki.com" + JsonLoader.get_image_url(self, page_url)
        JsonLoader.fetch_and_display_image(self, image_url, self.view)