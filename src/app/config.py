from os import environ

import pydantic


class Config(pydantic.BaseSettings):
    DEBUG_CONFIG: bool = False

    LOG_CONSOLE_LEVEL: str = "INFO"
    LOG_FILE: str = None
    LOG_FILE_LEVEL: str = "INFO"

    class Config:
        env_file = environ.get('DOTENV_FILE', '.env')

    def __init__(self):
        super().__init__()
        self._configure_debug_configs()

    def _configure_debug_configs(self):
        if self.DEBUG_CONFIG:
            for k, v in self.__dict__.items():
                if k.isupper():
                    print(f"{k}: {v!r}")


config = Config()
