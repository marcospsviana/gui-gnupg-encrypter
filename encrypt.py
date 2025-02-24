from package import gnupg
import os


def encypt_file(file, file_key, temp_home_gnupg):
    
    try:
        file_path = os.path.split(file)
        current_directory = os.getcwd()
        output_path=f"{os.path.expanduser("~")}/{file_path[-1]}.pgp"
        gpg = gnupg.GPG(gpgbinary="gpg", gnupghome=temp_home_gnupg)
        with open(file_key, "rb") as public:
            gpg.import_keys(public.read())
        recipient = gpg.list_keys()[0]['uids']
        with open(output_path, "w") as file_output:
            gpg.encrypt_file(file, recipients=recipient, armor=True, output=output_path, always_trust=True)
        return output_path
    except Exception as err:
        return err
    
