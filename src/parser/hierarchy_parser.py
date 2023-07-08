from src.utils.load_utils import load_txt
from src.utils.text_utils import get_name_mapping


class HierarchyParser:
    def __init__(self, 
                 hierarchy_file: str = "resources/hierarchy.txt", 
                 classname_file: str = "resources/id_to_name.txt"
                 ) -> None:
        self.parent_child_map = {}
        self.child_parent_map = {}
        self.class_name_mapping = get_name_mapping(classname_file)
        self.hierarchy_file = hierarchy_file
    
    def load_resources(self):
        lines = load_txt(self.hierarchy_file)
        for line in lines:
            parent, child = line.strip().split()
            self.parent_child_map.setdefault(parent, []).append(child)
            self.child_parent_map[child] = parent
    
    def get_siblings(self, class_name: str) -> list:
        class_name_id = self.class_name_mapping.get(class_name)
        parent = self.child_parent_map.get(class_name_id)
        if parent:
            siblings = self.parent_child_map.get(parent, [])
            siblings.remove(class_name_id)
            return siblings
        return []
    
    def get_parent(self, class_name: str) -> str:
        class_name_id = self.class_name_mapping.get(class_name)
        return self.child_parent_map.get(class_name_id, None)
    
    def get_parent_by_id(self, class_id: str) -> str:
        return self.child_parent_map.get(class_id, None)
    
    def get_ancestors(self, class_name: str) -> list:
        class_name_id = self.class_name_mapping.get(class_name)
        ancestors = []
        parent = self.get_parent_by_id(class_name_id)
        while parent:
            ancestors.append(parent)
            parent = self.get_parent_by_id(parent)
        return ancestors
    
    def find_common_ancestor(self, class_name1: str, class_name2: str) -> bool:
        ancestors1 = set(self.get_ancestors(class_name1))
        ancestors2 = set(self.get_ancestors(class_name2))
        # common_ancestors = ancestors1.intersection(ancestors2)
        # return len(common_ancestors) > 0
        return bool(ancestors1 & ancestors2)