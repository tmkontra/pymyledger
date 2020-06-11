import json

from .base import BaseSerializer
from .v0 import SerializerV0


class Serializer:
    _latest_verison = 0

    _version_map = {
        0: SerializerV0,
    }

    def __init__(self, fp):
        self.fp = fp

    def save(self, data, version=None):
        v = version or self._latest_verison
        ser = self._version_map[v]
        out = ser.serialize_data(data)
        with open(self.fp, "w") as f:
            json.dump(out, f)

    def load(self):
        with open(self.fp, "r") as f:
            data = json.load(f)
            version = data.get("version", self._latest_verison)
            serializer: BaseSerializer = self._version_map.get(version)
            if serializer is None:
                raise ValueError("Unsupported version specified:", version)
            return serializer.deserialize_data(data)
