from src.utils.load_utils import load_txt


def get_name_mapping(file_name: str) -> dict:
    id_to_name = load_txt(file_name)

    name_to_id = {} 
    for i in range(len(id_to_name)):
        idx = id_to_name[i].split("\t")[0].strip()
        name = id_to_name[i].split("\t")[1].strip()
        name_to_id[name] = idx
    return name_to_id
