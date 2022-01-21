import color_code as color

def get_color_code_manual():
    pairNo = 1
    print('{:<13} {:<13} {:<13} \n'.format('Pair No.', 'Major Color', 'Minor Color'))
    for major_color in color.MAJOR_COLORS:
        for minor_color in color.MINOR_COLORS:
            print('{:<13} {:<13} {:<13} \n'.format(pairNo,major_color, minor_color))
            pairNo += 1
