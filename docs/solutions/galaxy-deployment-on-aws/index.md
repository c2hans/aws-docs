---
source_url: https://docs.aws.amazon.com/solutions/galaxy-deployment-on-aws/index.html
---

---
title: 'Guidance for Galaxy Deployment on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/galaxy-deployment-on-aws/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Galaxy Deployment on AWS

## Overview

This Guidance shows how you can run Galaxy software on AWS, allowing you to benefit from the ease-of-use of the Galaxy platform while using purpose-built services from AWS for the needed undifferentiated heavy-lifting, without compromising your security or data integrity. Galaxy is an open-source web application where you can run data intensive jobs for biomedical research through a graphical web interface. With the AWS native services for data storage and compute, this Guidance shows how you can optimize the end-to-end platform of Galaxy when uploading, managing, and analyzing large datasets.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/galaxy-deployment-on-aws.pdf)

![Architecture diagram](/images/solutions/galaxy-deployment-on-aws/images/galaxy-deployment-on-aws-1.png)

1. **Step 1**: Galaxy users access the Galaxy Web application by the public endpoint of the Application Load Balancer.
1. **Step 2**: Galaxy stores user metadata and history in the PostgreSQL database hosted in Amazon Aurora Serverless, and Galaxy users have access through the Galaxy Web server. The credentials for this access are stored in AWS Secrets Manager.
1. **Step 3**: The Galaxy Data volume stores user data, including input data for processing and processed data. Amazon Elastic File System (Amazon EFS) provides the storage capacity.
1. **Step 4**: Galaxy leverages a message queue for communication between internal processes. This Guidance hosts the message queue on Amazon MQ with the RabbitMQ message broker. Credentials for the broker are stored in Secrets Manager.
1. **Step 5**: Users can review, schedule, and manage bioinformatics jobs in the Galaxy Jobs pod through the Galaxy Web server.
1. **Step 6**: AWS Backup takes regular backups of Amazon EFS file systems and PostgreSQL databases.
1. **Step 7**: The monitoring and log collection of both the Galaxy components and the AWS infrastructure are centralized in Amazon CloudWatch.
1. **Step 8**: Amazon Elastic Kubernetes Service (Amazon EKS) provides the control plane, manages both the networking and the nodes for the Kubernetes pods, and horizontally scales by adding or removing nodes. Additional pods are deployed through Amazon EKS to synchronize secrets with Secrets Manager and to publish logs to CloudWatch.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-galaxy-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses services that allow you full visibility into your workloads through monitoring and logging, while also providing you with reliable, stable, and dependable applications. For example, with CloudWatch, you gain observability with metrics, personalized dashboards, and logs, in addition to alerts that are defined from metrics throughout this Guidance, so you can monitor the health of your workloads and minimize the impact from incidents. Also, Amazon EKS clusters can identify unhealthy containers and replace them automatically with new containers, so that your workloads are available to respond to incidents and events. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

By default, all incoming connections to Galaxy originate from the public Internet and are directed to the Galaxy server through a publicly accessible Application Load Balancer. Alternatively, this Guidance can be configured to use an internal Application Load Balancer in a private subnet, where traffic is routed through a virtual private network (VPN) connection or through AWS Direct Connect. In both cases, compute resources are deployed within private subnets and are not directly accessible from the public Internet. Galaxy handles application-level authentication and authorization through its own user management or through Active Directory Federation Service (AD FS). [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

To implement a reliable application-level architecture, the individual components of this Guidance are deployed as loosely coupled Kubernetes pods. Also, the message broker is the fully managed service Amazon MQ, which, in our default configuration, includes a standby server. Finally, the shared filesystem is provided through Amazon EFS and is highly available, as is the database provided through Aurora Serverless. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon EKS is an AWS native service, and this Guidance focuses on cost-efficient ways to deploy and configure it with selected resources so that you can achieve a reliable Kubernetes application with high availability and low operational costs. The architecture for Amazon EKS is spanned across multiple Availability Zones for high availability. While some traffic will exist between subnets deployed into Availability Zones, its latency should not make any significant performance impact. Amazon EFS is designed to provide serverless, fully elastic file storage that allows you to share file data without the need to provision or manage storage capacity and performance. It provides a Portable Operating System Interface (POSIX) file system with the necessary performance for bioinformatic workloads. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

A significant factor for data transfer costs within Amazon EKS clusters are calls to Kubernetes services from external clients going through Application Load Balancers. The data transfer costs when calling services are mapped to communications between pods running in different Availability Zones. Due to the highly configurable autoscaling minimum, maximum, and desired number of compute nodes, along with their corresponding Amazon Elastic Compute Cloud (Amazon EC2) parameters, resources are efficiently managed. Finally, serverless architectures have a pay-per-value pricing model and scale based on demand. This includes the Aurora Serverless database and Amazon EFS. We recommend you tag AWS resources that belong to a project programmatically, and then create custom reports in AWS Cost Explorer using the tags to visualize and monitor costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

By choosing the right sized instances, you use only the resources you need, thereby reducing unnecessary emissions. Also, by using services with dynamic scaling, you minimize the environmental impact of the backend services, and ensure scaling of compute resources based on your website needs. Additionally, the use of fully managed services, such as Amazon EFS, minimizes the required resources. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
