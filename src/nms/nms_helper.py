from src.parser.hierarchy_parser import HierarchyParser


def check_parent_between_2_classes(hierarchy_parser: HierarchyParser, 
                                   class1: str, 
                                   class2: str
                                   ) -> int:
    parent1 = hierarchy_parser.get_parent(class1)
    parent2 = hierarchy_parser.get_parent(class2)
    
    if parent1 == class2:
        return 2
    elif parent2 == class1:
        return 1
    return 0

def calculate_iou(box1: tuple, 
                  box2: tuple
                  ) -> float:
    """
    Considering coordinates of the bounding box in the tuple format (x1, y1, x2, y2).
    """
    x1_i = max(box1[0], box2[0])
    y1_i = max(box1[1], box2[1])
    x2_i = min(box1[2], box2[2])
    y2_i = min(box1[3], box2[3])

    intersection_area = max(0, x2_i - x1_i) * max(0, y2_i - y1_i)
    box1_area = (box1[2] - box1[0]) * (box1[3] - box1[1])
    box2_area = (box2[2] - box2[0]) * (box2[3] - box2[1])
    union_area = box1_area + box2_area - intersection_area
    iou = intersection_area / union_area if union_area > 0 else 0
    return iou
