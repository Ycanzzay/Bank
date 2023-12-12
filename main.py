def generate_points(*args):
    return ['.' * num for num in args]

result = generate_points(2, 4, 3)
print(result)