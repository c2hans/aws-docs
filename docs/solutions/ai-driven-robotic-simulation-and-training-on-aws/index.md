---
source_url: https://docs.aws.amazon.com/solutions/ai-driven-robotic-simulation-and-training-on-aws/index.html
---

---
title: 'Guidance for AI-Driven Robotic Simulation and Training on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/ai-driven-robotic-simulation-and-training-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for AI-Driven Robotic Simulation and Training on AWS

## Overview

This Guidance demonstrates how to build an AI-assisted robot training and fleet management system using Amazon Bedrock foundation models and AWS Trainium. It helps organizations overcome the complexity of training robots for precise tasks and managing fleets at scale through two complementary methodologies: imitation learning using NVIDIA Isaac Sim on Amazon EC2, and reinforcement learning with Bedrock-generated reward functions. The solution accelerates training with AWS Trainium, standardizes data processing with LeRobot datasets, and enables seamless fleet deployment through AWS IoT Core. This guidance also showcases Reinforcement Learning with Vision Language Action Model reference architecture that shows how to train robot policies using reinforcement learning with Vision-Language-Action (VLA) models on AWS infrastructure. This comprehensive approach reduces implementation time, ensures scalability, and delivers robust industrial robotics capabilities without requiring deep AI expertise.

## Benefits

### Automate robot policy development pipelines

Deploy continuous integration workflows that automatically build, train, and version Vision-Language-Action models when code updates occur. Reduce manual intervention and accelerate iteration cycles by orchestrating distributed GPU training across scalable compute resources.

### Scale multi-modal robot training efficiently

Train complex robotic policies using centralized storage for camera frames, joint states, and language annotations with elastic compute provisioning. Handle large demonstration datasets and distribute training workloads across multiple nodes to fine-tune sophisticated models faster.

### Deploy trained policies seamlessly

Transition trained VLA models from development to production using containerized inference services with automated artifact management. Maintain model lineage and version control while serving real-time action commands to your robot fleet with consistent performance.

## How it works

### Imitation Learning Simulation Environment

This architecture diagram shows a robotic learning system integrating the intelligence of foundation models with ML and mathematical algorithms, accelerated by AWS Trainium/GPU infrastructure and managed through cloud-native technologies.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/ai-driven-robotic-simulation-and-training-on-aws.pdf)Step 1To teach the robot to perform tasks like pushing a T-bar into a T-slot on a workbench, connect to the simulation environment and choose between a single environment for simple tasks or multiple parallel environments for complex training scenarios.Step 2Connect to Isaac Sim simulation environments running in Amazon Elastic Kubernetes Service (Amazon EKS) through Amazon DCV. Deploy the DCV server as a DaemonSet to provide visualization capabilities for simulation pods. Run multiple Isaac Sim environments in parallel across Amazon EKS nodes to enable concurrent processing for simulations and dataset generation. Optional: Consider AWS Batch as an alternative orchestration service to manage multiple Amazon Elastic Compute Cloud (Amazon EC2) instances running Isaac Sim simulations, providing automatic scaling and job management for distributed simulation workloads.Step 3In the NVIDIA Isaac Sim simulation environment, step up the environment with the Universal Scene Description (USD) file.Step 4Isaac Sim generates robot manipulation scenarios with randomized T-bar and robot positions, publishing scene data (camera images, robot poses, object positions) to Robot Operating System 2 (ROS 2) topics at 10-30 Hz frequency.Step 5Amazon Bedrock foundation models analyze the robot workspace conditions (object distances, robot positioning, environmental constraints) and return high-level strategy recommendations. For advanced and complex tasks, use Amazon Bedrock AgentCore with Strands agents and Model Context Protocol (MCP) server to coordinate and orchestrate the tasks.Step 6The application logic in the simulation environment processes AI strategies and uses ML algorithms to generate safe robot positions and velocities, while simultaneously storing all episode data through the HuggingFace LeRobot library for optimized formatting and preprocessing.Step 7Completed episodes are organized using LeRobot's standardized directory structure organize (data/chunk-000/episode_000000.parquet) and automatically uploaded with metadata files enabling seamless integration with LeRobot training pipelines.Step 8The Amazon Simple Storage Service (Amazon S3) bucket triggers AWS Lambda functions upon new episode uploads to update the LeRobot dataset indices and notify the Amazon EKS or GPU training orchestration system of available data for processing.Step 9The Amazon EKS cluster with dedicated AWS Trainium node groups (trn1.32xlarge instances) or GPUs receives training job requests and provisions containerized training environments with LeRobot framework.Step 10LeRobot's ecosystem processes Amazon S3 episode data, implementing DiffusionPolicy with GPU/Trainium optimizations. The system executes mixed-precision distributed training and packages final models for Amazon S3 and HuggingFace Hub. The pipeline uses transformers, accelerator-specific operations, and standardized workflows throughout.Step 11AWS IoT Core manages robot fleet deployment by creating AWS IoT Jobs for model distribution. Robots subscribe to these jobs, download and validate LeRobot models from Amazon S3, and execute standardized deployment steps. The AWS IoT device management with IoT jobs monitors deployment progress and can trigger rollbacks if needed. Successfully deployed robots publish operational metrics while performance data streams to Amazon S3.Step 12The imitation learning pipeline uses AWS IAM roles for service-to-service authentication between core components (Amazon EKS, Amazon S3, Amazon Bedrock, AWS Lambda, AWS IoT Core) and controls access to resources. Robot devices authenticate using IoT thing policies while accessing Amazon S3 for model downloads, with all cross-service communications enforced through least-privilege IAM policies.### Reinforcement Learning Training Environment

