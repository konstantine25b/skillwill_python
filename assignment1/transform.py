def transform_variable(var):
    if isinstance(var, str):
        try:
            # Try to transform string to integer
            transformed_var = int(var)
            print(f"Transformed string '{var}' to integer {transformed_var}.")
        except ValueError:
            # Handle the case where the string is not a valid integer
            print(f"Cannot transform string '{var}' to an integer.")
            transformed_var = var  # keep the original value if transformation fails
    elif isinstance(var, int):
        # Transform integer to string
        transformed_var = str(var)
        print(f"Transformed integer {var} to string '{transformed_var}'.")
    else:
        # If the variable is neither string nor integer, return it as is
        print(f"Variable is neither string nor integer: {var}")
        transformed_var = var
    
    return transformed_var
