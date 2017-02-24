import tiles
import download

dimensions = 256
highest_detail = 20

"""Find highest level of detail for bounding box by testing available images"""
def get_detail(top_left_latitude, top_left_longitude, bottom_right_latitude, bottom_right_longitude):
  detail = highest_detail

  while detail > 1:
    top_left_quad_key = get_quad_key(top_left_latitude, top_left_longitude, detail)
    bottom_right_quad_key = get_quad_key(bottom_right_latitude, bottom_right_longitude, detail)
    # If the top left and bottom right image exist, then the highest level of detail has been found
    if download.is_image_available(top_left_quad_key) and download.is_image_available(bottom_right_quad_key):
      break
    # Try a lower level of detail
    detail -= 1

  return detail

"""Return a matrix containing all the quad keys needed for the images in the bounding box"""
def get_quad_keys_matrix(top_left_latitude, top_left_longitude, bottom_right_latitude, bottom_right_longitude, detail):
  (top_left_tile_x, top_left_tile_y) = get_tile(top_left_latitude, top_left_longitude, detail)
  (bottom_right_tile_x, bottom_right_tile_y) = get_tile(bottom_right_latitude, bottom_right_longitude, detail)

  quad_keys_matrix = []
  # Iterate over all tiles in the bounding box
  for x in range(top_left_tile_x, bottom_right_tile_x + 1):
    quad_keys_x = []
    for y in range(top_left_tile_y, bottom_right_tile_y + 1):
      quad_keys_x.append(tiles.tile_to_quad_key(x, y, detail))
    if quad_keys_x:
      # Check that the list is not empty
      quad_keys_matrix.append(quad_keys_x)

  return quad_keys_matrix

"""Return tile for coordinate"""
def get_tile(latitude, longitude, detail):
  (pixel_x, pixel_y) = tiles.coord_to_pixel(latitude, longitude, detail)
  return tiles.pixel_to_tile(pixel_x, pixel_y)

"""Return quad key for coordinate"""
def get_quad_key(latitude, longitude, detail):
  (tile_x, tile_y) = get_tile(latitude, longitude, detail)
  return tiles.tile_to_quad_key(tile_x, tile_y, detail)

"""Find the crop rectangle that includes only the bounding box in a larger image"""
def get_crop_rectangle(top_left_latitude, top_left_longitude, bottom_right_latitude, bottom_right_longitude, detail):
  (top_left_pixel_x, top_left_pixel_y) = tiles.coord_to_pixel(top_left_latitude, top_left_longitude, detail)
  (bottom_right_pixel_x, bottom_right_pixel_y) = tiles.coord_to_pixel(bottom_right_latitude, bottom_right_longitude, detail)
  (top_left_tile_x, top_left_tile_y) = tiles.pixel_to_tile(top_left_pixel_x, top_left_pixel_y)

  # Get x and y values by subtracting offset from pixel values
  top_left_rectangle_x = top_left_pixel_x - dimensions * top_left_tile_x
  top_left_rectangle_y = top_left_pixel_y - dimensions * top_left_tile_y
  bottom_right_rectangle_x = bottom_right_pixel_x - dimensions * top_left_tile_x
  bottom_right_rectangle_y = bottom_right_pixel_y - dimensions * top_left_tile_y

  # Make sure there is at least one pixel difference in x and y, check edges
  if top_left_rectangle_x == bottom_right_rectangle_x:
    if top_left_rectangle_x == (tiles.map_size(detail) - 1):
      top_left_rectangle_x -= 1
    else:
      bottom_right_rectangle_x += 1

  if top_left_rectangle_y == bottom_right_rectangle_y:
    if top_left_rectangle_y == (tiles.map_size(detail) - 1):
      top_left_rectangle_y -= 1
    else:
      bottom_right_rectangle_y += 1

  return (top_left_rectangle_x, top_left_rectangle_y, bottom_right_rectangle_x, bottom_right_rectangle_y)
