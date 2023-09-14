def get_top():
    file = open('top-200-cryptos.txt')
    data = file.read()
    split = data.split('\n')
    return split
