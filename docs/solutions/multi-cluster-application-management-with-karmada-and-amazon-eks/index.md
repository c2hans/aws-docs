---
source_url: https://docs.aws.amazon.com/solutions/multi-cluster-application-management-with-karmada-and-amazon-eks/index.html
---

---
title: 'Guidance for Multi-Cluster Application Management with Karmada and Amazon EKS'
canonical_url: https://docs.aws.amazon.com/solutions/multi-cluster-application-management-with-karmada-and-amazon-eks/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Multi-Cluster Application Management with Karmada and Amazon EKS

Centralized Kubernetes multi-cluster management and deployment

## Overview

This Guidance shows how to use Karmada with Amazon Elastic Kubernetes Service (Amazon EKS) to manage and run your cloud-native applications across multiple Kubernetes clusters on AWS. Karmada provides ready-to-deploy automation for multi-cluster application management, offering features like centralized multi-cloud management, high availability, failure recovery, and traffic scheduling. You can centrally manage and control multiple Kubernetes clusters through a single entry point without modifying your applications. This Guidance is compatible with the Kubernetes API, allowing seamless integration with the existing Kubernetes suite of built-in policy sets to address a variety of deployment scenarios. These include policies for active-active configurations, remote disaster recovery, and geo-redundancy—allowing you to manage applications across multiple clusters with high availability and resilience.

## How it works

### Karmada Control Plane

This architecture diagram shows how to deploy a Karmada Control Plane on an Amazon EKS parent cluster.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/multi-cluster-application-management-with-karmada-and-amazon-eks.pdf#page=1)Step 1The user interacts with the Aggregated Kubernetes API Endpoint (part of the Karmada Control Plane) using kubectl, a Kubernetes command line interface (CLI) tool, and a Network Load Balancer as the endpoint.Step 2The Network Load Balancer provides SSL termination and acts as a proxy for Karmada services running on the Amazon Elastic Kubernetes Service (Amazon EKS) parent cluster.Step 3The Karmada Control Plane exposes the Karmada API through its API server. In addition, it exposes the Kubernetes API, which receives calls for Kubernetes and Karmada management tasks.Step 4Karmada runs several components on the Amazon EKS compute nodes. To keep records of API objects and states, the Karmada API server uses its own etcd database deployment.Step 5The Karmada etcd database uses Amazon EBS volumes attached to the Amazon EKS compute node and Amazon Elastic Compute Cloud (Amazon EC2) instances to maintain its state and consistency. All cluster state changes and updates are stored in persistent Amazon Elastic Block Store (Amazon EBS) volumes across all Amazon EC2 compute nodes that host etcd pods.### Application deployment to Karmada-managed EKS clusters

This diagram shows how to deploy applications to Karmada-managed Amazon EKS clusters.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/multi-cluster-application-management-with-karmada-and-amazon-eks.pdf#page=2)Step 1The user interacts with the Karmada API server (part of the Karmada Amazon EKS Control Plane) using the kubectl CLI with the Karmada Installation of CLI Tools. The user sends commands directed at multiple clusters. For example, deploying an NGINX application with an equal load across two Amazon EKS clusters in different Regions.Step 2The Karmada Amazon EKS Control Plane maintains the status and state of all Amazon EKS cluster members. Upon receiving the user request, it interprets the requirements and instructs member clusters accordingly. For example, it will deploy and run an NGINX deployment in each member cluster.Step 3The Karmada Amazon EKS cluster Member 1 receives instructions from the Karmada Control Plane to deploy and run an NGINX container application.Step 4The Karmada Amazon EKS cluster Member 2 receives instructions from the Karmada Control Plane to deploy and run an NGINX container application.Step 5The Karmada Amazon EKS Control Plane (parent cluster) checks the application's deployment status on Member Clusters 1 and 2 and updates the state in its etcd database.Step 6The user validates the status of the multi-cluster application deployment communicating with the Karmada Amazon EKS Control Plane through the Karmada CLI commands `kubectl.`## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Access a guide with detailed deployment instructions

[Open guide](https://aws-solutions-library-samples.github.io/compute/multi-cluster-application-management-with-karmada-and-amazon-eks.html)

- **Let's make it happen**: Use sample code to deploy this Guidance in your AWS account

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-multi-cluster-application-management-with-karmada-and-amazon-eks)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon EKS provides dynamic scaling of compute nodes across Availability Zones, enabling reliable and consistent Kubernetes cluster deployment, management, and upgrades using Infrastructure as Code (IaC). It also integrates with Amazon CloudWatch Container Insights for monitoring. Additionally, Karmada simplifies multi-cluster and multi-cloud Kubernetes management from a centralized portal, reducing operational overhead by applying policies and configurations uniformly across clusters for consistent application deployment and networking. Karmada also supports hybrid deployments across AWS accounts, allowing you to choose the most suitable infrastructure. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM) allows for the creation of policies with granular controls to specify the permitted and denied actions. The utilization of IAM policies facilitates adherence to the "principle of least privilege" with regards to resource access. Furthermore, IAM integrates with AWS CloudTrail to provide comprehensive logging of user activity, thereby enhancing auditing capabilities and visibility into actions performed. Additionally, Amazon EKS integrates with Amazon Virtual Private Cloud (Amazon VPC) to establish logical network isolation between the Kubernetes nodes. This network-level isolation, combined with granular access controls, serves to enhance the overall security posture of the Amazon EKS environment, which is built upon the open-source Kubernetes API. Together, they incorporate industry-standard security and encryption practices for both the platform and application layers. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance supports a highly available topology in a number of ways. One, Amazon EKS deploys Kubernetes control and compute planes across multiple Availability Zones to provide high availability. Two, Amazon EKS uses Elastic Load Balancing (ELB) that routes application traffic to healthy nodes. Three, Amazon EKS sends cluster metrics to CloudWatch, enabling custom alerts based on thresholds. Four, Kubernetes has built-in high availability features, including a distributed etcd database and the ability to run the Control Plane on multiple servers across Availability Zones. Lastly, Karmada enhances reliability through cross-cluster load balancing and auto-scaling, dynamically scheduling workloads based on utilization. Karmada itself is designed for high availability with multi-master clustering and redundancy. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon EKS supports auto-scaling of compute nodes, which matches capacity to demand, improving performance efficiency. This includes various types of Amazon EC2 instances to better match the kind of workloads you are running. Karmada can deploy workloads closer to end-users on Amazon EKS clusters in different geographical locations, which reduces latency and improves the user experience. Integrated with Kubernetes native auto-scaling features, Karmada can help in automatically scaling applications based on the demand for efficient resource use. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon EKS charges a fixed monthly fee for the Control Plane and with it, you can use the capabilities of Kubernetes to optimize your pod resource requests and achieve lower costs. For example, Amazon EKS can automatically scale compute nodes based on workload demand to reduce over-provisioning and costs. In addition, Karmada simplifies the management and deployment of multiple Amazon EKS clusters and workloads across different clusters from a central location. This reduces the overhead costs related to the administration and management of multiple Amazon EKS clusters and their associated workloads. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon EKS is designed to run on the highly efficient AWS cloud infrastructure, which has been engineered with sustainability in mind. This includes the use of custom-designed, ARM-based Graviton processors that deliver significantly higher performance-per-watt compared to traditional x86 chips. Beyond the energy-efficient hardware, the AWS data centers hosting Amazon EKS also incorporate innovative cooling and power distribution systems to maximize efficiency. By running on this AWS foundation built for sustainability, Amazon EKS is able to provide the required compute resources for containerized applications with a smaller environmental footprint compared to on-premises deployments. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
