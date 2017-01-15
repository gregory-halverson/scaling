from numpy import nanmin, nanmax

def scale(data, minimum, maximum):
    data_min = nanmin(data)
    data_max = nanmax(data)
    data_range = data_max - data_min
    target_range = maximum - minimum
    scaled = (data - data_min) / data_range * target_range + minimum

    return scaled

