---
source_url: https://docs.aws.amazon.com/solutions/mhp-fleetexecuter-on-aws/index.html
---

---
title: 'Guidance for MHP FleetExecuter on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/mhp-fleetexecuter-on-aws/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for MHP FleetExecuter on AWS

## Overview

This Guidance demonstrates how to optimize manufacturing and logistics material movement using MHP FleetExecuter on AWS, a software-based fleet management solution that optimizes intralogistics operations. By seamlessly integrating and controlling manufacturer-independent Automated Guided Vehicles (AGVs), Autonomous Mobile Robots (AMRs), and driverless transport systems (DTS), the solution helps manufacturers and logistic companies streamline their transport processes while maintaining vendor flexibility. Through the unique combination of artificial intelligence, cloud integration, and modularity, it enables real-time coordination of complex infrastructure components and diverse robotic fleets. This modular approach helps organizations enhance automation efficiency, reduce operational complexity, and achieve sustainable intralogistics management through intelligent optimization and comprehensive fleet control capabilities.

## Benefits

### Unified Multi-Robot Fleet Control

Control all AGVs, AMRs, and mobile robots, from transporting to cleaning to manufacturing robots, with one software platform on AWS. FleetExecuter supports both VDA5050 and proprietary standards and is open for further standardization including Mass Robotics and ISO, enabling integration with any robot manufacturer while providing complete fleet control and eliminating vendor lock-in across your operations.

### Enterprise-Grade System Integration

Seamlessly integrate MHP FleetExecuter running on AWS with your existing ERP, Warehouse Management, and Manufacturing Execution systems. Leverage MHP's extensive experience in  connecting shopfloor fleet operations to top-floor enterprise systems across various industries, enabling real-time transport  order creation and status updates between your fleet and the enterprise systems

### Data-Driven Fleet Optimization

Leverage comprehensive data analytics from day one of MHPFleetExecuter deployment on AWS to optimize yourmobile robot and AGV fleet performance. Access real-time heatmap visualization and error clustering analysis stored in Amazon Aurora PostgreSQL to identify operational patterns, reduce downtime, and continuously improve fleet efficiency while maximizing asset utilization.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/mhp-fleetexecuter-on-aws.pdf)

![Architecture diagram](/images/solutions/mhp-fleetexecuter-on-aws/images/mhp-fleetexecuter-on-aws-1.png)

1. **Step 1**: MHP FleetExecuter's main logic runs in containers on Amazon Elastic Kubernetes Service (Amazon EKS) across two Availability Zones (AZ). Amazon Aurora (PostgreSQL) stores application data with replicas. Amazon Elastic File Service (Amazon EFS) provides StatefulSet storage with mount targets in both AZs. NAT Gateways enable internet access, and Amazon Route 53 handles the DNS.
1. **Step 2**: Operators access the FleetExecuter Service through the web browser, routed via Amazon Route 53 to the internet-facing Application Load Balancer (ALB), then to Amazon EKS services.
1. **Step 3**: AGVs and AMRs from different vendors communicate with FleetExecuter via AWS IoT Core using MQTT. An IoT gateway manages shopfloor equipment and communicates with AWS IoT Core via MQTT. Alternatively, customers can host the MQTT broker within the Amazon EKS cluster.
1. **Step 4**: Customers integrate their Enterprise Resource Planning (ERP) systems with FleetExecuter through AWS PrivateLink. ERP systems in separate VPCs connect securely via an internal Network Load Balancer (NLB) routing to Amazon EKS. The ERP system creates transport orders and receives real-time status updates.
1. **Step 5**: Amazon Elastic Container Registry (Amazon ECR) stores MHP FleetExecuter Service container images and supporting services. Amazon EKS worker nodes pull images from Amazon ECR during deployments.
1. **Step 6**: A bastion host running in an Amazon Elastic Compute Cloud (Amazon EC2) instance in a separate AZ enables administrative access to Amazon EKS, Amazon Aurora database, and Amazon EFS via AWS Systems Manager.
[Read usage guidelines](/solutions/guidance-disclaimers/)
