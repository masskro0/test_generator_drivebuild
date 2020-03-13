from shutil import move
from test_generator import TestGenerator
from os import path


def move_files(dbe, dbc):
    """Moves specified xml files to the done folder.
    :param dbc: Full path to the dbc file.
    :param dbe: Full path to the dbe file.
    :return: Void.
    """
    destination_path = path.dirname(path.realpath(__file__)) + "\\done"
    filename_dbc = path.basename(path.normpath(dbc))
    filename_dbe = path.basename(path.normpath(dbe))
    move(dbc, path.join(destination_path, filename_dbc))
    move(dbe, path.join(destination_path, filename_dbe))


if __name__ == '__main__':
    gen = TestGenerator("easy")         # Parameter is optional, you can also call gen.set_difficulty(str)
    gen.set_files_name("test_case")     # This method call is optional
    """
    while True:
        for paths in gen.getTest():
            dbe = paths[0]
            dbc = paths[1]
            # All your code goes here
            # Be sure to call onTestFinished(sid, vid)
    """
    while True:
        gen.genetic_algorithm()