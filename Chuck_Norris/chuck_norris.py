import binascii


def message_to_binary(message):
    # Truns each character into a binary string that is 7 digits long and
    # returns them as one large string
    binary = ''
    for letter in message:
        binary += format(int.from_bytes(letter.encode(), 'big'), '#09b')[2:]

    return binary


def binary_grouping(binary):
    value = binary[0]
    current_group = ''
    binary_group = []
    while len(binary) > 0:
        element = binary.pop(0)
        if element == value:
            current_group += element
        else:
            binary_group.append(current_group)
            current_group = element
            value = element
        if len(binary) == 0:
                binary_group.append(current_group)

    return binary_group


def chuck_norris(message):
    binary = list(message_to_binary(message))

    grouped = binary_grouping(binary)

    return grouped
