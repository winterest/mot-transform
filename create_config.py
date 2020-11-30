from configparser import ConfigParser

#Get the configparser object
config_object = ConfigParser()

    #### dataset_file, device, num_queries, aux_loss, masks, frozen_weights, 
    #### bbox_loss_coef, giou_loss_coef, mask_loss_coef, dice_loss_coef, 
    #### dec_layers, eos_coef, 

#Assume we need 2 sections in the config file, let's call them USERINFO and SERVERCONFIG
config_object["DETR"] = {
    "dataset_file": "coco",
    "device": "cuda",
    "num_queries": 100,
    "aux_loss": "True",
    "masks", "False",
    "frozen_weights": "",
    "bbox_loss_coef": 5,
    "giou_loss_coef": 2,
    "mask_loss_coef": 1,
    "dice_loss_coef": 1,
    "dec_layers": 6,
    "eos_coef": 0.1,
    "set_cost_class": "", ##### build_matcher
    "set_cost_bbox": "",
    "set_cost_giou": "",
    "lr_backbone":"", #### build_backbone
    "backbone": "",
    "dilation": "",
    




}

config_object["SERVERCONFIG"] = {
    "host": "tutswiki.com",
    "port": "8080",
    "ipaddr": "8.8.8.8"
}

#Write the above sections to config.ini file
with open('config.ini', 'w') as conf:
    config_object.write(conf)