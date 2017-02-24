import selection
import download

def download_image_with_bounding_box(top_left_latitude, top_left_longitude, bottom_right_latitude, bottom_right_longitude, output_filepath):
  detail = selection.get_detail(top_left_latitude, top_left_longitude, bottom_right_latitude, bottom_right_longitude)
  print 'Using level of detail: ' + str(detail)

  quad_keys_matrix = selection.get_quad_keys_matrix(top_left_latitude, top_left_longitude, bottom_right_latitude, bottom_right_longitude, detail)
  crop_rectangle = selection.get_crop_rectangle(top_left_latitude, top_left_longitude, bottom_right_latitude, bottom_right_longitude, detail)

  print 'Downloading image'
  stitched_image = download.stitch_images(quad_keys_matrix)
  cropped_image = download.crop_image(stitched_image, crop_rectangle)

  print 'Saving image'
  cropped_image.save(output_filepath)
