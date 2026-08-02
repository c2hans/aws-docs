---
source_url: https://docs.aws.amazon.com/solutions/architecting-swift-connectivity-on-aws/index.html
---

# Guidance for Architecting SWIFT Connectivity on AWS

## Overview

This Guidance demonstrates how to integrate SWIFT messaging protocols and services on AWS. Central Banks can take advantage of the global reach and reliability of SWIFT, while also leveraging the scalability, security, and cost-effectiveness of AWS to facilitate the exchange of financial information and transactions between financial institutions.

## How it works

A standardized environment for connecting to the SWIFT network.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/architecting-swift-connectivity-on-aws.pdf)

![Architecture diagram](/images/solutions/architecting-swift-connectivity-on-aws/images/architecting-swift-connectivity-on-aws-1.png)

1. **Step 1**: This architecture spans two Availability Zones.
1. **Step 2**: Amazon Virtual Private Cloud (Amazon VPC) is configured with private subnets according to AWS best practices and follows the SWIFT Customer Security Programme (CSP).
1. **Step 3**: An Amazon Elastic Compute Cloud (Amazon EC2) instance runs Alliance Messaging Hub (AMH) and SWIFT Alliance Access (SAA) or Lite2.
1. **Step 4**: An Amazon EC2 instance runs SWIFT Alliance Gateway (SAG) and SWIFTNet Link (SNL).
1. **Step 5**: (Optional) An Amazon Relational Database Service (Amazon RDS) Oracle instance runs in active or standby mode to store configuration and message data for AMH.
1. **Step 6**: An Amazon MQ instance manages communication for AMH.
1. **Step 7**: AWS Systems Manager removes the need for a jump server.
1. **Step 8**: Amazon CloudWatch provides the mechanism to store, access, and monitor SWIFT activities.
1. **Step 9**: AWS Secrets Manager encrypts, stores, and retrieves passwords.
1. **Step 10**: An Amazon Virtual Private Network (VPN) gateway with Elastic Load Balancing (ELB) connects the Amazon VPC to AWS Direct Connect.*
1. **Step 11**: Direct Connect establishes private connectivity between AWS and data centers or colocation environments.*
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

To instrument this Guidance for operational excellence, CloudWatch, AWS CloudTrail, and AWS Config can be used to monitor, audit, and report on resources and applications in the AWS environment. These services provide visibility into the state and performance of the infrastructure and applications, enabling the detection and resolution of issues. Additionally, AWS X-Ray can be used to trace application requests and identify performance bottlenecks. Finally, the implementation of operational playbooks and runbooks can improve operational efficiency by codifying operational procedures and automating routine tasks. To safely operate the Guidance and respond to incidents and events, several practices are implemented. First, AWS services such as CloudWatch and AWS Config provide monitoring and logging capabilities to detect and respond to events in near real-time. Second, automated systems are used to respond to events and incidents, reducing manual intervention and minimizing the time to recover from failures. Third, testing is conducted regularly to validate the operability and resilience of the system. Finally, a well-defined incident response plan is established to provide clear guidelines on how to respond to incidents and minimize the impact of downtime. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Multi-factor authentication (MFA) and access control policies can help secure authentication and authorization. These AWS services can be integrated with this Guidance to provide additional security: AWS Identity and Access Management (IAM), AWS IAM Identity Center (Successor to AWS Single Sign-On), and AWS Directory Service. Security controls such as encryption, network security, and monitoring can help protect resources. These are supported with the following services: Amazon VPC, AWS WAF, AWS Shield, AWS Key Management Service (AWS KMS), and CloudTrail. Data encryption at rest and in transit, data classification and access control policies, and data backup and recovery strategies can help protect data. AWS services that support these include AWS KMS, AWS Certificate Manager (ACM), Secrets Manager, Amazon Simple Storage Service (Amazon S3), and Amazon RDS. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Network redundancy, load balancing, and distributed architecture can help implement a highly available network topology. AWS services that help ensure high availability while minimizing the impact of any single point of failure include Amazon Route 53, ELB, AWS Global Accelerator, Amazon RDS Multi-AZ, and Amazon VPC. Loosely coupled dependencies, throttling, retry limits, and stateless compute can help establish a reliable application-level architecture. AWS services that can help with this include AWS Lambda, Amazon API Gateway, Amazon Simple Queue Service (Amazon SQS), Amazon Simple Notification Service (Amazon SNS), and Amazon MQ. Auto-scaling, load testing, and capacity planning can help adapt to changes in demand when implemented. AWS services that can help with this include Amazon EC2 Auto Scaling and AWS CloudFormation. Use AWS Backup and AWS Elastic Disaster Recovery to ensure that data is regularly backed up and can be recovered in the event of a disaster. Test the system's resilience using AWS Fault Injection Service to simulate various types of failures and ensure that the system is capable of withstanding failures. There may be limits and constraints such as service quotas, network latency, and geographic limitations that you need to be aware of. AWS services that can help resolve these constraints include AWS Trusted Advisor and Service Quotas. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

You can experiment with this Guidance and optimize it based on your data by using AWS services such as CloudWatch, X-Ray, Trusted Advisor, and Amazon Athena. Use these services to gather data, analyze the data, and identify areas for improvement. Use Amazon CloudFront, Route 53, and Global Accelerator to select the location where this Guidance should be deployed to decrease latency and improve performance. To meet the workload requirements of scaling, traffic patterns, and data access patterns, AWS services such as Amazon EC2 Auto Scaling, ELB, S3 Transfer Acceleration, and more, can be used. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

When selecting services, you should consider the pricing model, the utilization of resources, and the cost of data transfer. AWS offers a range of pricing models such as pay-as-you-go, reserved instances, and spot instances. It is important to choose the pricing model that best suits your needs to optimize cost. You should also consider the utilization of resources and scale the resources based on demand to avoid over provisioning. You can plan for data transfer charges by estimating the amount of data transfer between AWS services to and from the internet. AWS offers various pricing tiers for data transfer, and you can choose the one that fits your usage pattern. CloudFront can help reduce data transfer costs. You can also use pricing models, such as reserved instances and spot instances, to reduce costs. Reserved instances provide a discounted hourly rate when you commit to using an instance for a specific term, while spot instances allow you to bid on unused EC2 capacity at a lower price. You can also use cost allocation tags to track and optimize costs. This Guidance uses Amazon VPC configured with private subnets following SWIFT CSP protocols, and resources such as EC2 instances, Amazon RDS instances, and Amazon MQ instances are deployed based on demand. Autoscaling groups can also be used to scale resources based on demand. Using these strategies, you can ensure that you are only using the minimum resources required and that you are scaling to match the demand. Additionally, AWS provides tools such as Trusted Advisor and AWS Cost Explorer to help monitor and optimize costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

To scale efficiently, this Guidance implements autoscaling groups, which dynamically adjusts the number of EC2 instances based on demand. Additionally, Amazon Elastic Container Service (Amazon ECS) can run containerized applications and scale horizontally to maintain performance. Lambda can also be used for event-driven applications to scale automatically based on incoming requests. This Guidance implements architecture patterns such as horizontal scaling and load balancing to ensure consistent high utilization of deployed resources. ELB distributes incoming traffic across multiple EC2 instances, while CloudFront can be used to cache frequently accessed content and reduce the load on origin servers. To support data access and storage patterns, this Guidance utilizes Amazon S3 for object storage and Amazon RDS. Amazon Elastic File System (Amazon EFS) can also be used for shared file storage. These services provide flexible and scalable storage options that can meet various data access patterns. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
