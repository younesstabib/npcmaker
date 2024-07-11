import requests
from PySide6.QtGui import QPixmap
import requests
from bs4 import BeautifulSoup

class JsonLoader:
    def __init__(self, view):
        self.view = view
        self.load_json_data_maps()
        self.load_json_data_monsters()
        # Load first NPC img
        image_url = "https://nosapki.com" + self.get_image_url(self, "https://nosapki.com/fr/npcs/monsters/0")
        self.fetch_and_display_image(self, image_url, self.view)

    def load_json_data_monsters(self):
        url = "https://itempicker.atlagaming.eu/monsters.json"

        try:
            response = requests.get(url)
            response.raise_for_status()  # Check if the request was successful
            data = response.json()
            
            str_list = []

            # Extract 'id' and 'name' (uk) and populate the combobox
            results = [{"id": monster["id"], "name_uk": monster["name"]["uk"]} for monster in data]
            for result in results:
                self.view.npclist.addItem(f"{result['id']} - {result['name_uk']}")
                str_list.append(f"{result['id']} - {result['name_uk']}")
            self.view.npclistmodel.setStringList(str_list)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching JSON data: {e}")
    
    def load_json_data_maps(self):
        url = "https://itempicker.atlagaming.eu/maps.json"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            results = []
            for map_key, map_data in data.items():
                if isinstance(map_data, dict):
                    map_id = map_data.get("id", "id manquant")
                    name_dict = map_data.get("name", {})
                    if isinstance(name_dict, dict) and "uk" in name_dict:
                        map_name_uk = name_dict["uk"]
                    else:
                        map_name_uk = "none"
                    results.append({"id": map_id, "name_uk": map_name_uk})
                else:
                    print(f"structure de key : {map_key}")
            sorted_results = sorted(results, key=lambda x: x["id"])
            for result in sorted_results:
                self.view.maplist.addItem(f"{result['id']} - {result['name_uk']}")
            self.view.maplistmodel.setStringList(results)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching JSON data: {e}")
    
    @staticmethod
    def fetch_and_display_image(self, url, view):
        response = requests.get(url)
        if response.status_code == 200:
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            view.npcimg.setPixmap(pixmap)
        else:
            view.npcimg.setText("Image not found")

    @staticmethod
    def get_image_url(self, page_url):
        # download content from the page
        response = requests.get(page_url)
        if response.status_code != 200:
            raise Exception(f"Failed to load page: {page_url}")

        soup = BeautifulSoup(response.content, 'html.parser')

        # find div with class 'monster-original-view' and get url image
        div = soup.find('div', class_='monster-original-view')
        if not div:
            raise Exception("Div with class 'monster-original-view' not found")

        img_tag = div.find('img')
        if not img_tag or 'src' not in img_tag.attrs:
            raise Exception("Image tag not found or does not have 'src' attribute")

        return img_tag['src']
    
    def get_height_and_width(self):
        url = "https://itempicker.atlagaming.eu/maps.json"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            results = []
            for map_key, map_data in data.items():
                if isinstance(map_data, dict):
                    map_id = map_data.get("id", "id manquant")
                    name_dict = map_data.get("name", {})
                    width_map = map_data.get("w", "0")
                    height_map = map_data.get("h", "0")
                    if isinstance(name_dict, dict) and "uk" in name_dict:
                        map_name_uk = name_dict["uk"]
                    else:
                        map_name_uk = "none"
                    results.append({"id": map_id, "name_uk": map_name_uk})
                else:
                    print(f"structure de key : {map_key}")
            sorted_results = sorted(results, key=lambda x: x["id"])
            for result in sorted_results:
                self.view.maplist.addItem(f"{result['w']} - {result['h']} - {result['id']} - {result['name_uk']}")
            self.view.maplistmodel.setStringList(results)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching JSON data: {e}")