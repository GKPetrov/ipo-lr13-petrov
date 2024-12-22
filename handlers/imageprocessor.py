from PIL import ImageFilter, ImageDraw, ImageFont

class ImageProcessor:
    def __init__(self, img):
        self.img = img
    def apply_filter(self):
        if self.img:
            if self.img.mode not in ("RGB", "RGBA"):
                self.img = self.img.convert("RGB")
            self.img = self.img.filter(ImageFilter.CONTOUR)
        else:
            print("Изображение не загружено!")
    def apply_text(self):
        img_size = self.img.size
        draw = ImageDraw.Draw(self.img)  
        font = ImageFont.truetype("arial.ttf", 30)
        text = "Вариант 3"  
        bbox = draw.textbbox((0, 0), text, font = font)  
        text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1] 
        text_x = (img_size[0] - text_width) / 2  
        text_y = (img_size[1] - text_height) / 2  
        draw.text((text_x, text_y), text, font = font)  
        return self.img  
