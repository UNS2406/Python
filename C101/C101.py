# c101 - dropbox cloud storage

import dropbox

"""
    access_token variable is
    declared which has some string.
    Then a new transferData
    object is created using the
    class defined earlier and
    access_token is passed to
    it.
"""
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):

        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)


"""



After that a variable called
file_from is declared which
will have the path of the file
or folder which we want to
upload.
below that file_to variable is
declared which has the full
path to upload the file to,
including name that you
wish the file to be called
once uploaded.

Then upload_file function of
the class is called and
file_from and file_to is
passed to it as arguments
"""


def main():
    access_token = 'sl.AbKQY7cwlr949HZB7JxLOMrnYKuY39PSkiEnMjmzkLJ8mukldzSQjT8oLVfn_A-kB4yn6O0erRD07aV-9JeaGvvRPoLFEVvwg3_p2AufnKjhGlCgTVtpR4YV0SKhk6nbU2-ztZAB'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.
    file_to = input("enter the full path to upload to dropbox:- ")

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()
