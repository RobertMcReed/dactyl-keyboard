import os

# This is a dirty hack to modify the x3d files after generation
# so that the two keyboards can be shown at once with space in between

out_dir='render'
filenum = 0
for file in os.listdir(out_dir):
    if 'x3d' not in file:
        continue

    with open('{}/{}'.format(out_dir, file), 'r+') as f:
        filenum+=1
        lines = f.readlines()

        new_lines = []
        for line in lines:
            if not '<Coordinate point="' in line:
                new_lines.append(line)
                continue
            
            new_line = line.strip()
            new_line = new_line.replace('<Coordinate point="', '')
            new_line = new_line.replace(' " />', '')
            numbers = new_line.split(' ')
            new_numbers = []

            operator = -1 if filenum % 2 else 1

            for i, num in enumerate(numbers):
                if i % 3 == 0:
                    new_numbers.append(str(float(num) + 250 * operator))
                else:
                    new_numbers.append(num)
            newer_line = '<Coordinate point="{} " />'.format(
                ' '.join(new_numbers)
            )
            new_lines.append(newer_line)
        
        f.seek(0)
        f.write('\n'.join(new_lines))
        f.truncate()
