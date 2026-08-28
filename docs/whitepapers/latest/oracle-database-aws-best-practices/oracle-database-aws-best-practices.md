---
source_url: https://docs.aws.amazon.com/whitepapers/latest/oracle-database-aws-best-practices/oracle-database-aws-best-practices.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Best Practices for Running Oracle Database on AWS
<a name="oracle-database-aws-best-practices"></a>

Publication date: **November 18, 2021** ([Document History and Contributors](document-revisions.md))

## Abstract
<a name="abstract"></a>

Amazon Web Services (AWS) offers you the ability to run your Oracle Database in a cloud environment. Running Oracle Database in the AWS Cloud is very similar to running Oracle Database in your data center. To a database administrator or developer, there are no differences between the two environments. However, there are a number of AWS platform considerations relating to security, storage, compute configurations, management, and monitoring that will help you get the best out of your Oracle Database implementation on AWS.

This whitepaper provides best practices for achieving optimal performance, availability, and reliability, and lowering the total cost of ownership (TCO) while running Oracle Database in the AWS Cloud. The target audience for this whitepaper includes database administrators, enterprise architects, systems administrators, and developers who would like to run their Oracle Database in the AWS Cloud.

## Introduction
<a name="introduction-section"></a>

Amazon Web Services (AWS) provides a comprehensive set of services and tools for deploying Oracle Database on the reliable and secure AWS Cloud infrastructure. AWS offers its customers the following options for running Oracle Database on AWS:

1. Using [Amazon Relational Database Service (Amazon RDS) for Oracle](https://aws.amazon.com/rds/oracle/), which is a managed database service that helps simplify the provisioning and management of Oracle databases. RDS for Oracle makes it easy to set up, operate, and scale a relational database in the cloud by automating installation, disk provisioning and management, patching, minor version upgrades, failed instance replacement, as well as backup and recovery tasks. The push-button scaling feature of Amazon RDS allows you to easily scale the database instance up or down for better cost management and performance. RDS for Oracle offers both Oracle Database Enterprise Edition and Oracle Database Standard Edition. RDS for Oracle also comes with a [License-Included service model](https://aws.amazon.com/rds/oracle/pricing/), which allows you to pay per use by the hour.

1. Running a self-managed Oracle Database directly on Amazon Elastic Compute Cloud (Amazon EC2). This option gives you full control over the setup of the infrastructure and database environment. Running the database on Amazon EC2 is very similar to running the database on your own server. You have full control of the Oracle binaries database and have operating system-level access, so you can run monitoring and management agents and use your choice of tools for data replication, backup, and restoration. Furthermore, you have the ability to use every optional module available in Oracle Database. However, this option requires you to set up, configure, manage, and tune all the components, including Amazon EC2 instances, storage volumes, scalability, networking, and security based on AWS architecture best practices. In the fully-managed Amazon RDS (Amazon RDS) service, this is all taken care of for you.

1. FlashGrid Cluster virtual appliances enable running self-managed Oracle Real Application Cluster (RAC) and Oracle RAC extended clusters (across different AZs) on Amazon EC2. With FlashGrid Cluster you also have full control of the database and have operating system-level access.

1. Running a self-managed Oracle Database directly on VMware Cloud on AWS. VMware Cloud on AWS is an integrated cloud offering jointly developed by AWS and VMware. Like Amazon EC2, you have full control of the database and have operating system-level access. You can run advanced architectures like Oracle Real Application Cluster (RAC) and Oracle RAC extended clusters (across different AZs) in VMware Cloud on AWS.

Whether you choose to run a self-managed Oracle Database on Amazon EC2 or the fully-managed RDS for Oracle, following the best practices discussed in this whitepaper will help you get the most out of your Oracle Database implementation on AWS. AWS will discuss Oracle licensing options, considerations for choosing Amazon EC2 or Amazon RDS for your Oracle Database implementation, and how to optimize network configuration, instance type, and database storage in your implementation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
