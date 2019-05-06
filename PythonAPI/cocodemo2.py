from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
pylab.rcParams['figure.figsize'] = (8.0, 10.0)

if __name__ == "__main__":
    littleCo = COCO('F:/cocoapi/annotations/instances_val2017.json')
    #id_laptop = littleCo.getCatIds('laptop')

"""Extracting image ids corresponding to backpack and laptop images."""
    bag_img_ids = littleCo.getImgIds(catIds=[27])
    laptop_img_ids = littleCo.getImgIds(catIds=[73])
    #print "IDs of bag images:", bag_img_ids
    #print "IDs of laptop imgs:", laptop_img_ids

"""Extracting annotation ids corresponding to backpack and laptop images."""
    bag_ann_ids = littleCo.getAnnIds(catIds=[27])
    laptop_ann_ids = littleCo.getAnnIds(catIds=[73])
    #print "Annotation IDs of bags:", bag_ann_ids
    #print "Annotation IDs of laptops:", laptop_ann_ids

"""Extracting image names corresponding to bag and laptop categories."""
    bag_imgs = littleCo.loadImgs(ids=bag_img_ids)
    laptop_imgs = littleCo.loadImgs(ids=laptop_img_ids)
    #print "Bag images:", bag_imgs
    #print "Laptop images:", laptop_imgs

    bag_img_names = [image['file_name'] for image in bag_imgs]
    laptop_img_names = [image['file_name'] for image in laptop_imgs]
    print "Bag Images:", len(bag_img_names), bag_img_names[:5]
    print "Laptop Images:", len(laptop_img_names), laptop_img_names[:5]

"""Extracting annotations corresponding to bag and laptop images."""
    bag_ann = littleCo.loadAnns(ids=bag_ann_ids)
    laptop_ann = littleCo.loadAnns(ids=laptop_ann_ids)
    bag_bbox = [ann['bbox'] for ann in bag_ann]
    laptop_bbox = [ann['bbox'] for ann in laptop_ann]
    print "Bags' bounding boxes:", len(bag_ann), bag_bbox[:5]
    print "Laptops' bounding boxes:", len(laptop_bbox), laptop_bbox[:5]

"""Saving files corresponding to bags and laptop category in a directory."""
    import shutil
    #path_to_imgs = "/export/work/Data Pool/coco_data/train2014/"
    #path_to_subset_imgs = "/export/work/Data Pool/coco_subset_data/"
    path_to_ann = "F:/cocoapi/PythonAPI/annotations/"
    dirs_list = [("F:/cocoapi/PythonAPI/val2017/", "F:/cocoapi/PythonAPI/")]

    for source_folder, destination_folder in dirs_list:
        for img in bag_img_names:
            shutil.copy(source_folder + img, destination_folder + img)
        print "Bag images copied!"
        for img in laptop_img_names:
            shutil.copy(source_folder + img, destination_folder + img)
        print "Laptop images copied!" 

"""Creating empty files for annotation."""
    for f in os.listdir("F:/cocoapi/images/"):
        if f.endswith('.jpg'):
            open(os.path.join(path_to_ann, f.replace('.jpg', '.txt')), 'w+').close()
    print "Done creating empty annotation files." 