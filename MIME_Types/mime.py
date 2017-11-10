def mime_types(table_length, num_files, association_table, files):
    return ''

def type_to_dict(association_table):
    type_list = []
    for item in association_table:
        split_type = item.split(' ')
        type_list.append(split_type)

    mime_dict = {file_type: content for file_type, content in type_list}

    return mime_dict
