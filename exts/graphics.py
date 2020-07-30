import random
from PIL import Image, ImageDraw, ImageFont


class GraphicsCode(object):
    """
    图形码
    """
    def rnd_color(self):
        return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

    def gene_text(self):
        words = "123456789abcdefghijkmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ"
        # return "".join(random.sample(string.ascii_letters + string.digits, 4))
        return "".join(random.sample(words, 4))

    def draw_lines(slef,draw, num, width, height):
        for num in range(num):
            x1 = random.randint(0, width / 2)
            y1 = random.randint(0, height / 2)
            x2 = random.randint(0, width / 2)
            y2 = random.randint(height / 2, height)
            draw.line(((x1, y1), (x2, y2)), fill="black", width=1)

    def get_random_Color(self):
        c1 = random.randint(50, 150)
        c2 = random.randint(50, 150)
        c3 = random.randint(50, 150)
        return (c1, c2, c3)

    def draw_point(self, draw, num, width, height):
        for num in range(num):
            x = random.randint(0, width)
            y = random.randint(0, height)

            draw.point((x, y), self.get_random_Color())

    def get_verify_code(self):
        code = self.gene_text()
        width, height = 116, 50
        im = Image.new("RGB", (width, height), "white")
        font = ImageFont.truetype('/System/Library/Fonts/Songti.ttc', 40)
        draw = ImageDraw.Draw(im)
        self.draw_lines(draw, num=8, width=116, height=38)
        self.draw_point(draw, num=300, width=116, height=38)
        for item in range(4):
            draw.text((5 + random.randint(-3, 3) + 23 * item, 5 + random.randint(-3, 3)),
                      text=code[item], fill=self.rnd_color(), font=font)
        return im, code