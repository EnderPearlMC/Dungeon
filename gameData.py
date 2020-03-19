from tools.fileManager import FileManager


# class which get datas in files and make them as variable
class GameData:

    # construct method
    def __init__(self):

        self.file_manager = FileManager()

        self.data_player = {
            "name": "",
            "level": 0,
            "money": 0,
            "dungeon": 1
        }

    # makes basic_data_player as file
    def make_datas_as_file(self):

        self.file_manager.write_file("files/player.yaml", self.data_player)

    # returns value of the player file
    def get_player_file_data(self):

        return self.file_manager.read_file("files/player.yaml")
