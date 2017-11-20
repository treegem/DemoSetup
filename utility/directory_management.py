import os


def assert_parent_directory(path):
    par_dir = os.path.dirname(path)
    if not os.path.isdir(par_dir):
        os.makedirs(par_dir)
