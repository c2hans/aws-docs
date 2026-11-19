---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/essential-eight-maturity/scenario.html
---

# Scenario and architecture overview

The government agency has three workloads in the AWS Cloud:
+ A [serverless data lake](serverless-data-lake.md) that uses Amazon Simple Storage Service (Amazon S3) for storage and AWS Lambda for extract, transform, and load (ETL) operations
+ A [containerized web service](containerised-web-service.md) that runs on Amazon Elastic Container Service (Amazon ECS) and uses a database in Amazon Relational Database Service (Amazon RDS)
+ A [commercial off-the-shelf (COTS) software](cots-software.md) application that runs on Amazon Elastic Compute Cloud (Amazon EC2)

A *cloud team* provides centralized core services for the organization in the AWS environment. A distinct *application team* owns each workload. An application team is also known as a *developer team* or *delivery team*.

## Core architecture
<a name="core-architecture"></a>

The cloud team has already established the following capabilities in the AWS Cloud:
+ Identity federation links AWS IAM Identity Center to their Microsoft Entra ID (formerly *Azure Active Directory*) instance. The federation enforces multi-factor authentication (MFA), automatic expiry of user accounts, and the use of short-lived credentials through AWS Identity and Access Management (IAM) roles.
+ The cloud team uses a centralized Amazon Machine Image (AMI) pipeline to patch operating systems and core applications with EC2 Image Builder.
+ The cloud team enabled Amazon Inspector to identify vulnerabilities and sends all security findings to Amazon GuardDuty for centralized management.
+ The cloud team uses established mechanisms to update application control rules, respond to cybersecurity events, and review compliance gaps.
+ The cloud team uses AWS CloudTrail for logging and monitoring.
+ Security events, such as root user sign-in, initiate alerts.
+ Service control policies (SCPs) and Amazon VPC endpoint policies establish data perimeters for the AWS environments.
+ SCPs prevent application teams from disabling security and logging services, such as CloudTrail and AWS Config.
+ The cloud team aggregates AWS Config findings from across the entire AWS organization into a single AWS account for security.
+ The cloud team enabled the AWS Config [Australian Cyber Security Centre (ACSC) Essential 8 conformance pack](https://docs.aws.amazon.com/config/latest/developerguide/operational-best-practices-for-acsc_essential_8.html) across all AWS accounts in the organization.
