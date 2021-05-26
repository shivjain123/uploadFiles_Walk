import os;
import dropbox;
from dropbox.files import WriteMode;

class TransferData:
    def __init__(self, access_token):
        super().__init__()
        self.access_token = access_token


    def upload_file(self, file_from, file_to):

        dbx = dropbox.Dropbox(self.access_token)

        local_path = input("Enter file path.")

        for root, sub_folders, files in os.walk(file_from):

            relative_path = os.path.relpath(local_path, file_from)
            dropbox_path = os.path.join(file_to, relative_path)

            with open(local_path, 'rb') as f:
                dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))


def main():
    access_token = 'ksAyx1HqRZ4AAAAAAAAAAXenJVA7FF-0W9et3dBwy9FIOM5mwgoJsck9jU212snd'
    transferData = TransferData(access_token)

    file_from = input("Please enter the Soruce Path.")
    file_to = input("Please enter the Destination Path.")

    # API v2
    transferData.upload_file(file_from, file_to)


if __name__ == '__main__':
    main()
