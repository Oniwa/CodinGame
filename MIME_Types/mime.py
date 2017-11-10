import os.path


def mime_types(table_length, num_files, association_table, files):
    return ''


def type_to_dict(association_table):
    type_list = []
    for item in association_table:
        split_type = item.split(' ')
        type_list.append(split_type)

    mime_dict = {file_type: content for file_type, content in type_list}

    return mime_dict


def get_file_ext(files):
    file_ext = []

    for item in files:
        # This accounts for the case when the file is '.pdf'
        if item[0] == '.':
            item = 'a' + item
        ext = os.path.splitext(item)[1][1:]
        if ext == '':
            file_ext.append('UNKNOWN')
        else:
            file_ext.append(ext.lower())

    return file_ext
