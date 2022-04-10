post_x = float(input("请输入X坐标点"))
post_y = float(input("请输入Y坐标点"))
rect_width = float(input("请输入矩形宽度"))
rect_height = float(input("请输入矩形高度"))
degree = input("请输入旋转角度")
if not degree:
    pass
else:
    rotate_x = input("请输入旋转点X坐标点")
    rotate_y = input("请输入旋转点Y坐标点")
scape = float(input("请输入间距"))

with open("./location.txt","r",encoding="utf-8") as f:
    location_table=f.read().splitlines()
    for i in location_table:
        i = i.replace("x=\"\"","x=\""+str(post_x)+"\"")
        i = i.replace("y=\"\"","y=\""+str(post_y)+"\"")
        i = i.replace("width=\"\"","y=\""+str(rect_width)+"\"")
        i = i.replace("height=\"\"","y=\""+str(rect_height)+"\"")
        post_y = post_y + scape
        print(i)