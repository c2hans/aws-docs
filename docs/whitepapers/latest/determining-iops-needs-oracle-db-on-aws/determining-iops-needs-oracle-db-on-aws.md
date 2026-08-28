---
source_url: https://docs.aws.amazon.com/whitepapers/latest/determining-iops-needs-oracle-db-on-aws/determining-iops-needs-oracle-db-on-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Determining IOPS Needs for Oracle Database on AWS
<a name="determining-iops-needs-oracle-db-on-aws"></a>

Publication date: **November 17, 2021** ([Document history](document-revisions.md))

 Amazon Web Services (AWS) provides a comprehensive set of services and tools for deploying Oracle Database on the AWS Cloud infrastructure, one of the most reliable and secure cloud computing services available today. Many businesses of all sizes use Oracle Database to handle their data needs. Oracle Database performance relies heavily on the performance of the storage subsystem, but storage performance always comes at a price. This whitepaper includes information to help you determine the input/output operations per second (IOPS) necessary for your database storage system to have the best performance at optimal cost.

## Introduction
<a name="introduction"></a>

 AWS offers customers the flexibility to run Oracle Database on either [Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS), which is a managed database service in the cloud, or on [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2). Many customers prefer to use Amazon RDS for Oracle Database because it provides an easy, managed option to run Oracle Database on AWS without having to think about infrastructure provisioning, or installing and maintaining database software. You can also run Oracle Database directly on Amazon EC2, which allows you full control over setup of the entire infrastructure and database environment.

 To get the best performance from your database, you must configure the storage tier to provide the IOPS and throughput that the database needs. This is a requirement for both Oracle Database on Amazon RDS and Oracle Database on Amazon EC2. If the storage system does not provide enough IOPS to support the database workload, you will have sluggish database performance and transaction backlog. However, if you provision much higher IOPS than your database actually needs, you will have unused capacity.

 The elastic nature of the AWS infrastructure allows you to increase or decrease the total IOPS available for Oracle Database on Amazon EC2, but doing this could have a performance impact on the database, requires extra effort, and might require database downtime.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
