---
source_url: https://docs.aws.amazon.com/solutions/physical-ai-for-robotics-on-aws/index.html
---

---
title: 'Guidance for Physical AI for Robotics on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/physical-ai-for-robotics-on-aws/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Physical AI for Robotics on AWS

## Overview

This Guidance demonstrates how to integrate advanced AI capabilities with physical robotics systems on AWS, enabling autonomous operation in real-world environments. It helps organizations implement end-to-end solutions for developing and training robots with AI-based autonomy, combining deep learning, large language models, and reinforcement learning with physical sensing and control systems. The solution shows both robotics OEMs and industrial users how to create adaptive, self-learning robots that can perceive, reason, and interact autonomously in operational settings. Furthermore, it demonstrates how to leverage AWS's scalable infrastructure for continuous simulation, training, and improvement of robotic systems that evolve to meet changing industrial needs.

## Benefits

### Bridging simulation to reality gap

Enable seamless transition of Physical AI virtual training to real-world deployment while continuing the training in real-world environments modeled by intelligent sensors to meet target autonomous robot application requirements.

### Flexible development with powerful tools

Accelerate development by choosing between simulation with NVIDIA's physics engine or real-world training with Amazon SageMaker's ML capabilities, and combining both paths for comprehensive Physical AI robot applications development.

### Intelligent edge for continuous learning

Enable continuous robot evolution with AWS IoT Greengrass edge deployment that serves a dual purpose - executing ML inference for real-time robot control while simultaneously collecting sensor data for ongoing model improvement and adaptation.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/physical-ai-for-robotic-applications-on-aws.pdf)

![Architecture diagram](/images/solutions/physical-ai-for-robotics-on-aws/images/physical-ai-for-robotics-on-aws-1.png)

1. **Step 1**: Begin Simulation training with robotics reinforcement learning using NVIDIA Isaac Sim containers deployed on GPU-powered Amazon Elastic Compute Cloud (Amazon EC2) instances for modeling and NVIDIA Isaac Lab to scale training scenarios. Test physics constraints and scenarios through multiple iterations within this simulation loop.
1. **Step 2**: AWS Batch orchestrates simulation workloads across GPU-powered Amazon EC2 Auto Scaling groups to dynamically scale compute resources based on demand.
1. **Step 3**: One-way Deployment: The trained ML model with robot policies are deployed one-way to AWS IoT Greengrass running on physical controllers that interface with robots at the edge.
1. **Step 4**: AWS IoT Greengrass components process real-time physics and environmental feedback data from sensors including cameras, audio, gyroscopes, force, accelerometers, contact sensors, joint encoders, position, and pressure sensors.
1. **Step 5**: AWS IoT Greengrass sends MQTT sensor data through AWS IoT Core and Amazon Data Firehose to Amazon Simple Storage Service (Amazon S3) data lakes, while video streams flow via Amazon Kinesis Video Streams to Amazon S3 for storage and management
1. **Step 6**: Amazon SageMaker AI processes batches of real-world data to train and/or retrain and optimize models, bridging sim-to-real gaps between NVIDIA Isaac Sim virtual simulation and actual robot operations.
1. **Step 7**: Continuous Deploy and Monitor: Refined ML models trained in Amazon SageMaker AI are deployed to AWS IoT Greengrass on the robot edge. Inference is performed using these models to optimize robot behavior and meet performance goals. A monitoring layer tracks metrics, detects drift, and triggers retraining. ML model iteration continues through this cycle: robots generate operational data, models are refined based on real-world performance, and improved models are redeployed.
[Read usage guidelines](/solutions/guidance-disclaimers/)
