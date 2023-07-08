import random

from src.utils.load_utils import seed_everything
from src.const import const_map as CONST_MAP 
from src.parser.hierarchy_parser import HierarchyParser
from src.nms.nms import nms_modify 


seed_everything(CONST_MAP.SEED_VALUE)

if __name__ == "__main__":
    hierarchy = HierarchyParser("resources/hierarchy.txt", "resources/id_to_name.txt")
    hierarchy.load_resources()
    
    """
    Class Hierarchy 
    """
    
    siblings = hierarchy.get_siblings('physical entity')
    print(f"Siblings: {siblings}")

    parent = hierarchy.get_parent('congener')
    print(f"Parent: {parent}")

    ancestors = hierarchy.get_ancestors('congener')
    print(f"Ancestors: {ancestors}")

    common_ancestor = hierarchy.find_common_ancestor('physical entity', 'thing')
    print(f"Having the same ancestor: {common_ancestor}")

    """
    NMS function
    """

    bounding_boxes = [[random.randint(0, 20) for _ in range(4)] for _ in range(5)]
    confidence_scores = [random.random() for _ in range(5)]
    class_labels = ['n13489037', 'n07066659', 'n00893836', 'n04234763', 'n08498888']
    
    boxes = nms_modify(bounding_boxes=bounding_boxes,
                       scores=confidence_scores,
                       classes=class_labels,
                       hierarchy_parser=hierarchy,
                       score_threshold=CONST_MAP.SCORE_THRESHOLD,
                       iou_threshold=CONST_MAP.IOU_THRESHOLD)
    print(f"Filtered Bounding Boxes: {boxes}")