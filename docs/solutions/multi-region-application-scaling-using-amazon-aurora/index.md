---
source_url: https://docs.aws.amazon.com/solutions/multi-region-application-scaling-using-amazon-aurora/index.html
---

---
title: 'Guidance for Multi-Region Application Scaling Using Amazon Aurora'
canonical_url: https://docs.aws.amazon.com/solutions/multi-region-application-scaling-using-amazon-aurora/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Multi-Region Application Scaling Using Amazon Aurora

## Overview

This Guidance demonstrates how you can scale your web or mobile applications using the read local, write global approach to build a resilient, self-healing system spanning multiple AWS Regions. Within each Region, your app will automatically scale on AWS-managed compute instances to meet fluctuating demand. A proxy service maintains your database connections, splitting reads and writes to optimize performance. If a Region fails, the system can quickly shift to a backup, with event-driven automation monitoring for issues and syncing your configuration.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/multi-region-application-scaling-using-amazon-aurora.pdf)

![Architecture diagram](/images/solutions/multi-region-application-scaling-using-amazon-aurora/images/multi-region-application-scaling-using-amazon-aurora-1.png)

1. **Step 1**: Users connect to the application through AWS Global Accelerator, which sends application traffic through the AWS global network infrastructure.
1. **Step 2**: Global Accelerator routes the connection to the nearest Region's Application Load Balancer.
1. **Step 3**: The Application Load Balancer routes the connection to the application Pods on Amazon Elastic Kubernetes Service (Amazon EKS).
1. **Step 4**: Setup the PgBouncer Proxy Pods on the same Amazon EKS cluster to automatically scale using the Horizontal Pod Autoscaler.
1. **Step 5**: Maintain a pool of connections to Amazon Aurora Global Database using the PgBouncer Proxy. Divide connections into writer and reader pools. The writer pool connects to the Amazon Aurora writer node in the primary Region. The reader pool connects to the Aurora reader nodes in the same Region as Amazon EKS.
1. **Step 6**: Generate an event on an Amazon EventBridge event bus when Aurora Global Database switches over or fails over to the secondary Region.
1. **Step 7**: Run an AWS Lambda function for the Aurora Global Database switchover and failover using an event rule.
1. **Step 8**: Synchronize PgBouncer Proxy configuration for the writer node in the primary Region of Aurora Global Database using Lambda.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-multi-region-application-data-using-amazon-aurora)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Operational excellence in a multi-Region context involves ensuring that your infrastructure operates smoothly across different Regions. Amazon CloudWatch is used to monitor various aspects, including the performance of the Aurora Global Database, the Amazon EKS cluster (such as CPU and memory usage), and incoming requests routed through the Application Load Balancer. Performance insights within Aurora allow for further observation of database performance. Moreover, in configuring this approach, collaboration between Amazon EKS, Application Load Balancer, Aurora Global Database, and Global Accelerator is emphasized to isolate faults in individual partitions. This collaborative effort enhances scalability and resilience, particularly in mitigating the rare but potential occurrence of Availability Zone (AZ) or Region failures. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance utilizes various AWS services to protect resources and data. Amazon EKS employs Kubernetes Role-Based Access Control (RBAC) to manage access to cluster resources so that only authorized entities can interact with sensitive components. Network security is strengthened through the use of the AWS Transit Gateway and Global Accelerator, which provide secure communication channels between Regions and help mitigate distributed denial of service (DDoS) attacks. Aurora Global Database enhances data security with encryption at rest and in transit, safeguarding sensitive information from unauthorized access. Additionally, AWS Identity and Access Management (AWS IAM) is utilized to manage user permissions and access policies so that only authenticated and authorized users can interact with AWS resources. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance incorporates redundancy and fault tolerance across multiple layers of the architecture. Amazon EKS uses multiple AZs to distribute workloads for high availability and fault tolerance. The use of Aurora Global Database enhances database reliability by replicating data across Regions, minimizing the risk of data loss, and helping to ensure continuity of operations in the event of a Regional outage. Additionally, Global Accelerator routes traffic to healthy endpoints, automatically rerouting traffic away from unhealthy or degraded resources to maintain service availability. Automated scaling mechanisms within Amazon EKS and Application Load Balancer help manage fluctuations in workload demand so that resources are dynamically allocated to meet performance requirements without manual intervention. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses various AWS services and features to streamline resource utilization, enhance scalability, and minimize latency. Amazon EKS employs auto-scaling capabilities to dynamically adjust compute resources based on workload demands. Utilizing add-ons like Horizontal Pod Autoscaler and Karpenter, along with Application Load Balancer, supports automatic and elastic scaling of applications and worker nodes, as well as efficient traffic distribution across healthy targets. Aurora facilitates scaling database reads across Regions and positioning applications near users. Additionally, Aurora Optimized Reads for Aurora PostgreSQL offers improved query latency by up to 8x and cost savings of up to 30% compared to instances without it. Global Accelerator further enhances network performance by up to 60% by routing application traffic through the AWS global network infrastructure, simplifying the management of multi-Regional deployments with two static IPs cast from AWS globally distributed edge locations. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

In this Guidance, cost optimization is facilitated through the strategic utilization of AWS services and features, with a focus on maximizing efficiency while minimizing expenses. With Amazon EKS, Horizontal Pod Auto Scaling and Karpenter enable automatic scaling of applications and worker nodes, optimizing resource allocation to match varying demand levels. Aurora plays a pivotal role in cost optimization by offering two storage configurations tailored to specific workload requirements. The Aurora Standard configuration delivers cost-effective pricing for applications with moderate I/O usage, while the Aurora I/O-Optimized configuration provides enhanced pricing for I/O-intensive workloads, supporting optimal performance without overspending. The Aurora Autoscaling feature dynamically adjusts read replicas based on application workload fluctuations for efficient resource utilization and minimizing unnecessary expenses. Furthermore, the use of AWS Graviton Processors, specifically Graviton3 instances, on Aurora and Amazon EKS optimizes price-to-performance ratios, offering significant cost savings while maintaining high performance. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance deploys and integrates an Amazon EKS cluster and an Aurora Global Database in the AWS Cloud—there is no need to procure any physical hardware. Capacity providers keep virtual “infrastructure” provisioning to a minimum, along with the necessary auto-scaling events should the workloads demand it. Every pod running on the Kubernetes platform, including the Amazon EKS cluster and the Aurora Global Database, will consume memory, CPU, I/O, and other resources. Furthermore, by supporting the use of energy-efficient processor instance types, like AWS Graviton Processors, this Guidance provides increased sustainability. Using Graviton in Amazon EC2 and Aurora can improve the performance of workloads with fewer resources, thereby decreasing the user's overall resource footprint. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Scale applications using multi-Region Amazon EKS and Amazon Aurora Global Database: Part 1**: In Part 1, this blog post demonstrates the architecture patterns and design attributes of a multi-Region application.

[Learn more](https://aws.amazon.com/blogs/database/part-1-scale-applications-using-multi-region-amazon-eks-and-amazon-aurora-global-database/)

- **Scale applications using multi-Region Amazon EKS and Amazon Aurora Global Database: Part 2**: In Part 2, this blog post showcases how we implement a solution for a retail website using microservices run on Amazon EKS clusters in multiple Regions, and Aurora Global Database (PostgreSQL-compatible edition) for transactional data persistence and low-latency local reads.

[Learn more](https://aws.amazon.com/blogs/database/part-2-scale-applications-using-multi-region-amazon-eks-and-amazon-aurora-global-database/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
