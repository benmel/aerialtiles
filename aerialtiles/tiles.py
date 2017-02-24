import math

dimensions = 256
earth_radius = 6378137.0
min_latitude = -85.05112878
max_latitude = 85.05112878
min_longitude = -180.0
max_longitude = 180.0

"""Clip num if below min or above max"""
def clip(num, min_num, max_num):
  return min(max(num, min_num), max_num)

"""Height and width of map with detail"""
def map_size(detail):
  return dimensions * 2**detail

"""Convert coordinate to pixel"""
def coord_to_pixel(latitude, longitude, detail):
  map_size_detail = map_size(detail)
  latitude = clip(latitude, min_latitude, max_latitude)
  longitude = clip(longitude, min_longitude, max_longitude)

  x = (longitude + 180) / 360.0
  sin_latitude = math.sin(latitude * math.pi / 180)
  y = 0.5 - math.log((1 + sin_latitude) / (1 - sin_latitude)) / (4 * math.pi)

  pixel_x = int(round(clip(x * map_size_detail + 0.5, 0, map_size_detail - 1)))
  pixel_y = int(round(clip(y * map_size_detail + 0.5, 0, map_size_detail - 1)))

  return (pixel_x, pixel_y)

"""Convert pixel to coordinate"""
def pixel_to_coord(pixel_x, pixel_y, detail):
  map_size_detail = map_size(detail)
  x = (clip(pixel_x, 0, map_size_detail - 1) / float(map_size_detail)) - 0.5
  y = 0.5 - (clip(pixel_y, 0, map_size_detail - 1) / float(map_size_detail))

  latitude = 90 - 360 * math.atan(math.exp(-y * 2 * math.pi)) / math.pi
  longitude = 360 * x

  return (latitude, longitude)

"""Convert pixel to tile"""
def pixel_to_tile(pixel_x, pixel_y):
  tile_x = pixel_x / dimensions
  tile_y = pixel_y / dimensions

  return (tile_x, tile_y)

"""Convert tile to pixel"""
def tile_to_pixel(tile_x, tile_y):
  pixel_x = tile_x * dimensions
  pixel_y = tile_y * dimensions

  return (pixel_x, pixel_y)

"""Convert num to binary and return list of length detail"""
def binary_list(num, detail):
  binary_string = str(bin(num)[2:])
  binary_fill = binary_string.zfill(detail)
  return list(binary_fill)

"""Interleave tile values and return quad key"""
def tile_to_quad_key(tile_x, tile_y, detail):
  binary_x = binary_list(tile_x, detail)
  binary_y = binary_list(tile_y, detail)
  quad_key = ''

  for bit_x, bit_y in zip(binary_x, binary_y):
    combined = str(int(bit_y + bit_x, 2))
    quad_key += combined

  return quad_key
