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
       fitness value.
       
This generator offers a module to run and calculate the fitness value local in beamngpy. If you 
don't need it, skip now to Troubleshooting.
Additionally install the the requirements of requirements_local.txt. Before running run_local.py in
the utils directory you must follow these steps:
       
    - Mainapp and Simnode must be listening for connections and requests before running the
      test generator
    - run_local.py: You must change two paths. The first one points to the directory where
      DriveBuild stores its created JSON, LUA and PREFAB files. It is in the user path, e.g.
      "C:\\Users\\MaSSK\\Documents\\BeamNG.research", where several drivebuild directories
      are created, e.g. drivebuild10.
      The second path is your trunk folder. Go to your BeamNG trunk folder (where you have
      installed BeamNG) and go to the levels directory. If you haven't already then create
      a directory called "drivebuild" and in there a directory called "scenarios". Change
      the destination_path to the scenarios path, e.g. 
      'D:\\Program Files (x86)\\BeamNG\\levels\\drivebuild\\scenarios'. 
    - Put your trained model in ai/models, your prediction in ai (optional) and your AI car
      in test_subjects. Of course this is dependent on your implementation.
    
    
Troubleshooting:

     - If DriveBuild doesn't start when the generator should calculate the fitness values or start
       the test cases, then you have to restart SimNode and the test generator/test execution.
     - Don't worry if generating points or mutation seems to be stuck. These operations are
       computationally heavy and need some time to finish. In the worst case you have to wait
       up to 120 seconds.
     - If you get any file errors, try to delete everything from the scenario and done folder
     - If no progress is made after 4 minutes, restart the test generator and DriveBuild, which
       is caused by some false configuration probably.
   
    