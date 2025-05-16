def create_line_cords(cell_size: int):
    list_points = []

    grid_width = cell_size * 9
    offset_x = (1200 - grid_width) // 2
    offset_y = (900 - grid_width) // 2

    # Горизонтальні лінії
    for y_point in range(10):
        y = y_point * cell_size + offset_y
        list_points.append([(offset_x, y), (offset_x + grid_width, y)])

    # Вертикальні лінії
    for x_point in range(10):
        x = x_point * cell_size + offset_x
        list_points.append([(x, offset_y), (x, offset_y + grid_width)])

    return list_points