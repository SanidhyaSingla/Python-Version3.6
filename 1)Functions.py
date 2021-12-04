def hello():
    print('Hello ' * 10)

def pyramid(layers):
    icon = '*'
    for i in range(layers):
        print(icon.center(layers))

hello()