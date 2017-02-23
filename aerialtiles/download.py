import urllib
import cStringIO
from PIL import Image

dimensions = 256
tile_url = 'http://h0.ortho.tiles.virtualearth.net/tiles/h{0}.jpeg?g=131'

def stitch_images(quad_keys_matrix):
  width = len(quad_keys_matrix) * dimensions
  length = len(quad_keys_matrix[0]) * dimensions
  image = Image.new('RGB', (width, length))

  for x, col in enumerate(quad_keys_matrix):
    for y, quad_key in enumerate(col):
      url = get_url(quad_key)
      quad_key_image = download_image(url)
      image.paste(quad_key_image, (x * dimensions, y * dimensions))
  return image

def is_image_available(quad_key):
  url = get_url(quad_key)
  quad_key_image = urllib.urlopen(url)
  image_type = quad_key_image.info().type
  return image_type == 'image/jpeg'

def get_url(quad_key):
  return tile_url.format(quad_key)

def download_image(url):
  file = cStringIO.StringIO(urllib.urlopen(url).read())
  image = Image.open(file)
  return image

def crop_image(image, crop_rectangle):
  return image.crop(crop_rectangle)
