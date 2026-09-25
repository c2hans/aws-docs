---
source_url: https://docs.aws.amazon.com/solutions/tactical-edge-application-deployment-on-aws/index.html
---

---
title: 'Guidance for Tactical Edge Application Deployment on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/tactical-edge-application-deployment-on-aws/
source: aws-documentation
generated_on: 2026-09-25
---

# Guidance for Tactical Edge Application Deployment on AWS

## Overview

This Guidance shows two architectural patterns for deploying applications in tactical edge environments on AWS using third-party hardware devices and platforms. The term "edge" refers to compute, network, and storage capabilities that operate outside AWS Regions, often in scenarios where communication with the cloud may be limited by low bandwidth, intermittent connectivity, or extended periods of disconnection. In addition to establishing a foundational tactical edge architecture, this Guidance offers deployment patterns that use both native AWS Internet of Things (IoT) services and Kubernetes, an open-source container orchestration system. AWS customers can use this to reliably deploy mission-critical applications in tactical edge environments with limited or intermittent network connectivity like mobile command centers, tactical vehicles, and operating bases.

## How it works

### Deploy applications onto third-party hardware

This architecture extends the deployment onto third-party hardware to a single-node Kubernetes cluster on the third-party hardware.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/tactical-edge-application-deployment-on-aws.pdf?target=_blank)Step 1AWS IoT Greengrass core software runs on compatible edge hardware devices and operating systems.Step 2AWS IoT Core and AWS IoT Greengrass cloud services establish secure connections from edge devices to AWS using TLS and X.509 certificates, and orchestrate over-the-air (OTA) deployments.Step 3The AWS-provided components are used to manage edge applications. This includes a local MQTT 5 broker, stream manager for data streaming, secret manager, and AWS Systems Manager for managing local secrets, patching, and SSH tunnels. It also includes a shadow manager for managing device and application state.Step 4The mission application DevOps pipeline integrates with the cloud-to-edge deployment capabilities of IoT Core and IoT Greengrass, utilizing the AWS Cloud Development Kit (AWS CDK) and/or the IoT Greengrass Development Kit Command-Line Interface (GDK CLI) to configure and trigger IoT Greengrass deployments.Step 5The edge application artifacts are built and staged in Amazon Simple Storage Service (Amazon S3) and/or a container registry. These artifacts are then deployed as IoT Greengrass components to the edge device through IoT Greengrass deployments.Step 6Mission-specific IoT Greengrass components and containers are used to execute the applications and machine learning (ML) models deployed from the mission application pipeline.Step 7The mission applications communicatie with vehicles, sensors, and other fixed assets that are connected to the third-party hardware in the field. This communication can occur through either mission wireless networks or hardwired links to the connected assets.Step 8Network connectivity is used for the initial deployment and edge-to-cloud data capture, if available during mission operations. However, the edge applications are designed to continue running even if the network is disrupted or becomes unavailable.Step 9Operators interact with mission applications and the underlying system resources. Components can be deployed locally, if needed, through the IoT Greengrass CLI.Step 10Data and analytics pipelines are utilized to process and store the mission data in the cloud. Furthermore, machine learning models can be trained on this data using Amazon SageMaker, and then staged for deployment through the mission application pipeline.### Kubernetes-based deployment

