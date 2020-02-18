def print_prediction(dictionary):
    result = f"My prediction for a flower with features\n\
    - sepal_length = {dictionary['sepal_length']}\n\
    - sepal_width  = {dictionary['sepal_width']}\n\
    - petal_length = {dictionary['petal_length']}\n\
    - petal_width = {dictionary['petal_width']}\n\
\n\
\tis {dictionary['my_pred']:s}."

    print(result)
