---
source_url: https://docs.aws.amazon.com/solutions/cell-based-architecture-for-amazon-eks/index.html
---

---
title: 'Guidance for a Cell-Based Architecture for Amazon EKS'
canonical_url: https://docs.aws.amazon.com/solutions/cell-based-architecture-for-amazon-eks/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for a Cell-Based Architecture for Amazon EKS

Improve resiliency and reduce your data transfer costs between Availability Zones

## Overview

This Guidance demonstrates how to configure a cell-based architecture for Amazon Elastic Kubernetes Service (Amazon EKS). It moves away from typical multiple Availability Zone clusters to a single Availability Zone cluster. These single Availability Zone clusters are called cells, and the aggregation of these cells in each Region is called a supercell. These cells help to ensure that a failure in one cell doesn't affect the cells in another, reducing data transfer costs and improving both the availability and resiliency against Availability Zone failures for Amazon EKS workloads.

## Benefits

### Protect service reliability

Deploy independent application cells using bulkhead architecture patterns. Prevent issues in one cell from cascading across your container environment while maintaining service stability.

### Reduce data transfer costs

Keep container workload communications within Availability Zone boundaries. Eliminate inter-AZ data transfer costs for chatty microservices while maintaining high availability.

### Meet business demands efficiently

Deploy and manage containerized workloads separately within each zone. Respond to changing business needs without complex infrastructure coordination.

## How it works

### Cell-Based EKS Architecture

This architecture diagram shows how you can use a cell-based architecture to improve resiliency and reduce data transfer costs for Amazon EKS workloads. It shows what a cell consists of and how those cells are routed. For more details about supercells, open the other tab.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/a-cell-based-architecture-for-amazon-eks.pdf#page=1)Step 1A cell consists of an Amazon Elastic Kubernetes Service (Amazon EKS) cluster having its compute nodes (workloads) and dedicated Application Load Balancers(ALB) deployed within a single Availability Zone (AZ). These cells are independent replicas of the application and create a fault isolation boundary to limit the scope of impact. There can be multiple cells per AZ, and multiple cells can be deployed across multiple AZs to provide high availability and resiliency against AZ failures.Step 2Clients are routed towards Amazon EKS workloads within each cell by a cell-routing layer, which consists of Amazon Route 53 weighted routing records, and Amazon Route 53 Application Recovery Controller to provide readiness checks, routing control, and zonal shifts capability. An application load balancer balances the traffic to the Kubernetes resources within each cell.Step 3Once the request reaches a cell, all subsequent internal communications among the Kubernetes (k8s) workloads stays within the cell. This prevents cross-cell dependency, making each cell statically stable and more resilient. Additionally, with minimal inter-AZ communication, there are no inter-AZ data transfer costs for chatty workloads, as traffic never leaves the AZ boundary. Amazon EKS workloads utilize Karpenter for compute autoscaling needs.Step 4Amazon EKS workloads that require access to data persistence can continue to use other data store services managed by AWS, like Amazon Relational Database Service (Amazon RDS), Amazon DynamoDB, and Amazon ElastiCache, which span across multiple AZs for high availability.### Regional Cell Aggregation

This architecture diagram shows how multiple cells are aggregated to create a supercell. It also outlines how those supercells are routed. For more details about the main architecture, open the other tab.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/a-cell-based-architecture-for-amazon-eks.pdf#page=2)Step 1A cell consists of an Amazon Elastic Kubernetes Service (Amazon EKS) cluster having its compute nodes (workloads) and dedicated Application Load Balancers(ALB) deployed within a single Availability Zone (AZ). These cells are independent replicas of the application and create a fault isolation boundary to limit the scope of impact. There can be multiple cells per AZ, and multiple cells can be deployed across multiple AZs to provide high availability and resiliency against AZ failures.Step 2An aggregation of multiple cells within a Region is called a supercell.Step 3Amazon EKS workloads in each AWS Region, or supercell, use ELB to load balance the traffic to Amazon EKS workloads within each cell.Step 4Clients are routed to a supercell using the Route 53 weighted routing policy and also use the Route 53 Application Recovery Controller to provide routing control and zonal shift capabilities.Step 5Multiple supercells can be deployed across AWS Regions for disaster recovery, or to satisfy data residency requirements.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/compute/cell-based-architecture-for-amazon-eks.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-cell-based-architecture-for-amazon-eks)

## Related content

- **Life360’s journey to a multi-cluster Amazon EKS architecture to improve resiliency**: This blog post demonstrates how Life360 uses a multi-cluster Amazon EKS architecture to address Amazon EKS scaling and workload management, and have a statically stable resilient infrastructure for AZ wide failures.

[Learn more](https://aws.amazon.com/blogs/containers/life360s-journey-to-a-multi-cluster-amazon-eks-architecture-to-improve-resiliency/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