This architecture extends the deployment onto third-party hardware to a single-node Kubernetes cluster on the third-party hardware.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/tactical-edge-application-deployment-on-aws.pdf#page=3?target=_blank)Step 1IoT Greengrass core software runs on compatible edge hardware devices and operating systems.Step 2IoT Core and IoT Greengrass cloud services establish secure connections from edge devices to AWS using TLS and X.509 certificates, and orchestrate over-the-air (OTA) deployments.Step 3Non-containerized mission specific applications and ML models are deployed to the edge device as IoT Greengrass components.Step 4The AWS-provided components are used to manage edge applications. This includes a local MQTT 5 broker, a stream manager for data streaming, a secret manager and Systems Manager for managing local secrets, patching, and SSH tunnels.Step 5Custom Kubernetes components are responsible for configuring a single-node Kubernetes cluster on the edge device, and subsequently deploying containers to the cluster.Step 6The Kubernetes cluster runs adjacent to the IoT Greengrass software on the operating system of the edge device. This Kubernetes cluster is responsible for running the mission containers, which are either deployed by the custom Kubernetes IoT Greengrass components or containers run by local operators.Step 7The mission containers are built and staged in either a cloud-based container registry or Amazon S3. These containers are then deployed to the edge device through the custom Kubernetes components using IoT Greengrass deployments.Step 8A local container registry can be deployed and configured by the Kubernetes components. The Kubernetes components can stage container images to the registry from the cloud as part of IoT Greengrass deployments.## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The IoT Greengrass, IoT Core, Systems Manager, and Amazon CloudWatch services facilitate the secure provisioning and onboarding of edge devices, as well as the deployment of edge applications. This is achieved through the over-the-air deployment capabilities provided by IoT Core and IoT Greengrass. Furthermore, these services enable proactive monitoring of edge device health and operational status using the monitoring and logging capabilities of IoT Greengrass and CloudWatch. Additionally, they enforce consistent configurations across the edge fleet with IoT Core groups, IoT Greengrass deployments, and Systems Manager for operating system and package management. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance uses unique X.509 certificates for secure device authentication and TLS-encrypted communication. Device permissions are scoped using the device’s IoT policies and AWS Identity and Access Management (IAM) roles. Certificates and keys are stored in secure hardware like hardware security modules (HSMs) and trusted platform modules (TPMs). Secrets Manager and IoT Greengrass secrets manager facilitate secure synchronization of credentials between the cloud and the edge. These services provide the foundational security capabilities for data protection and access control in the two architecture patterns. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The IoT Greengrass service enables disconnected application management, facilitating offline operation and data processing to help ensure mission-critical capabilities remain functional even in disconnected environments. When the edge devices are connected to the cloud, they can receive regular software updates and patches using the capabilities of Systems Manager and the over-the-air deployment features of IoT Greengrass. This helps address vulnerabilities and maintain the overall system reliability. Furthermore, the IoT Greengrass service is designed to operate in environments where network connections may be intermittent or disconnected for extended periods of time or indefinitely. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses IoT Greengrass to deploy edge applications that process data closer to the source, reducing latency and bandwidth requirements. AWS customers can deploy edge applications like ML and video analytics to filter, preprocess, and act on data at the edge, minimizing raw data transfer to the cloud. This Guidance also optimizes resource utilization by allowing AWS customers to tailor hardware and edge deployments according to their mission’s needs. It implements caching and buffering to enable offline operation using IoT Greengrass; it uses Systems Manager for monitoring to proactively optimize performance, enabling edge data processing without the need to transfer data back to the cloud. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

By using IoT Greengrass, AWS customers can configure edge environments tailored to their needs, optimizing resource utilization and cost-effectiveness. The flexible architecture of this offering enables deploying only the necessary components, minimizing unnecessary resource consumption. It optimizes data transfer costs by processing and analyzing data at the edge, reducing cloud transmission and using purpose-built AWS services for further storage and analysis. Additionally, IoT Greengrass enables AWS customers to right-size the edge hardware platform for their specific use case. This allows processing data locally at the edge before transferring only the necessary pre-processed data, especially over expensive network links like satellite. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance offers AWS customers to choose hardware that is optimized for their specific mission requirements so that power and cooling are tailored accordingly. Two examples of this are IoT Greengrass and containers that allow for the optimization and reduction of the software deployment footprint, minimizing unnecessary resource consumption. This Guidance also optimizes data transfer resources by processing and analyzing data at the edge, which reduces the amount of data transmitted to the cloud and consequently minimizes power consumption due to lower network bandwidth needs. These services allow AWS customers to right-size their edge application deployment and compute needs, as well as process data locally close to the source without the need to transfer raw data back to the cloud over resource-intensive data links. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
