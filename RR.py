from PIL import Image
def read(path):
    return Image.open(path)    
def resize(pic,hight=None,width=None):
    picH = pic.size[0]
    picW = pic.size[1]
    if hight == None and width == None:
        print("no parament")
        exit()
    if hight != None:
        width = int(hight*picW/picH)
    if width != None:
        hight = int(width*picH/picW)
    return pic.resize((hight,width))    
def save(pic,path):
    pic.save(path)
def rr(path,pathS,hight=None,width=None):
    save(resize(read(path),hight=hight,width=width),pathS)
def returnP(path,hight=None,width=None):
    return resize(read(path),hight=hight,width=width)