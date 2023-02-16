import random
import colorgram as cg

class RandomColor:
    def rand_color():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        color_tuple = (r, g, b)
        return color_tuple


    def color_pallete():
        color_list = []
        color = cg.extract('img.jpg',6)
        
        for i in range(6):
            r = (color[i].rgb).r
            g = (color[i].rgb).g
            b = (color[i].rgb).b

            color_list.append((r, g, b))

        return color_list





