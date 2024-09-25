import os, shutil

from copy_static import copy_content_src_to_dest

path_public = './public'
path_static = './static'

def main():
    print("Deleting public directory..")
    if os.path.exists(path_public):
        shutil.rmtree(path_public)
    
    print("Copying files from 'static' directory to 'public' directory..")
    copy_content_src_to_dest(path_static, path_public)
    print("Creation of folder(s) and copying of files successful!")


main()