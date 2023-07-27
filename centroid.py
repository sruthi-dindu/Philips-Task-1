import math
#from draw_boundary import *

def centroid(name_bbox, all_bboxes, distance_threshold):
    def calculate_distance(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def find_nearby_bounding_boxes(name_bbox, all_bboxes, distance_threshold):
        all_bboxes.remove(name_bbox)
        name_centroid = [(name_bbox[0][0] + name_bbox[2][0]) / 2, (name_bbox[0][1] + name_bbox[2][1]) / 2]

        """nearby_bboxes = []
        min_distance = 999999999999
        for bbox in all_bboxes:
            centroid = [(bbox[0][0] + bbox[2][0]) / 2, (bbox[0][1] + bbox[2][1]) / 2]
            distance = calculate_distance(name_centroid, centroid)
            if distance < min_distance:
                min_distance = distance
                nearby_bboxes = bbox
                """


        nearby_bboxes = []
        for bbox in all_bboxes:
            centroid = [(bbox[0][0] + bbox[2][0]) / 2, (bbox[0][1] + bbox[2][1]) / 2]
            distance = calculate_distance(name_centroid, centroid)
            if distance < distance_threshold:
                nearby_bboxes.append(bbox)
        print(name_bbox)
        print(nearby_bboxes)
        print("\n")
        #draw_boundary(nearby_bboxes[0])
        return nearby_bboxes
        
    find_nearby_bounding_boxes(name_bbox, all_bboxes, distance_threshold)
    
