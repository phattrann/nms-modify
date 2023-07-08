from src.nms.nms_helper import check_parent_between_2_classes, calculate_iou
from src.parser.hierarchy_parser import HierarchyParser


def nms_modify(bounding_boxes: list[tuple, ],
               scores: list[float, ], 
               classes: list[str, ], 
               hierarchy_parser: HierarchyParser, 
               score_threshold: float, 
               iou_threshold: float
               ) -> list[tuple, ]:
    
    filtered_boxes = []
    filtered_index = set()

    # Question 3.c.1
    indices = [i for i, score in enumerate(scores) if score > score_threshold] # Filtered index of bounding boxes 
    
    indices.sort(key=lambda i: (classes[i], scores[i]), reverse=True)
    i = 0
    while i < len(indices):
        if indices[i] not in filtered_index:
            best_index = indices[i]
            filtered_index.add(indices[i])
            j = i + 1
            while j < len(indices):
                if indices[j] != indices[i]:
                    if calculate_iou(bounding_boxes[indices[i]], bounding_boxes[indices[j]]) > iou_threshold:
                        class_i = classes[indices[i]]
                        class_j = classes[indices[j]]
                
                        if class_i == class_j and scores[indices[j]] < scores[best_index]:
                            # Question 3.c.2: Same Class, Eliminate box j if it has lower confidence than box i
                            filtered_index.add(indices[j])
                        elif class_i != class_j:
                            # Question 3.c.3: Different Class, Eliminate box that is the parent class of another
                            parent_result = check_parent_between_2_classes(hierarchy_parser, class_i, class_j)
                            if parent_result == 1:
                                filtered_index.add(indices[j])
                            elif parent_result == 2:
                                filtered_index.add(indices[i])

                j += 1

        i += 1

    filtered_boxes = [(bounding_boxes[i], scores[i], classes[i]) for i in filtered_index]

    return filtered_boxes
