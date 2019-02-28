from input import take_file

photos = take_file('b_lovely_landscapes.txt')

new_photos = []

check = False
for photo in photos:
    if photo[1] == 'H':
        new_photos.append(photo)
    else:
        if check == False:
            prev = photo
            check = True
        else:
            temp = [[prev[0][0], photo[0][0]], 'V', prev[2].union(photo[2])]
            check = False
            new_photos.append(temp)


# print(photos)
print(new_photos)


output = [new_photos[0][0]]
for start in range(len(new_photos)):
    for end in range(start+1, len(new_photos)):
        if len(new_photos[end][2].intersection(new_photos[start][2])) > 0:
            output.append(new_photos[end][0])
            new_photos[start+1], new_photos[end] = new_photos[end], new_photos[start+1]
            break


print(output)

file_output = str(len(output)) + '\n'

for slide in output:
    for pic in slide:
        file_output += str(pic) + ' '
    file_output += '\n'


with open('b_answer.txt', mode='w') as f_out:
    f_out.write(file_output)


