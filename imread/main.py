import cv2 as cv                    # inport openCV libraries

def load_img_w_specific_setting(flag):

    def display_info_of_loaded_img (img):
        dimension = img.shape
        height    = dimension[0]
        width     = dimension[1]
        if len(dimension) > 2:
            channel   = dimension[2]
        else:
            channel = -1
        print('load setting is ', flag)
        print('width: %d height: %d channel: %d' % (width, height, channel) )
        print('depth info: ', img.dtype)
        # cv.imshow(str(flag), img)
        cv.imwrite(str(flag)+'.png',img)

    img = cv.imread('raw.png', flag)                # load an image in the same folder w/ the script
                                                    # cv2.imread(filename[, flags]) → retval
    display_info_of_loaded_img(img)
                                                    
load_img_w_specific_setting(cv.IMREAD_UNCHANGED)
load_img_w_specific_setting(cv.IMREAD_GRAYSCALE)
load_img_w_specific_setting(cv.IMREAD_COLOR)
load_img_w_specific_setting(cv.IMREAD_ANYDEPTH)
load_img_w_specific_setting(cv.IMREAD_ANYCOLOR)
load_img_w_specific_setting(cv.IMREAD_ANYCOLOR | cv.IMREAD_ANYDEPTH)

# cv.waitKey(0)                                       # hold the created windows
# cv.destroyAllWindows()                              # proceed to end code and destroy all windows

# Note: In the case of a color images, the decoded images will have the channels stored in B G R order.
#       use Mac terminal to show information (especially depth): sips -g all image.png