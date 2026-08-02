---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/essential-eight-maturity/scenario.html
---

# Scenario and architecture overview
<a name="scenario"></a>

The government agency has three workloads in the AWS Cloud:
+ A [serverless data lake](serverless-data-lake.md) that uses Amazon Simple Storage Service (Amazon S3) for storage and AWS Lambda for extract, transform, and load (ETL) operations
+ A [containerised web service](containerised-web-service.md) that runs on Amazon Elastic Container Service (Amazon ECS) and uses a database in Amazon Relational Database Service (Amazon RDS)
+ A [commercial off-the-shelf (COTS) software](cots-software.md) running on Amazon EC2

A *cloud team* provides a centralised platform for the organisation, running core services for the AWS environment. A cloud team provides core services for the AWS environment. Each workload is owned by a distinct *application team*, also known as a *developer team* or *delivery team*.

## Core architecture
<a name="core-architecture"></a>

The cloud team has already established the following capabilities in the AWS Cloud:
+ Identity federation links AWS IAM Identity Center to their Microsoft Entra ID (formerly *Azure Active Directory*) instance. The federation enforces MFA, automatic expiry of user accounts, and the use of short-lived credentials through AWS Identity and Access Management (IAM) roles.
+ A centralised AMI pipeline is used to patch OSs and core applications with EC2 Image Builder.
+ Amazon Inspector is enabled to identify vulnerabilities, and all security findings are sent to Amazon GuardDuty for centralised management.
+ Established mechanisms are used to update application control rules, respond to cyber security events, and review compliance gaps.
+ AWS CloudTrail is used for logging and monitoring.
+ Security events, such as login of the root user, initiate alerts.
+ SCPs and VPC endpoint policies establish data perimeters for your AWS environments.
+ SCPs prevent application teams from disabling security and logging services, such as CloudTrail and AWS Config.
+ AWS Config findings are aggregated from across the whole AWS organization into a single AWS account for security.
+ The AWS Config [ACSC Essential 8 conformance pack](https://docs.aws.amazon.com/config/latest/developerguide/operational-best-practices-for-acsc_essential_8.html) is enabled across all AWS accounts in your organization.
