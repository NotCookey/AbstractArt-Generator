<h2><p align="center">Abstract Art Generator</p></h2>

![abstract_art (6)](https://github.com/NotCookey/AbstractArt-Generator/assets/88582190/d4e3f4e9-eb4b-4bd5-87f3-1970b9cc641c)

This project can generate abstract art images consisting of geometric shapes on a gradient background.

```python
from AbstractArt import AbstractArtGenerator
```

# Initialize the class 
```python
generator = AbstractArtGenerator(size=(1920, 1080), num_shapes=500)
```

# Generate the image
```python
generator.generate()
```

# Save the image 
```python
generator.save("image.png")
```
Parameters:

size - Size of the generated image in (width, height)  
num_shapes - Number of geometric shapes to draw

Shapes:
```
- Circles   
- Triangles
- Squares   
- Leafs     
- Stars
- Droplets
```

Concurrency:
```
The shape drawing is done concurrently using a ThreadPoolExecutor to  
speed up the generation process.
```

Requirements:
```
- PIL
- concurrent.futures
```

Usage example:
```python
generator = AbstractArtGenerator(size=(1920, 1080))
generator.generate()
generator.save("abstract.png")
```

<hr>

Hope this helps!
