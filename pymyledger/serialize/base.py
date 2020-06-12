class BaseSerializer:
    @classmethod
    def serialize_data(cls, data):
        raise NotImplementedError

    @classmethod
    def deserialize_data(cls, json):
        raise NotImplementedError
