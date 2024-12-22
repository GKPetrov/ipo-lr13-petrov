from PIL import Image
class ImageHandler:
    def __init__(self, img_path):
        self.img_path = img_path
        self.img = None
    def load_img(self):
        self.img = Image.open(self.img_path)
        return self.img
    def save_img(self, save_path):
        if self.img:
            self.img.save(save_path)
        else:
            print("Изображение не загружено!")
    def size_img(self):
        self.img.thumbnail((200,200))
    def get_img(self):
        if self.img:
            return self.img
        else:
            print("Изображение не загружено!")
            return None