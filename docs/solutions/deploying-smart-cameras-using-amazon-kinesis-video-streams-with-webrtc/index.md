---
source_url: https://docs.aws.amazon.com/solutions/deploying-smart-cameras-using-amazon-kinesis-video-streams-with-webrtc/index.html
---

---
title: 'Guidance for Deploying Smart Cameras Using Amazon Kinesis Video Streams with WebRTC'
canonical_url: https://docs.aws.amazon.com/solutions/deploying-smart-cameras-using-amazon-kinesis-video-streams-with-webrtc/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Deploying Smart Cameras Using Amazon Kinesis Video Streams with WebRTC

## Overview

This Guidance demonstrates how to use Amazon Kinesis Video Streams with WebRTC to enable low-latency, bi-directional, peer-to-peer video streaming from home surveillance cameras. Kinesis Video Streams, a managed service for real-time video processing, can store video and other media files for replay and analytics, while WebRTC facilitates direct, low-latency connections between the camera and client applications. This Guidance allows seamless, responsive home monitoring from mobile devices or web browsers, as the peer-to-peer WebRTC connection minimizes latency and bandwidth compared to traditional client-server streaming. It also includes sample applications with the included software development kit (SDK). Camera manufacturers and connected home providers can use the SDK as a starting point to build custom camera management and viewing experiences. This helps them to more easily integrate high-quality, low-latency video capabilities into their connected home offerings and provides consumers with a reliable home monitoring experience.

## How it works

### Live View Smart Home Surveillance Cameras

This architecture diagram shows how use Kinesis Video Streams for WebRTC, allowing for the low-latency, bi-directional, peer-to-peer streaming of video from home surveillance cameras.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/deploying-smart-cameras-using-amazon-kinesis-video-streams-with-webrtc.pdf)Step 1The camera authenticates to AWS IoT Core using the Credentials Provider.Step 2The Amazon Kinesis Video Streams software development kit (SDK) opens signaling to the signaling channel, awaiting viewer requests.Step 3Amazon CloudFront is the content delivery network (CDN) for the static single-page application (SPA) hosted in Amazon Simple Storage Service (Amazon S3).Step 4The camera owner logs in to the mobile client. Amazon Cognito and Amazon API Gateway manage user access for the mobile client.Step 5The mobile client calls an API to look up the cameras belonging to the owner. The owner then selects a specific camera to initiate real-time video streaming.Step 6The mobile client initiates a connection to the Kinesis Video Streams signaling channel, a WebSocket connection that the camera is listening to for viewer connection requests. The viewer and the camera negotiate connection details by sending messages to each other over the signaling channel.Step 7The mobile client and the camera establish a peer-to-peer connection. The Kinesis Video Streams client streams video data through the WebRTC peer connection, and the camera owner views the video stream in the mobile client. Optionally, the WebRTC data channel can be utilized for bi-directional command and control messages. If a direct, peer-to-peer connection cannot be established, video data can be relayed through the Kinesis Video Streams Traversal Using Relays around NAT (TURN) server.### Smart Home Surveillance Camera

This architecture diagram shows how to stream video from smart home cameras to Kinesis Video Streams for storage, playback, and analytics. It also shows how to send push notifications to mobile application users to notify them of events.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/deploying-smart-cameras-using-amazon-kinesis-video-streams-with-webrtc.pdf#page=2)Step 1The camera detects an event and begins recording video and audio using local storage.Step 2The camera application publishes an event to AWS IoT Core. A rule is configured in Rules for IoT Core with an action to publish an Amazon Simple Notification Service (Amazon SNS) message, triggering a push notification to the end user's mobile application. An AWS Lambda function subscribes to the Amazon SNS topic to save events in an Amazon DynamoDB table.Step 3The Kinesis Video Streams Producer SDK uses the X.509 certificate to authenticate to AWS IoT Core using the credentials provider. It then streams media to a stream belonging to the camera for storage, playback, and analytics.Step 4Kinesis Video Streams is configured with the Amazon S3 delivery feature to automatically extract still images from the uploaded media to deliver to an Amazon S3 bucket of your choice. An Amazon S3 trigger is configured to invoke a Lambda function, which will invoke an Amazon Rekognition image to perform object detection and trigger notifications in Amazon SNS.Step 5The camera owner logs in to the mobile client. Amazon Cognito and API Gateway manage user access for the mobile client.Step 6The mobile client application invokes an API to retrieve a list of cameras and view a list of events. The events list view uses the images stored in Amazon S3 as preview thumbnails for viewing the stored media.Step 7The mobile application user selects an event to replay and uses Kinesis Video Streams playback to replay the stored video and audio.## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses Kinesis Video Streams and AWS IoT Core, which allow users to identify ways of optimizing the location event ingestion workflow and ensure the workflow can scale in the event of a large influx of new events. For instance, Kinesis Video Streams sends metrics to Amazon CloudWatch, giving users visibility into video streaming data. In addition, AWS IoT Core sends metrics to CloudWatch to monitor incoming messages and alerts when ingestion stops or slows, indicating possible network or other issues. AWS IoT Core also provides fleet management capabilities to give operators insights into connected camera status. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM) policies scope permissions for the required AWS services to the minimum level. Kinesis Video Streams allows scoping permissions to authorized users and devices; it also protects data at rest with AWS Key Management Service (AWS KMS) and in transit with TLS. Moreover, AWS IoT Core policies control device access to MQTT topics and cloud interactions. Finally, Amazon Cognito provides authentication and authorization controls for mobile applications. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Serverless services designed across multiple Availability Zones (AZs) provide resilience against a number of failures. Specifically, it helps to ensure data ingestion into AWS IoT Core, processing by Lambda, and storage in Amazon S3, which offers versioning, object lock, and lifecycle configuration for reliability. DynamoDB provides features like on-demand backup, point-in-time recovery, and global tables for data sync. Also, Kinesis Video Streams is built on AWS Regions and AZs, which offer low-latency, high-throughput, and highly redundant networking. This allows applications and databases to automatically failover between AZs with higher availability, fault tolerance, and scalability than traditional data centers. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

AWS IoT Core scales to accommodate increasing message ingestion while offering low latency. Lambda enables the configuration of concurrency reservations to reduce cold start times and enhance performance. And Kinesis Video Streams automatically provisions and scales all the necessary infrastructure to ingest streaming video data from millions of devices. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Kinesis Video Streams for WebRTC reduces the need for cloud-based video streaming through peer-to-peer connectivity while providing pay-as-you-go TURN service pricing when cloud streaming is required. AWS IoT Core scales pricing with usage, enabling ongoing cost optimization by identifying goals, measuring metrics, and making incremental improvements, aided by cost tagging and billing groups. Cloud storage with Amazon S3 enables agility and cost savings through unlimited scale, storage class selection, and features like the Amazon S3 Intelligent-Tiering storage class. Similarly, DynamoDB offers cost optimization through capacity modes, table classes, and cost allocation tags. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The majority of services comprising this Guidance are constructed using serverless technologies, thereby reducing the required compute footprint. For instance, Lambda will only execute when invoked by AWS IoT Core, and Amazon S3 can use more energy-efficient storage volumes for long-term media storage, such as thumbnail preview images. By building upon serverless services, the overall compute usage can be diminished, enabling the construction of a fully event-driven architecture that scales up and down with traffic demands, consuming less energy during periods of lower ingestion. Furthermore, employing Kinesis Video Streams eliminates the need to maintain steady-state applications running on instances, instead automatically provisioning and elastically scaling all the infrastructure required to ingest streaming video data from millions of devices. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
