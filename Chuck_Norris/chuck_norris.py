import binascii


def message_to_binary(message):
    binary = ''
    for letter in message:
        binary += format(int.from_bytes(letter.encode(), 'big'), '#09b')[2:]

    return binary

def chuck_norris(message):

    return '0 0 00 0000 0 00'