import selection
import download

def download_image_with_bounding_box(top_left_latitude, top_left_longitude, bottom_right_latitude, bottom_right_longitude, detail, filename):
  quad_keys_matrix = selection.get_quad_keys_matrix(top_left_latitude, top_left_longitude, bottom_right_latitude, bottom_right_longitude, detail)
  crop_rectangle = selection.get_crop_rectangle(top_left_latitude, top_left_longitude, bottom_right_latitude, bottom_right_longitude, detail)

  stitched_image = download.stitch_images(quad_keys_matrix)
  cropped_image = download.crop_image(stitched_image, crop_rectangle)
  cropped_image.save(filename)
