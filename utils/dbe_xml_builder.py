"""This class builds an environment XML file for DriveBuild in the required format."""

import xml.etree.ElementTree as ElementTree
from os import path
import os
from os import remove
from pathlib import Path
from shutil import move


class DBEBuilder:

    def __init__(self):
        # Build a tree structure.
        self.root = ElementTree.Element("environment")
        self.root.set("xmlns", "http://drivebuild.com")
        self.root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        self.root.set("xsi:schemaLocation", "http://drivebuild.com drivebuild.xsd")
        self.author = ElementTree.SubElement(self.root, "author")
        self.author.text = "Michael Heine"

        # Change the light value of the environment as you like.
        self.timeOfDay = ElementTree.SubElement(self.root, "timeOfDay")
        self.timeOfDay.text = "0"

        self.lanes = ElementTree.SubElement(self.root, "lanes")

    def indent(self, elem, level=0):
        """Pretty prints a xml file.
        :param elem: XML tag.
        :param level: Number of empty spaces, initially zero (meaning it starts only a new line).
        :return: Void.
        """
        i = "\n" + level * "    "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "    "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self.indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    def add_obstacles(self, obstacle_list):
        """Adds obstacles to the XML files.
        :param obstacle_list: List of obstacles. Each obstacle is a dict and must contain x and y position. Check
                              generator.py in simnode in DriveBuild to see which object needs which properties.
        :return: Void.
        """
        obstacles = ElementTree.SubElement(self.root, "obstacles")
        for obstacle in obstacle_list:
            name = obstacle.get("name")
            x = obstacle.get("x")
            y = obstacle.get("y")
            z = obstacle.get("z")
            xRot = obstacle.get("xRot")
            yRot = obstacle.get("yRot")
            zRot = obstacle.get("zRot")
            width = obstacle.get("width")
            length = obstacle.get("length")
            height = obstacle.get("height")
            radius = obstacle.get("radius")
            baseRadius = obstacle.get("baseRadius")
            upperWidth = obstacle.get("upperWidth")
            upperLength = obstacle.get("upperLength")
            full_string = '' + name + ' x="' + str(x) + '" y="' + str(y) + '"'
            if z:
                full_string += ' z="' + str(z) + '"'
            if xRot:
                full_string += ' xRot="' + str(xRot) + '"'
            if yRot:
                full_string += ' yRot="' + str(yRot) + '"'
            if zRot:
                full_string += ' zRot="' + str(zRot) + '"'
            if width:
                full_string += ' width="' + str(width) + '"'
            if length:
                full_string += ' length="' + str(length) + '"'
            if height:
                full_string += ' height="' + str(height) + '"'
            if radius:
                full_string += ' radius="' + str(radius) + '"'
            if baseRadius:
                full_string += ' baseRadius="' + str(baseRadius) + '"'
            if upperWidth:
                full_string += ' upperWidth="' + str(upperWidth) + '"'
            if upperLength:
                full_string += ' upperLength="' + str(upperLength) + '"'
            ElementTree.SubElement(obstacles, full_string)

    def add_lane(self, segments, markings: bool = True, left_lanes: int = 0, right_lanes: int = 0):
        """Adds a lane and road segments.
        :param segments: List of dicts containing x-coordinate, y-coordinate and width.
        :param markings: {@code True} Enables road markings, {@code False} makes them invisible.
        :param left_lanes: number of left lanes
        :param right_lanes: number of right lanes
        :return: Void
        """
        lane = ElementTree.SubElement(self.lanes, "lane")
        if markings:
            lane.set("markings", "true")
        if left_lanes != 0 and left_lanes is not None:
            lane.set("leftLanes", str(left_lanes))
        if right_lanes != 0 and right_lanes is not None:
            lane.set("rightLanes", str(right_lanes))
        for segment in segments:
            ElementTree.SubElement(lane, 'laneSegment x="{}" y="{}" width="{}"'
                                   .format(segment.get("x"), segment.get("y"), segment.get("width")))

    def save_xml(self, name):
        """Creates and saves the XML file, and moves it to the scenario folder.
        :param name: Desired name of this file.
        :return: Void, but it creates a XML file.
        """
        # Wrap it in an ElementTree instance, and save as XML.
        tree = ElementTree.ElementTree(self.root)
        self.indent(self.root)
        full_name = name + '.dbe.xml'

        current_path_of_file = Path(os.getcwd())
        current_path_of_file = os.path.realpath(current_path_of_file) + "\\" + full_name

        destination_path = Path(os.getcwd())
        destination_path = os.path.realpath(destination_path) + "\\scenario"

        tree.write(full_name, encoding="utf-8", xml_declaration=True)

        if not path.exists(destination_path):
            os.mkdir(destination_path)

        # Delete old files with the same name.
        if path.exists(destination_path + "\\" + full_name):
            remove(destination_path + "\\" + full_name)

        # Move created file to scenario folder.
        move(current_path_of_file, destination_path)
