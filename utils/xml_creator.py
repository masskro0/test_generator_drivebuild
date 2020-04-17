"""This file offers methods to create xml files of a list of control points.
  Methods are preconfigured to meet the requirements of the road_generator.py
  class.
"""

from utils.dbe_xml_builder import DBEBuilder
from utils.dbc_xml_builder import DBCBuilder


def build_environment_xml(control_points, file_name="exampleTest", left_lanes=0, right_lanes=0, obstacles=[]):
    """Creates a dbe xml file.
    :param control_points: List of dicts containing control points.
    :param file_name: Name of this dbe file.
    :param left_lanes: Number of left lanes.
    :param right_lanes: Number of right lanes.
    :param obstacles: List of dicts containing obstacles.
    """
    dbe = DBEBuilder()
    dbe.add_lane(control_points, left_lanes=left_lanes, right_lanes=right_lanes)
    if obstacles is not None and len(obstacles) > 0:
        dbe.add_obstacles(obstacles)
    dbe.save_xml(file_name)


def build_criteria_xml(participants: list, ego_car: dict, success_points: list, vc_pos, sc_speed, file_name: str ="exampleTest",
                       name: str ="Example Test", fps: str ="60", frequency: str ="6"):
    """Creates a dbc xml file. Failure, success and preconditions are controlled
      manually for this test generation since the road_generator creates simple
      lane following tests.
    :param sc_speed: Speed condition that has to be met at vc_pos.
    :param vc_pos: Position which must be entered at a specific speed by a specific participant.
    :param participants: List of dicts of car states. See the add_car method in dbc_xml_builder.py for more
                         information.
    :param ego_car: The test subject as dict. Contains the same information as any other participant.
    :param success_points: List with points of success. Each one is a dict with x, y and tolerance.
    :param file_name: Name of this dbc file. Should be the same as the environment file (laziness).
    :param name: Self defined description name of this file.
    :param fps: Frames per second.
    :param frequency: Frequency of the AI to compute the next step.
    :return: Void.
    """
    dbc = DBCBuilder()
    dbc.define_name(name)
    dbc.environment_name(file_name)
    dbc.steps_per_second(fps)
    dbc.ai_freq(frequency)
    for participant in participants:
        dbc.add_car(participant)
    for success_point in success_points:
        dbc.add_success_point(ego_car.get("id"), success_point)
    dbc.add_failure_conditions(ego_car.get("id"), "offroad")
    dbc.add_precond_partic_sc_speed(vc_pos, sc_speed)
    dbc.save_xml(file_name)


def build_xml(individual, iterator: int = 0):
    """Builds an environment and criteria xml file out of a list of control points.
    :param individual: obstacles (list), number of right lanes (int), number of left lanes (int),
                        control points (list), file name (string), participants (list)
    :param iterator: Unique index of a population.
    :return: Void.
    """
    obstacles = individual.get("obstacles")
    right_lanes = individual.get("right_lanes")
    left_lanes = individual.get("left_lanes")
    control_points = individual.get("control_points")
    file_name = individual.get("file_name")
    participants = individual.get("participants")
    file_name = file_name + str(iterator)
    success_point = {"x": control_points[-1].get("x"),
                     "y": control_points[-1].get("y"),
                     "tolerance": control_points[-1].get("width") / 2}
    success_points = [success_point]
    ego = None
    for participant in participants:
        if participant.get("id") is "ego":
            ego = participant
            break
    vc_pos = {"id": ego.get("id"),
              "tolerance": 3,
              "x": control_points[1].get("x"),
              "y": control_points[1].get("y")}
    sc_speed = 10
    build_environment_xml(control_points=control_points, file_name=file_name, left_lanes=left_lanes,
                          right_lanes=right_lanes, obstacles=obstacles)
    build_criteria_xml(participants=participants, ego_car=ego, success_points=success_points,
                       file_name=file_name, vc_pos=vc_pos, sc_speed=sc_speed)


def build_all_xml(population):
    """Calls the build_xml method for each individual.
    :param population: List of individuals containing control points and a fitness value for each one.
    :return: Void.
    """
    iterator = 0
    while iterator < len(population):
        build_xml(population[iterator], iterator)
        iterator += 1
