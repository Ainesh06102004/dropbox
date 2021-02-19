import dropbox

class Fileupload():
    def __init__(self, accesstoken):
        self.accesstoken = accesstoken

    def movefiles(self, fromfile, tofile):
        dbx = dropbox.Dropbox(self.accesstoken)
        
        with open(fromfile, 'rb') as f:
            dbx.files_upload(f.read(), tofile)

def upload():
    accesstoken = "sl.ArkWi-mSN4RQzNMXPVD_qKBfCHeWC9sam0-1Gy2XrSIrQw5bAoS0Sx6uOC8WQoeQ_hmSuRDFkIyY05iQ2_yxrSWtbu0xn9y_54HFBh8kdAMLdqkyhGWkoMe3ygDrXGdoLzHzSLU7T00"
    
    transferdata = Fileupload(accesstoken)

    fromfile = 'test.txt'

    fileto = '/fileto/Document.txt'

    transferdata.movefiles(fromfile, fileto)

upload()