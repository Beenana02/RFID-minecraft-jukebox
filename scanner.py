from mfrc522 import SimpleMFRC522
reader=SimpleMFRC522()
def scanDisc(id):
    print("Card Value is:",id) 

id= reader.read()[0]
scanDisc(id)