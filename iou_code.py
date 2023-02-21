box1 = [2 , 3 , 12 , 15] #ground truth
box2 = [8 , 10 , 20 , 23] #predicted

#intersection

xl = max(box1[0] , box2[0])
yl = max(box1[1] , box2[1])
xr = min(box1[2] , box2[2])
yr = min(box1[3] , box2[3])

area_intersection = (xr - xl) * (yr - yl)

#union

width_box1 = box1[2] - box1[0]
height_box1 = box1[3] - box1[1]
width_box2 = box2[2] - box2[0]
height_box2 = box2[3] - box2[1]

area_box1 = width_box1 * height_box1
area_box2 = width_box2 * height_box2

union_area = area_box1 + area_box2 - area_intersection

iou = area_intersection / union_area

print(iou)
