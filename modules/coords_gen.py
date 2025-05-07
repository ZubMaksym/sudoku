def create_line_cords(cell_size: int):
    # creates the x,y cords to draw the grid lines
    list_points = []
    for y_point in range(0, 10):
        hr_lines = []
        hr_lines.append((225, y_point*cell_size + 225))
        hr_lines.append((675, y_point*cell_size + 225))
        list_points.append(hr_lines)

    for x_point in range(0, 10):
        vr_lines = []
        vr_lines.append((x_point*cell_size +  225, 225))
        vr_lines.append((x_point*cell_size + 225, 675))
        list_points.append(vr_lines)
    # print(list_points)
    return list_points