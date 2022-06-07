def layer_function():
    return "text from function in layer"


# Change to True with INLCUDE_CHANGE = True in handler.py
INCLUDE_CHANGE = False

if INCLUDE_CHANGE:
    def layer_function_two():
        return "other text from layer too"
