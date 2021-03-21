import os

class Config:

    # Hard-coded centrally here.
    APP_NAME = 'api'

    KEY_HOST = 'POSTGRES_HOST'
    KEY_USER = 'POSTGRES_USER'
    KEY_PASSWORD = 'POSTGRES_PASSWORD'
    KEY_DATABASE = 'POSTGRES_DB'

    """Read application configuration from SSM Parameter Key Store"""
    def __init__(self):
        pass

    def get_value(self, key: str) -> str:
        return os.getenv(key)

    def get_connection_string(self, host=None) -> str:
        """Returns a postgresql connection string for the environment.  Allow overriding host to be able to test
        from virtualenv, which requires localhost to connect to docker-compose postgres"""
        if not host:
            host = self.get_value(Config.KEY_HOST)
        user = self.get_value(Config.KEY_USER)
        password = self.get_value(Config.KEY_PASSWORD)
        database = self.get_value(Config.KEY_DATABASE)

        cs = f"postgresql+psycopg2://{user}:{password}@{host}/{database}"
        print(f"CONNECTION STRING: {cs}")
        return cs
