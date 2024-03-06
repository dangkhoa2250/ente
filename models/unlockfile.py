import io
import msoffcrypto

class UnlockFile:
    def unlock_file(self, ROOTPATH, password):
        decrypted_file = io.BytesIO()
        try:
            with open(ROOTPATH, 'rb') as _iP:
                _encrypted_file = msoffcrypto.OfficeFile(_iP)
                _encrypted_file.load_key(password=password, verify_password=True)
                _encrypted_file.decrypt(decrypted_file)
                self.data = decrypted_file
            return True, decrypted_file
        except:
            return False, decrypted_file