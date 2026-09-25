---
source_url: https://docs.aws.amazon.com/solutions/implementing-ai-powered-visual-quality-management-with-softserve-edgeinsight-on-aws/index.html
---

---
title: 'Guidance for Implementing AI-Powered Visual Quality Management with SoftServe EdgeInsight on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/implementing-ai-powered-visual-quality-management-with-softserve-edgeinsight-on-aws/
source: aws-documentation
generated_on: 2026-09-25
---

# Guidance for Implementing AI-Powered Visual Quality Management with SoftServe EdgeInsight on AWS

## Overview

This Guidance demonstrates how to implement advanced industrial quality management using AI-powered computer vision at the edge with the EdgeInsight solution accelerator on AWS. It helps manufacturers rapidly deploy sophisticated monitoring systems that process video streams in near real-time using NVIDIA-accelerated machine learning. Organizations can benefit from local processing of camera feeds, seamless integration with existing factory OT data sources, and flexible data routing to either AWS cloud services or on-premise databases. This Guidance enables quick deployment of intelligent quality control systems while maintaining operational efficiency and reducing latency through edge processing.

## Benefits

### Accelerate industrial vision deployment

Deploy AI-powered computer vision applications at the edge in less time with standardized interfaces for diverse camera systems. You can rapidly implement quality inspection and monitoring solutions without managing complex hardware protocols or vendor-specific specifications.

### Enhance operational intelligence

Correlate visual data with operational technology inputs to gain comprehensive manufacturing insights. By combining video analytics with data from PLCs, DCS, and SCADA systems, you can identify root causes of quality issues and optimize production processes.

### Streamline continuous improvement

Implement a complete edge-to-cloud ML lifecycle that evolves with your manufacturing needs. Your models can be continuously trained with real and synthetic data in SageMaker, then securely deployed to edge devices through automated MLOps pipelines.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/implementing-ai-powered-visual-quality-management-with-softserve-edgeinsight-on-aws.pdf)

![Architecture diagram](/images/solutions/implementing-ai-powered-visual-quality-management-with-softserve-edgeinsight-on-aws/images/implementing-ai-powered-visual-quality-management-with-softserve-edgeinsight-on-aws-1.png)

1. **Step 1**: Connect to video feeds from factory-mounted cameras or Video Management Systems (VMS) for primary data input. Supplement training with synthetic data to expand test datasets and simulate rare defect patterns beyond typical factory scenarios.
1. **Step 2**: Deploy AWS IoT Greengrass on an NVIDIA Jetson device or Industrial PC (IPC) with discrete GPU to run the edge data processing pipeline.
1. **Step 3**: Create a Data Processing pipeline with Video Interface Manager to standardize interactions with Open Network Video Interface Forum (ONVIF) cameras, Real-Time Streaming Protocol (RTSP) streams, and GigE Vision systems. This abstraction layer eliminates the need to handle proprietary hardware protocols or vendor-specific specifications.
1. **Step 4**: Implement an RTSP server as a video stream broker to manage complex routing of video streams. This enables multiple components to access and process video data simultaneously while maintaining system performance.
1. **Step 5**: Deploy the NVIDIA DeepStream Computer Vision (DSCV) pipeline to analyze video in near real-time. This high-throughput, low-latency platform uses hardware acceleration to perform tasks from object detection to quality inspection.
1. **Step 6**: Use the Video Stream Export Manager (VSEM) to transfer processed or raw video to AWS Cloud storage and services through batch or near real-time operations.
1. **Step 7**: Configure the Data Integration Module to process inference data and execute business logic at the edge. Transform raw DeepStream CV data through filtering, aggregation, and enrichment. Combine video analytics with OT process data from Programmable Logic Controllers (PLC), Distributed Control System (DCS), and Supervisory Control and Data Acquisition (SCADA) systems for comprehensive context, such as correlating conveyor state data with object detection.
1. **Step 8**: Implement near real-time and batch video/data stream processing through interconnected services for seamless edge-to-cloud operations using AWS IoT Core, Amazon Simple Storage Service (Amazon S3), Amazon Kinesis Video Streams, Amazon Kinesis Data Streams, and AWS IoT SiteWise.
1. **Step 9**: Set up AWS IoT Core for secure bidirectional communication with edge compute devices. Use device shadows to maintain configuration synchronization during intermittent connectivity or partially air-gapped factory operations.
1. **Step 10**: Use Amazon S3 to store video artifacts and ML models for edge deployment, providing scalable object storage.
1. **Step 11**: Use Amazon Kinesis Data Streams and Amazon Kinesis Video Streams to ingest real-time video and inference metadata.
1. **Step 12**: Configure AWS IoT SiteWise to create digital representations of industrial data hierarchies. Enable production managers to correlate defect rates with machine parameters, linking visual defects to specific temperature, vibration, or other operational fluctuations.
1. **Step 13**: Use AWS Lambda as a connective layer between services to process edge-generated data and cloud operations. Transform data between services, extract video metadata, process inference outputs, trigger container deployments, and manage over-the-air update notifications and verifications.
1. **Step 14**: Deploy Amazon SageMaker AI as the ML foundation for EdgeInsight's AI-on-the-Edge computer vision continuous improvement cycle. Data scientists use Amazon SageMaker AI to train models using real or NVIDIA Omniverse-generated synthetic data, then store trained models in Amazon S3.
1. **Step 15**: Trigger ML Ops pipeline using AWS Lambda to package ML models as Docker containers and store them in Amazon Elastic Container Registry (Amazon ECR).
1. **Step 16**: Configure Docker Application Manager to pull images from Amazon ECR and deploy software updates and optimized Amazon SageMaker AI MLOps models to edge devices, ensuring secure and efficient delivery of improvements.
[Read usage guidelines](/solutions/guidance-disclaimers/)
