def take_file(file):

    photos= []

    with open(file) as f_in:
        file = f_in.readline()

        for index in range(int(file)):
            each = f_in.readline()[:-1].split(' ')
            unique = set()

            for index1 in range(int(each[1])):
                unique.add(each[index1 + 2])

            photos.append([[index], each[0],unique])

    return photos