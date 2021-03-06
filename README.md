Welcome to the Baxter Placing a Cap On a Bottle Project!
===================

University of Minnesota, Twin Cities

CSCI5551: Introduction to Intelligent Robotic Systems (Fall 2017)

Instructor:  Junaed Sattar

Project by: Bat-Orgil Batsaikhan

Overview
-------------

The goal of the project is to have Baxter detect the cap and the bottle via right hand camera and place the cap on the bottle. The MoveIt! package's Inverse Kinematics Service along with ROS integration of Baxter were used for the movement of the arm. OpenCV was used to perform image processing for object detection.

Demo:

[![Video1](https://ibb.co/k7cdPm)](https://drive.google.com/file/d/18sGaCG7gbiijbqib7HrNwQPrwOWVAdSS/view?usp=sharing)

[![Video2](https://ibb.co/k7cdPm)](https://drive.google.com/file/d/1jFv60ZlL8Ck7MG7n_YIpYOsp02bKXgC6/view?usp=sharing)

----------

<a name="Required tools and set up"></a> 
Required tools and set up
-------------
- Baxter Robot (from Rethink Robotics)
- [ROS Kinetic] (Or, ROS Indigo for Ubuntu 14.04)
- [Baxter setup](http://sdk.rethinkrobotics.com/wiki/Baxter_Setup)

------------
Running the Program
-------------
Once you setup the catkin workspace using the setup tutorial, copy the package bat under src.

You need to enable the robot before running the script. Also, configure the right hand camera with 960x600 resolution (works best for me).

Currently, I'm running the scripts through Jupyter Notebook. The object detection only works for water bottles with a small cap and a round opening.

You must modify the following parameters to make it work:
1. Table height
2. Bottle height
3. Parameters for the circle detection algorithm. Appropriate the min/max radius for the bottle opening. Experiment with param1 and param 2.
4. Parameters for the blob detection algorithm. Filtering by the area works best.

To test the program, simply run all cells of the .ipynb file: bat/src/bat/End To End.ipynb. Intermediate cells are helpful for understanding the workflow.
