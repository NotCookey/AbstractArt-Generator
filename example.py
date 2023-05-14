from AbstractArt import AbstractArtGenerator

if __name__ == "__main__":
    generator = AbstractArtGenerator(size=(1920, 1080), num_shapes=1000)
    generator.generate()
    generator.save("abstract_art.png")
