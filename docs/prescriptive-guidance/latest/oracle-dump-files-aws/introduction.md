---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/oracle-dump-files-aws/introduction.html
---

# Transferring Oracle Database dump files from on premises to AWS
<a name="introduction"></a>

*Subhani Shaik, Amazon Web Services*

This guide provides different approaches to migrating Oracle Database dump files from your on-premises environment to Amazon Web Services (AWS). The approaches covered include using Amazon Simple Storage Service (Amazon S3), Amazon Elastic File System (Amazon EFS) and an Oracle database link.

## Architecture
<a name="architecture"></a>

The following architecture diagram shows the high-level details of the solution. From the Oracle DB instance in the on-premises data center, data moves through a customer gateway by using AWS Direct Connect. The data passes through a customer router and an Direct Connect route and reaches the virtual private cloud (VPC) through an AWS Virtual Private Network (Site-to-Site VPN) gateway. In the VPC are an Amazon Elastic Compute Cloud (Amazon EC2) instance, an Amazon Relational Database Service (Amazon RDS) for Oracle database, and Amazon EFS. The infrastructure also includes AWS Identity and Access Management (IAM), AWS Key Management Service (AWS KMS), and Amazon S3.

![Architecture diagram.](https://docs.aws.amazon.com/prescriptive-guidance/latest/oracle-dump-files-aws/images/guide-img/5859e5d2-f674-4a5c-b6d2-1c867406b465/images/269968a0-3f07-49af-804e-91db2cc7958d.png)
