---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/archiving-mysql-data/targeted-business-outcomes.html
---

# Targeted business outcomes
<a name="targeted-business-outcomes"></a>

This guide focuses on the following business outcomes:
+ Improved user experience
+ Data compliance requirements fulfilled
+ Reduced storage costs
+ Organized data

## Improved user experience
<a name="improved-user-experience.742c2165-378c-5854-a4fa-9e8cb0e7328c"></a>

Databases that retain historical data can have sluggish performance because of large tables and indexes. When you archive your historical data, you slim your tables and indexes. This has a direct positive impact on customer-facing API operations that interact with your database.

## Data compliance requirements fulfilled
<a name="data-compliance-requirements-fulfilled.d4248bbd-efa6-55f1-b4d8-4b2f5884bf1b"></a>

Industries such as financial services, public sector organizations, and healthcare have stringent archival requirements. By archiving application data that resides on your Amazon RDS for MySQL, Amazon RDS for MariaDB, or Aurora MySQL-Compatible database in Amazon S3, you can meet the requirements for regulated compliance, including the following:
+ Payment Card Industry Data Security Standard (PCI DSS)
+ Health Insurance Portability and Accountability Act (HIPAA) and Health Information Technology for Economic and Clinical Health (HITECH) Act
+ Federal Risk and Authorization Management Program (FedRAMP)
+ General Data Protection Regulation (GDPR)
+ Federal Information Processing Standards (FIPS) 140-2
+ National Institute of Standards and Technology (NIST) 800–171

## Reduced storage costs
<a name="reduced-storage-costs.bec09a73-72e1-5eb8-ac12-34671c233780"></a>

Keeping data in Amazon RDS increases storage cost and requires higher IOPS. If you compare the cost of storage per GB-month for [Amazon RDS for MySQL Multi-AZ GP2](https://aws.amazon.com/rds/mysql/pricing/) with that of [Amazon S3 Glacier](https://aws.amazon.com/glacier/pricing/) in the `us-east-1` AWS Region, the S3 Glacier storage cost is about 57 times lower than that of Amazon RDS.

## Organized data
<a name="organized-data.744e13aa-8021-5ebf-9aeb-474701e3b6ab"></a>

It's good to keep informative data that will be accessed frequently by application in the database. However, applications generate a large quantity of data that isn't required very often or becomes stale. These records can be archived and kept in place, which is cost-effective and doesn't impact application performance.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
