---
source_url: https://docs.aws.amazon.com/solutions/deploying-rancher-rke2-at-the-edge-on-aws/index.html
---

---
title: 'Guidance for Deploying Rancher RKE2 at the Edge on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/deploying-rancher-rke2-at-the-edge-on-aws/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Deploying Rancher RKE2 at the Edge on AWS

## Overview

This Guidance demonstrates how to deploy Rancher Kubernetes Engine (RKE2) at the edge with AWS services, enabling organizations to run mission-critical workloads in tactical edge environments with Denied, Disruptive, Intermittent, and Limited (DDIL) communication. It showcases an edge-to-cloud pattern for collecting and forwarding sensor data from the field to the cloud. This helps organizations overcome the challenges of deploying and managing mission-critical applications in environments with limited or intermittent connectivity.

## How it works

### Single-node cluster

This architecture diagram shows an edge and cloud pattern to deploy containerized workloads on a single node cluster at the edge using RKE2 on any third party hardware in DDIL environments.

[Download the architecture diagram PDF](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/deploying-rancher-rke2-at-the-edge-on-aws.pdf#page=1)Step 1Rancher Multi-Cluster Manager (MCM) is deployed in AWS GovCloud (US) on an RKE2 cluster. RKE2 cluster will be deployed on Amazon Elastic Compute Cloud (Amazon EC2) instances running Suse Enterprise Linux Server (SLES) AMI hardened to Defense Information Systems Agency (DISA) Security Technical Implementation Guide (STIG) security standards.Step 2Rancher MCM provides centralized administration for downstream RKE2 clusters on one or more edge devices through Elastic Load Balancing (ELB).Step 3Elemental is an MCM extension which provides a full cloud-native OS management for edge devices. An endpoint is registered in Elemental, which creates a seed image and an initial registration config that contains a registration URL.Step 4Elemental-built Suse Linux Enterprise Micro (SLE Micro) is installed along with the initial registration config on the edge device through a USB.Step 5The device registers to Elemental in Rancher MCM.Step 6Fleet Manager is a DevOps engine that polls container registries and Git repositories for declarative changes to infrastructure and applications.Step 7Fleet Manager first deploys an RKE2 cluster or K3s in addition to Harbor registry at the edge. K3s is recommended for light-weight workloads while RKE2 is recommended for larger complex workloads.Step 8Fleet Manager then orchestrates replication of contents from Amazon Elastic Container Registry (Amazon ECR) to Harbor registry.Step 9Once RKE2 or K3s is available, Fleet Manager deploys mission workloads on the edge, pulling images from Harbor registry. Fleet Manager provides centralized deployment of initial workloads and Day 2 operations.Step 10Operators interact with mission applications through exposed mission web applications.Step 11Mission applications receive sensor data from the field.Step 12An AWS IoT Greengrass client running on Elemental can also receive sensor data.Step 13An AWS IoT Greengrass client forwards data to AWS IoT Core on the cloud.Step 14Mission workloads connect with upstream AWS services such as Amazon Simple Storage Service (Amazon S3) to transfer data from edge to the cloud.Step 15AWS Distro for Open Telemetry processes telemetry data at the edge and forwards this data to Amazon CloudWatch for performance monitoring of edge device and mission applications.### Multi-node cluster

This architecture diagram shows two distinct edge-to-cloud patterns for managing applications in tactical edge scenarios, illustrating how mission-critical workloads can be deployed on RKE2 in DDIL environments.

[Download the architecture diagram PDF](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/deploying-rancher-rke2-at-the-edge-on-aws.pdf#page=2)Step 1Rancher MCM is deployed in AWS GovCloud (US) on an RKE2 cluster. RKE2 cluster will be deployed on Amazon EC2 instances running SLES AMI hardened to DISA STIG security standards. Alternately, MCM can be run on an Amazon Elastic Kubernetes Service (Amazon EKS) cluster.Step 2Harvester, which provides Hyper Converged Infrastructure (HCI) and automation capabilities, is installed on the edge device through a USB or Preboot eXecution Environment (PXE) boot.Step 3Harvester registers device to Rancher MCM in AWS GovCloud (US).Step 4Rancher MCM provides centralized administration of downstream Harvester and RKE2 cluster deployments on one or more edge devices.Step 5Fleet Manager is a DevOps engine that polls container registries and Git repositories for declarative changes to infrastructure and applications. Fleet Manager provides centralized deployment of initial workloads and Day 2 operations. Fleet Manager first deploys Harbor Registry at the edge.Step 6Harbor registry at the edge replicates contents from Amazon ECR.Step 7Fleet Manager deploys Suse Linux virtual machines (VMs), RKE2 cluster and/or K3s on Suse Linux VMs and mission workloads on the edge, pulling images from Harbor Registry. K3s is recommended for lightweight workloads while RKE2 is recommended for larger complex workloads.Step 8Operators interact locally with mission web applications.Step 9Mission applications receive sensor data from the field.Step 10An AWS IoT Greengrass client running on Suse Linux VM can also receive sensor data.Step 11The AWS IoT Greengrass client forwards data to AWS IoT Core in the cloud.Step 12Mission workloads connect with upstream AWS services, such as Amazon S3 to transfer data from edge to the cloud.Step 13Distro for Open Telemetry processes telemetry data at the edge and forwards this data to CloudWatch for performance monitoring of edge device and mission applications.## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

For consistent and continuous deployment of edge applications through a continuous DevOps pipeline, leverage Rancher's MCM and Rancher Fleet to automate the deployment and updating of RKE2 container workloads at the edge. Gain visibility into the performance and status of your edge components by integrating Distro for Open Telemetry and CloudWatch, providing you with key insights to optimize your edge operations. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Secure your edge infrastructure by using Session Manager, a capability of AWS Systems Manager, to establish safe connections to your EC2 instances running Rancher MCM. AWS Identity and Access Management (IAM) roles and policies control access, and IAM instance roles enable your EC2 instances to interact with other AWS services. Enhance image security by leveraging Harbor registry to scan for vulnerabilities, ensuring your container images are secure. Protect your environment from distributed denial of service (DDoS) attacks with AWS Shield Standard, and enforce code compliance through the use of Harbor registry. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon EC2 Auto Scaling helps ensure your edge applications are highly available and resilient by maintaining necessary capacity. ELB distributes traffic across multiple EC2 instances in different Availability Zones. Leverage multi-AZ and multi-Region configurations to enhance the reliability of your edge solution, providing you with a robust and fault-tolerant architecture. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Monitor the performance of your edge solution using CloudWatch metrics, and leverage Amazon EC2 Auto Scaling to optimize resource utilization. By analyzing performance data to identify and address any bottlenecks, you can ensure your edge applications and Rancher MCMoperate efficiently. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon EC2 Auto Scaling automatically adjusts your capacity based on demand, expanding during peak periods and scaling down during slower times. AWS Trusted Advisor receives recommendations on cost optimization opportunities, while the open-source Harbor registry eliminates the need for purchasing commercial licenses. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Reduce your environmental impact by leveraging the wide variety of EC2 instance types to choose the right-sized resources for your workloads. Combine this with Amazon EC2 Auto Scaling to automatically scale resources up and down, minimizing unused capacity and lowering your carbon footprint. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
