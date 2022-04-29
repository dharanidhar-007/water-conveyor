

def New_Folder(name):
    import os

    directory = name

    parent_dir = 'D:\WaterDispenserRecord\{}'.format(directory)

    os.mkdir(parent_dir)
    print("Directory '% s' created" % directory)
