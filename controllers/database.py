import sqlite3

class Database:
    _connection = None

    @classmethod
    def get_db_connection(cls):
        if cls._connection is None:
            cls._connection = sqlite3.connect('controllers/inference_system/knowledge_base/knowledge_base.db')
        return cls._connection

    @classmethod
    def close_db_connection(cls):
        if cls._connection is not None:
            cls._connection.close()
            cls._connection = None