This architecture diagram shows developers how to train robotic agents using NVIDIA Isaac Sim on Amazon EKS with LLM-generated reward functions, then automatically deploy trained models to physical robots using AWS IoT services.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/ai-driven-robotic-simulation-and-training-on-aws.pdf)Step 1A developer deploys the NVIDIA Isaac Sim on Amazon Elastic Kubernetes Service (Amazon EKS) and accesses its interface via Amazon DCV. The developer defines a task (e.g. opening a box) within the Isaac Sim environment, which serves as the simulation environment for the reinforcement learning agent to train on.Step 2The Isaac Sim controller pods leverage Amazon Bedrock to sample reward functions from the Large Language Model (LLM). This automated process of generating reward functions is a key innovation, as crafting effective reward functions manually can be very challenging.Step 3Amazon SQS receives the award function along with the training and simulation input data, as a message. The Amazon SQS queue acts as the intermediary between the reward function generation and the training execution.Step 4The Isaac Sim training pods read the message from the Amazon SQS queue and execute the training and simulation processes.Step 5The input data files and results are read and stored using an Mountpoint for Amazon Simple Storage Service (Amazon S3), which provides a cost-effective and low-latency file storage solution for the training artifacts.Step 6The developer interactively observes and debugs the training process in near real-time through the Amazon DCV remote visualization interface, gaining valuable insights into the agent's learning progress.Step 7The developer stores new model files in an Amazon S3 bucket for persistence.Step 8At the time of model creation, the creation event in Amazon S3 triggers an AWS Lambda function. This function deploys the trained model to the physical robot devices. The AWS Lambda function creates an AWS IoT Job in the AWS IoT Device Management service. AWS IoT Device Management handles scheduling, retrying, and reporting the status of remote operations on the robot devices, ensuring reliable and scalable model deployment.Step 9AWS IoT Device Management publishes the AWS IoT Job to AWS IoT Core, the managed message broker service that distributes the job information to the connected robot devices.Step 10The robotic devices subscribe to job notifications from AWS IoT Core. The robotics team implements the logic to retrieve and process robot-side job notifications.Step 11The robotic devices download the newly trained model from Amazon S3 and deploy it locally on the robot hardware, completing the loop of simulation-based training and real-world deployment.Step 12The reinforcement learning pipeline uses AWS IAM roles to secure the training flow between Amazon EKS, Amazon Bedrock (LLM reward functions), Amazon SQS, and Amazon S3 Mountpoint for data storage. The deployment flow leverages AWS IAM to enable AWS Lambda's model deployment pipeline and IoT thing policies for robot authentication when accessing AWS IoT Core and Amazon S3.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Imitation Learning and Simulation Environment**: Ready to deploy? Review the Imitation Learning in Simulation Environment sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-ai-driven-robotic-simulation-and-training-on-aws)

- **Reinforcement Learning with Vision Language Action Model**: Ready to deploy? Review the Reinforcement Learning with Vision Language Action Model sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-ai-driven-robotic-simulation-and-training-on-aws/tree/main/reinforcement_learning_vla/nvidia-gr00t-vla)

## Related content

- **Train Robot Learning on AWS Using LLM-Generated Functions**: This blog shows scalable robot learning on AWS using LLMs for reward functions with EKS and FSx.

[Read the blog](https://aws.amazon.com/blogs/industries/how-to-expansively-train-robot-learning-by-customers-on-aws-using-functions-generated-by-large-language-models/)

- **Getting Started with Robot Learning on AWS Batch**: This blog demonstrates how to build scalable infrastructure to fine-tune Isaac GR00T on AWS.

[Read the blog](https://aws.amazon.com/blogs/physical-ai/embodied-ai-blog-series-part-1/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
