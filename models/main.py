from .auth import Auth
from .unlockfile import UnlockFile

class Model:
    def __init__(self):
        self.auth = Auth()
        self.unlocker = UnlockFile()
