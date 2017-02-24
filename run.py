import sys
import getopt
from aerialtiles import main

def run():
  def usage():
    print "python run.py <top_left_latitude> <top_left_longitude> "\
          "<bottom_right_latitude> <bottom_right_longitude> <output_filepath>"

  try:
    opts, args = getopt.getopt(sys.argv[1:], "h")
  except getopt.GetoptError:
    usage()
    sys.exit(2)
  
  for opt, arg in opts:
    if opt in ("-h", "--help"):
      usage()
      sys.exit()
  
  if len(args) < 5:
    usage()
    sys.exit()

  top_left_latitude = float(args[0])
  top_left_longitude = float(args[1])
  bottom_right_latitude = float(args[2])
  bottom_right_longitude = float(args[3])
  output_filepath = args[4]

  if bottom_right_latitude > top_left_latitude:
    print "bottom_right_latitude must be less than or equal to top_left_latitude"
    sys.exit()

  if bottom_right_longitude < top_left_longitude:
    print "bottom_right_longitude must be greater than or equal to top_left_longitude"
    sys.exit()

  main.download_image_with_bounding_box(top_left_latitude, top_left_longitude, bottom_right_latitude, bottom_right_longitude, output_filepath)

if __name__ == "__main__":
  run()
