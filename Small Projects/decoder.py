def decode(message_file):
    decoded_dict = {}
    with open(message_file, 'r') as file:
        lines = file.readlines()
        nums = len(lines)
        for line in lines:
            num, word = line.split()
            decoded_dict[int(num)] = word.strip()

    pyramid = []
    num = 1
    while num <= nums:
        row = []
        for j in range(len(pyramid) + 1):
            if num <= nums:
                row.append(num)
                num += 1
        pyramid.append(row)

    last_elements = [sublist[-1] for sublist in pyramid]
    output_message = [decoded_dict[element] for element in last_elements]
    return ' '.join(output_message)


# Test the function
decoded_message = decode('input.txt')
print(decoded_message)
