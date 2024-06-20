# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPixmap
import requests

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Load JSON data and populate combobox
        self.load_json_data_monsters()
        self.load_json_data_maps()
        self.connect_events()

        # Load first NPC img
        image_url = f"https://itempicker.atlagaming.eu/api/monsters/icon/0"
        self.fetch_and_display_image(image_url)
    
    def load_json_data_monsters(self):
        url = "https://itempicker.atlagaming.eu/monsters.json"

        try:
            response = requests.get(url)
            response.raise_for_status()  # Check if the request was successful
            data = response.json()
            
            # Extract 'id' and 'name' (in English) and populate the combobox
            results = [{"id": monster["id"], "name_uk": monster["name"]["uk"]} for monster in data]
            for result in results:
                self.ui.npclist.addItem(f"{result['id']} - {result['name_uk']}")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching JSON data: {e}")
    
    def load_json_data_maps(self):
        url = "https://itempicker.atlagaming.eu/maps.json"

        try:
            response = requests.get(url)
            response.raise_for_status() # si la requete est bonne
            data = response.json()
            results = []
            for map_key, map_data in data.items():
                if isinstance(map_data, dict):
                    map_id = map_data.get("id", "id manquant")
                    name_dict = map_data.get("name", {})
                    if isinstance(name_dict, dict) and "uk" in name_dict:
                        map_name_uk = name_dict["uk"]
                    else:
                        map_name_uk = "Nom UK manquant"
                    results.append({"id": map_id, "name_uk": map_name_uk})
                else:
                    print(f"structure de key : {map_key}")
            sorted_results = sorted(results, key=lambda x: x["id"])
            for result in sorted_results:
                # print(f"{result['id']} - {result['name_uk']}")
                self.ui.maplist.addItem(f"{result['id']} - {result['name_uk']}")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching JSON data: {e}")
    
    def fetch_and_display_image(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            self.ui.npcimg.setPixmap(pixmap)
        else:
            self.ui.npcimg.setText("Image not found")

    def connect_events(self):
        self.ui.npclist.activated.connect(self.on_combobox_npclist_activated)
    
    def on_combobox_npclist_activated(self, index):
        # Obtenir le texte sélectionné
        selected_text = self.ui.npclist.itemText(index)
        image_url = f"https://itempicker.atlagaming.eu/api/monsters/icon/" + str(selected_text.split()[0])
        self.fetch_and_display_image(image_url)
        # Mettre à jour le texte du label
        # self.ui.label.setText(f"Selected: {selected_text}")
        # Mettre à jour l'image du texte selectionné


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
