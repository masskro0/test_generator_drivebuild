# Search-based Software Engineering for Testing Autonomous Cars

A test generator utilizing a genetic algorithm to generate test cases for DriveBuild
for the simulator BeamNG.research.

Please read carefully before you run anything. Also, use virtual environments.

Prerequisites:

     1. You need Windows 10
     2. Install BeamNG.reseach and beamngpy according to the instructions: https://github.com/BeamNG/BeamNGpy
     3. Install Python 3.7.0 or higher
     4. Install DriveBuild according to the instructions: https://github.com/TrackerSB/DriveBuild
     

Instructions:

     - Create a virtual environment and install the requirements from requirements.txt
     
     - Install Shapely from this directory directly from Powershell
   
     - In test_generator.py you have to change the service in the onTestFinished method if it 
       differs from my implemented one.
       
     - See the interface.py module to see how to instantiate the test generator. You basically have
       to generate a TestGenerator object and call getTest() in a loop to generate test cases.
       Additionally, you can set the difficulty by set_difficulty(str) and set the files name
       set_files_name(str) ["easy", "medium", "hard"] but these are optional.
       
     - DriveBuild must call onTestFinished(sid, vid) so the test generator can determine the 
       fitness value after test execution.
       
In case that DriveBuild is not working for you, you can use the convert_test function like
in interface.py. This will use DriveBuild to convert the xml files into game files and
automatically move it to the scenario folder. You have to change the paths in
xml_to_bng_files.py. Make sure that Mainapp as well as SimNode of DriveBuild are running.
    
Troubleshooting:

     - If DriveBuild doesn't start when the generator should calculate the fitness values or start
       the test cases, then you have to restart SimNode and the test generator/test execution.
     - Don't worry if generating points or mutation seems to be stuck. These operations are
       computationally heavy and need some time to finish. In the worst case you have to wait
       up to 30 seconds.
     - If you get any file errors, try to delete everything from the scenario and done folder
     - If no progress is made after 1 minute, restart the test generator and DriveBuild, which
       is caused by some false configuration probably.
   
    
