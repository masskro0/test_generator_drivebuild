from test_generator import TestGenerator
from utils.xml_to_bng_files import convert_test

if __name__ == '__main__':
    gen = TestGenerator("easy")         # Parameter is optional, you can also call gen.set_difficulty(str)
    gen.set_files_name("test_case")     # This method call is optional

    while True:
        for paths in gen.getTest():
            dbe = paths[0]
            dbc = paths[1]
            # convert_test(dbc, dbe)        # Use this function only when DriveBuild doesn't work for you.
            # All your code goes here
            # Be sure to call onTestFinished(sid, vid)
