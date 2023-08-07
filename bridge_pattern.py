class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        pass



class Circle(Shape):
    def __init__(self, color, x, y, radius):
        super().__init__(color)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        print(f"Drawing Circle at ({self.x}, {self.y}), radius {self.radius}, color {self.color}")


class Square(Shape):
    def __init__(self, color, x, y, side_length):
        super().__init__(color)
        self.x = x
        self.y = y
        self.side_length = side_length

    def draw(self):
        print(f"Drawing Square at ({self.x}, {self.y}), side length {self.side_length}, color {self.color}")



class Renderer:
    def render_circle(self, x, y, radius, color):
        pass

    def render_square(self, x, y, side_length, color):
        pass



class VectorRenderer(Renderer):
    def render_circle(self, x, y, radius, color):
        print(f"Drawing a vector circle at ({x}, {y}), radius {radius}, color {color}")

    def render_square(self, x, y, side_length, color):
        print(f"Drawing a vector square at ({x}, {y}), side length {side_length}, color {color}")


class RasterRenderer(Renderer):
    def render_circle(self, x, y, radius, color):
        print(f"Drawing a raster circle at ({x}, {y}), radius {radius}, color {color}")

    def render_square(self, x, y, side_length, color):
        print(f"Drawing a raster square at ({x}, {y}), side length {side_length}, color {color}")


if __name__ == "__main__":
    circle = Circle("red", 10, 10, 5)
    square = Square("blue", 20, 20, 10)

    vector_renderer = VectorRenderer()
    raster_renderer = RasterRenderer()

    circle.draw()
    square.draw()

    circle.color = "green"
    square.color = "yellow"

    circle.draw()
    square.draw()

    circle.renderer = vector_renderer
    square.renderer = raster_renderer

    circle.draw()
    square.draw()
