---
source_url: https://docs.aws.amazon.com/solutions/high-availability-oracle-databases-on-aws/index.html
---

---
title: 'Guidance for High Availability Oracle Databases on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/high-availability-oracle-databases-on-aws/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for High Availability Oracle Databases on AWS

Deploy Oracle databases with high availability instances on AWS

## Overview

This Guidance helps customers set up high availability for Oracle databases using Amazon RDS Custom for Oracle service, a managed cloud data service that makes it easier to operate and scale relational databases. It addresses the challenges for those who want to utilize Amazon RDS Custom for Oracle, but don't have an automated way to implement those instances. This hinders their ability to meet application service level agreements and requires manually configuring high availability instances. This Guidance can help customers streamline their high availability setup, offload complex configuration tasks, and ensure maximum availability, thanks to the integration of Oracle Data Guard with Fast-Start Failover monitoring.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/high-availability-oracle-databases-on-aws.pdf)

![Architecture diagram](/images/solutions/high-availability-oracle-databases-on-aws/images/high-availability-oracle-databases-on-aws-1.png)

1. **Step 1**: Upload Oracle Database 19c Client into an Amazon Simple Storage Service (Amazon S3) bucket and provide that bucket name as an input to the AWS CloudFormation script.
1. **Step 2**: Deploy the CloudFormation script using the CloudFormation console or command line interface (CLI) by passing the required input parameters.
1. **Step 3**: CloudFormation creates the required AWS Identity and Access Management (IAM) roles and permissions. AWS Lambda functions help support the operations performed by the CloudFormation script.
1. **Step 4**: CloudFormation provisions an Amazon Elastic Compute (Amazon EC2) instance, copies the Oracle client media from the Amazon S3 bucket, installs it on the Amazon EC2 instance, and sets up the Oracle client. This Amazon EC2 instance acts as the Oracle Data Guard observer instance that observes, monitors, and initiates failover from primary to standby.
1. **Step 5**: CloudFormation then invokes the creation of an Amazon Relational Database Service (Amazon RDS) Custom for Oracle read replica for the primary instance provided by the customer. This replica acts as the standby instance for this high availability setup.
1. **Step 6**: The Oracle clients communicate with the database using the Transparent Network Substrate (TNS) protocol. TNS connectivity is set up and verified from the Oracle Data Guard observer instance to both the primary and the standby instances. The Oracle Data Guard user password is fetched from AWS Secrets Manager to make the connection. In this architecture, we use AWS Systems Manager document (SSM document) to perform this automation.
1. **Step 7**: Oracle Data Guard makes configuration changes, sets up synchronous log shipping, and enables Data Guard Fast-Start Failover that is automated through the SSM document.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-high-availability-oracle-databases-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

CloudFormation and Systems Manager documents were deployed throughout this Guidance to enhance operational excellence. These services help automate post-instance creation tasks in Amazon RDS Custom for Oracle databases, enabling users to quickly set up, monitor, and understand the state and achievement of business outcomes for their environment. The use of CloudFormation and Systems Manager streamlines the process of integrating and deploying changes to the high availability setup, ensuring efficient and controlled modifications to the database stack. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Amazon EC2 security groups, IAM, and AWS Key Management Service (AWS KMS) work collectively to enhance security in this Guidance. Using Amazon EC2 security groups and IAM policies, access is granted to the Amazon EC2 observer instance based on the principal of least privilege. Only the required ports for the database listener and the Oracle Data Guard communication are open between the Amazon EC2 instance and the Amazon RDS Custom database instance. Also, infrastructure protection is prioritized by restricting access through the Amazon EC2 security group settings. Finally, data protection is ensured by requiring an AWS KMS key for encryption in Amazon RDS Custom for Oracle, and by scoping IAM policies to the minimum permissions required, with only authorized access allowed. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

CloudFormation and AWS CloudTrail work in tandem to enhance reliability throughout this Guidance. CloudTrail monitors and tracks changes, and CloudFormation streamlines deployment. These measures collectively contribute to ensure failover management, effective monitoring, and consistent deployments. When it comes to monitoring and tracking changes, Amazon RDS Custom for Oracle automatically generates a CloudTrail entry that is crucial for Amazon RDS Custom for Oracle automation logs. This ensures effective monitoring of actions that may impact the system's reliability. To streamline the deployment process and ensure consistency, the script is built on CloudFormation. This script simplifies the deployment of the entire stack, reducing the chances of errors and ensuring reliable deployments. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon RDS Custom for Oracle was deployed throughout this Guidance to enhance performance efficiency. This service is designed for privileged access to databases and operating systems, making it ideal for critical workloads that require high availability. It offers a streamlined deployment option, allowing users to implement, test, and easily customize configuration settings such as an Amazon RDS instance size, observer instance size, Oracle Data Guard configuration parameters, and Fast-Start Failover parameters. Also, Amazon RDS Custom for Oracle can be customized to meet the requirements of older, custom, and packaged applications. Implementing this Guidance in multiple Availability Zones within the same Region ensures maximum availability and optimal performance. And, the streamlined deployment option allows for easy customization of your configuration settings. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon EC2 and a Virtual Private Cloud (VPC) are used throughout this Guidance to optimize the cost of your workloads. An Amazon EC2 instance evaluates the cost by leveraging the pay-as-you-go model. This Guidance also uses an Amazon EC2 T3 instance, which are the low-cost general purpose instance types. This Guidance also uses Amazon RDS Custom for Oracle within the same VPC, which further eliminates data charges across VPCs. By utilizing the managed service capabilities in this Guidance, you can benefit from scalable compute and storage options, ensuring that resources are scaled to match the demand dynamically. This approach also ensures that only the minimum resources required are provisioned, effectively optimizing costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon EC2, Lambda, and Amazon RDS Custom for Oracle enhance sustainability in this Guidance. These services can easily scale up or down to match the load, using the scale compute feature, for sustainable utilization of resources. Lambda offers automatic scaling based on demand, and being a serverless service, it reduces the chances of overprovisioning your resources. This helps ensure maximum utilization of resources. Finally, Amazon EC2 and Amazon RDS Custom for Oracle can also be configured to scale up or down based on demand. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
