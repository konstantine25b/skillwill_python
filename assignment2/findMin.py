def find_min_numeric_value(data):

    numeric_values = [value for value in data.values() if isinstance(value, (int, float))]

    if not numeric_values:
        return None

    min_value = min(numeric_values)
    return min_value