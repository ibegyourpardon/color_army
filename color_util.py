from colors import color_list


def get_color_id(original_color: str):
    """
    通过计算 rgb 三个位置和预设位置的差，求出绝对值之和，总和越小的，意味着和这个预设颜色越接近。
    最后取最小差值的预设颜色，就可以认为是最接近的预设的颜色了。
    预期参数格式为 255,255,255 形式的字符串
    """
    distance_r = 765 # 255 * 3
    color = {}

    #转换输入的字符串为 tuple
    color_tuple = original_color.split(",")

    for i in color_list:
        rgb_set = i['rgb']
        # print(type(rgb_set[0]))
        r = rgb_set[0] - int(color_tuple[0])
        g = rgb_set[1] - int(color_tuple[1])
        b = rgb_set[2] - int(color_tuple[2])
        distance = abs(r) + abs(g) + abs(b)
        if distance < distance_r:
            distance_r = abs(r) + abs(g) + abs(b)
            color = i
    return color['id']