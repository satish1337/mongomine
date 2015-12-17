from . import dev

class Settings(dev.Settings):
    ALLOWED_HOSTS = ['*']    