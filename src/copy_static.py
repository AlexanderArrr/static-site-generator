import os, shutil

def copy_content_src_to_dest(srcpath, destpath):
    log_dict = {}

    if not os.path.exists(destpath):
        log_dict[destpath] = 'Directory'
        os.mkdir(destpath)
    src_file_list = os.listdir(srcpath)
    for entry in src_file_list:
        entry_srcpath = os.path.join(srcpath, entry)
        entry_destpath = os.path.join(destpath, entry)
        if not os.path.isfile(entry_srcpath):
            copy_content_src_to_dest(entry_srcpath, entry_destpath)
        if not os.path.exists(entry_destpath):
            shutil.copy(entry_srcpath, entry_destpath)
            log_dict[entry_srcpath] = 'File'
            log(log_dict, entry_destpath)
    return


def log(log_dict, file_destpath=None):
    if not len(log_dict) == 0:
        for key, value in log_dict.items():
            if value == 'Directory':
                print(f"{value} '{key}' created")
            if value == 'File':
                print(f"{value} '{key}' copied to '{file_destpath}'")