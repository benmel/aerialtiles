import tiles

def get_quad_keys_matrix(top_left_latitude, top_left_longitude, bottom_right_latitude, bottom_right_longitude, detail):
  (top_left_pixel_x, top_left_pixel_y) = get_tile(top_left_latitude, top_left_longitude, detail)
  (bottom_right_pixel_x, bottom_right_pixel_y) = get_tile(bottom_right_latitude, bottom_right_longitude, detail)

  quad_keys_matrix = []
  for x in range(top_left_pixel_x, bottom_right_pixel_x + 1):
    quad_keys_x = []
    for y in range(top_left_pixel_y, bottom_right_pixel_y + 1):
      quad_keys_x.append(tiles.tile_to_quad_key(x, y, detail))
    if quad_keys_x:
      quad_keys_matrix.append(quad_keys_x)

  return quad_keys_matrix

def get_tile(latitude, longitude, detail):
  (pixel_x, pixel_y) = tiles.coord_to_pixel(latitude, longitude, detail)
  return tiles.pixel_to_tile(pixel_x, pixel_y)
