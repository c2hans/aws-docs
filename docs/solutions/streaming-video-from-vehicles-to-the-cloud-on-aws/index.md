---
source_url: https://docs.aws.amazon.com/solutions/streaming-video-from-vehicles-to-the-cloud-on-aws/index.html
---

---
title: 'Guidance for Streaming Video from Vehicles to the Cloud on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/streaming-video-from-vehicles-to-the-cloud-on-aws/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Streaming Video from Vehicles to the Cloud on AWS

## Overview

This Guidance demonstrates how to use the Internet of Things (IoT) and Amazon Kinesis Video Streams with Web Real-Time Communication (WebRTC) to monitor videos from a vehicle. Original equipment manufacturers (OEMs) can give their customers the ability to monitor low-latency videos from a vehicle for security purposes, and the video can be accessed from a variety of in-vehicle platforms and viewed on any web browser. This Guidance can help OEMs increase direct revenue and improve engagement with OEM applications and web services.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/streaming-video-from-vehicles-to-the-cloud-on-aws.pdf)

![Architecture diagram](/images/solutions/streaming-video-from-vehicles-to-the-cloud-on-aws/images/streaming-video-from-vehicles-to-the-cloud-on-aws-1.png)

1. **Step 1**: The vehicle authenticates to AWS IoT Core using the credentials provider service.
1. **Step 2**: The Amazon Kinesis Video Streams client connects to the signaling channel, awaiting viewer requests.
1. **Step 3**: Amazon CloudFront is the content delivery network (CDN) for the static single-page application (SPA) hosted in Amazon Simple Storage Service (Amazon S3).
1. **Step 4**: The vehicle owner logs into the mobile client. Amazon Cognito and Amazon API Gateway manage user access for the mobile client.
1. **Step 5**: The mobile client calls an API to look up the vehicles that belong to the owner. The owner then selects a specific vehicle to initiate real-time video streaming.
1. **Step 6**: The mobile client initiates a connection to the Kinesis Video Streams signaling channel, a websocket connection that the vehicle is listening to for viewer connection requests. The viewer and the vehicle negotiate connection details by sending messages to each other over the signaling channel.
1. **Step 7**: The mobile client and the vehicle establish a peer-to-peer connection. The Kinesis Video Streams client streams video data through the WebRTC peer connection, and the vehicle owner views the video stream in the mobile client. Optionally, the WebRTC data channel can be utilized for bi-directional command and control messages. If a direct, peer-to-peer connection cannot be established, video data can be relayed through the Kinesis Video Streams Traversal Using Relays around NAT (TURN) server.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

WebRTC session count and minutes are counted and logged through the KVS WebRTC service. Each channel is set up on demand, so it can readily match to users. This allows for analysis of overall fleet and individual usage. Visibility into this usage can support billing or credit limits. Sessions can also be anonymized or tokenized to prevent matching to users if required by local regulation. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

CloudFront secures web application delivery by HTTPS. Amazon Cognito handles user authorization, and an Amazon Cognito token secures access to API Gateway. This architecture secures IoT device access by X.509 certification over mutual transport layer security (mTLS). These devices are granted temporary credentials to access KVS only when there is user demand. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

All cloud resources are serverless and scale with demand, helping prevent system downtime even if demand increases. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses serverless systems to allow for both scalability and minimum configuration and maintenance. AWS IoT Core is purpose-built to manage permissions and configuration of a large fleet of devices, such as vehicles. KVS is built to facilitate peer-to-peer WebRTC with common signaling and support services (such as a TURN server), without infrastructure provisioning or additional configuration. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

To help minimize data transfer charges, data transferred in and out of the AWS Region is limited to the owner by using CloudFront to distribute an active application and API Gateway for queries. Data transferred to and from the vehicle is limited to small JSON messages with changes in shadow state and temporary credentials. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The services in this Guidance are serverless and scale with demand, so you do not need to provision and maintain “standing” infrastructure. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **AWS IoT Greengrass V2 Component to send video over Kinesis Video Streams with WebRTC**: This sample code demonstrates how to create an AWS IoT Greengrass V2 Component to send video over Kinesis Video Streams with WebRTC.

[Learn more](https://github.com/awslabs/aws-iot-greengrass-component-kvs-webrtc)

- **Designing Next Generation Vehicle Communication with AWS IoT Core and MQTT**: This whitepaper demonstrates the best practices for implementing an extensible, scalable and resilient communication architecture for the next generation of vehicles on AWS.

[Learn more](/whitepapers/latest/designing-next-generation-vehicle-communication-aws-iot/designing-next-generation-vehicle-communication-aws-iot.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
