import os
import jq
import json
import glob
from pathlib import Path, PurePath

class jsfsdb:
    def __init__(self, dbpath):
        self.dbpath = Path(dbpath)
        if not self.dbpath.is_dir():
            self.dbpath.mkdir()

    def _resolve_filename(self, collection, id):
        if id is None:
            filename = self.dbpath.joinpath("{}.json".format(collection))
        else:
            pathname = self.dbpath.joinpath(collection)
            if not pathname.is_dir():
                pathname.mkdir()
            filename = self.dbpath.joinpath(collection, "{}.json".format(id))

        return str(filename)

    def read(self, collection, id):
        filename = self._resolve_filename(collection, id)
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            return data
        except:
            return {}

    def create(self, data, collection, id):
        filename = self._resolve_filename(collection, id)
        buf = json.dumps(data, sort_keys=True, indent=2)
        with open(filename, 'w') as f:
            f.write(buf)

    def update(self, data, collection, id):
        # for now, this just re-writes (recreates) the file
        self.create(data, collection, id)

    def count(self, collection):
        collection_path = self.dbpath.joinpath(collection)
        try:
            file_count = len([name for name in os.listdir(str(collection_path)) if os.path.isfile(str(collection_path.joinpath(name)))])
        except FileNotFoundError:
            file_count = 0
        return(file_count)

    def all(self, collection):
        collection_path = self.dbpath.joinpath(collection)
        arr = []
        all_files = glob.glob(str(collection_path.joinpath("*.json")))
        for name in sorted(all_files, key=lambda x: str(os.path.splitext(os.path.basename(x))[0])):
            with open(name, "r") as f:
                d = json.load(f)
                arr.append(d)
        return(arr)

    def query(self, collection, query_str):
        return(jq.compile(query_str).input(self.all(collection)))
