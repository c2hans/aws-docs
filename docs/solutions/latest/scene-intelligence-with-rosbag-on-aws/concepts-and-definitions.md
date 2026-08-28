---
source_url: https://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/concepts-and-definitions.html
---

# Concepts and definitions
<a name="concepts-and-definitions"></a>

This section describes key concepts and defines terminology specific to this solution:

 **AV/ADAS**

Autonomous Vehicle/Advanced Driver-Assistance System. Developing and deploying AV/ADASs requires scalable compute, storage, networking, analytics, and deep learning frameworks.

 **DAG**

Directed Acyclic Graph. Workflows in Amazon MWAA are authored as DAGs using Python.

 **drive**

Logical grouping of data, such as `Test Car 1 stores its rosbag file on Drive 1`.

 **lane detection (LaneDet)**

A specific object detection model to identify automotive roads within images.

 **object detection**

Refers to identifying objects within an image pulled from the rosbag file. Based on the [COCO dataset](https://cocodataset.org/) for object detection, this term implies the detection of recognized objects such as street lights, stop signs, and people.

 **ROS**

Robot Operating System. The ROS is a set of software libraries and tools that help you build robot applications.

 **rosbag**

A ROS archive file containing sensor data, meant for playback and logging.

 **scene detection**

See **object detection**.

 **YOLO**

You Only Look Once, a PyTorch object detection model.

**Note**
For a general reference of AWS terms, see the [AWS Glossary](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Scene Intelligence with Rosbag on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
