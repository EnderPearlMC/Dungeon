import yaml


# class which Manage every file : Create / Read
class FileManager:

    # writes file with a given path and some datas given
    # @param path : Path of the file
    # @param data : data to write into the file
    def write_file(self, path, data):
        with open(path, 'w') as outfile:
            yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)

    # reads file with a path given and returns an array with infos
    # @param path : Path of the file
    def read_file(self, path):
        with open(path, 'r') as stream:
            data_loaded = yaml.safe_load(stream)
            return data_loaded
