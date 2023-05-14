from PIL import Image, ImageDraw
import random
import math
import concurrent.futures


class AbstractArtGenerator:
    def __init__(self, size=(1920, 1080), num_shapes=500):
        self.size = size
        self.num_shapes = num_shapes
        self.image = None
        self.draw = None

    def generate(self):
        self.image = Image.new("RGB", self.size)
        self.draw = ImageDraw.Draw(self.image)

        gradient = [
            (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            for _ in range(2)
        ]
        for y in range(self.size[1]):
            color = tuple(
                int(
                    gradient_channel[0]
                    + (gradient_channel[1] - gradient_channel[0]) * y / self.size[1]
                )
                for gradient_channel in zip(gradient[0], gradient[1])
            )
            self.draw.line((0, y, self.size[0], y), fill=color)

        def draw_shape(shape_type, shape_size, shape_position, fill_color):
            if shape_type == "circle":
                self.draw.ellipse(
                    (
                        shape_position,
                        (shape_position[0] + shape_size, shape_position[1] + shape_size),
                    ),
                    fill=fill_color,
                )
            elif shape_type == "triangle":
                vertices = [
                    (shape_position[0] + shape_size / 2, shape_position[1]),
                    (shape_position[0], shape_position[1] + shape_size),
                    (shape_position[0] + shape_size, shape_position[1] + shape_size),
                ]
                self.draw.polygon(vertices, fill=fill_color)
            elif shape_type == "square":
                self.draw.rectangle(
                    (
                        shape_position,
                        (shape_position[0] + shape_size, shape_position[1] + shape_size),
                    ),
                    fill=fill_color,
                )
            elif shape_type == "leaf":
                leaf_points = []
                for angle in range(0, 360, 10):
                    x = shape_size * (math.sin(angle) ** 3)
                    y = shape_size * (math.cos(angle) - math.cos(2 * angle) / 2)
                    leaf_points.append(
                        (
                            shape_position[0] + shape_size / 2 + x,
                            shape_position[1] + shape_size / 2 + y,
                        )
                    )
                self.draw.polygon(leaf_points, fill=fill_color)
            elif shape_type == "star":
                star_points = []
                for angle in range(0, 360, 72):
                    x = shape_size * math.sin(math.radians(angle))
                    y = shape_size * math.cos(math.radians(angle))
                    star_points.append(
                        (
                            shape_position[0] + shape_size / 2 + x,
                            shape_position[1] + shape_size / 2 + y,
                        )
                    )
                    x = shape_size / 2 * math.sin(math.radians(angle + 36))
                    y = shape_size / 2 * math.cos(math.radians(angle + 36))
                    star_points.append(
                        (
                            shape_position[0] + shape_size / 2 + x,
                            shape_position[1] + shape_size / 2 + y,
                        )
                    )
                self.draw.polygon(star_points, fill=fill_color)
            elif shape_type == "droplet":
                droplet_points = []
                for angle in range(-60, 120, 10):
                    x = shape_size * (math.sin(math.radians(angle)) ** 3)
                    y = shape_size * (
                        math.cos(math.radians(angle)) - math.cos(math.radians(angle * 2)) / 2
                    )
                    droplet_points.append(
                        (
                            shape_position[0] + shape_size / 2 + x,
                            shape_position[1] + shape_size / 2 + y,
                        )
                    )
                self.draw.polygon(droplet_points, fill=fill_color)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for i in range(self.num_shapes):
                shape_type = random.choice(
                    ["circle", "triangle", "square", "leaf", "star", "droplet"]
                )
                shape_size = random.randint(50, 200)
                shape_position = (
                    random.randint(0, self.size[0] - shape_size),
                    random.randint(0, self.size[1] - shape_size),
                )
                shape_color = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                )
                alpha = random.randint(64, 192)
                fill_color = shape_color + (alpha,)

                futures.append(
                    executor.submit(draw_shape, shape_type, shape_size, shape_position, fill_color)
                )
            for future in concurrent.futures.as_completed(futures):
                future.result()

    def save(self, filename):
        if self.image is not None:
            self.image.save(filename)
