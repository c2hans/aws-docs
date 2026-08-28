---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluate-downgrading-sql-server-edition/introduction.html
---

# Evaluate downgrading Microsoft SQL Server from Enterprise edition to Standard edition on AWS
<a name="introduction"></a>

*Marcelo Fernandes and Paurav Chudasama, Amazon Web Services*

This guide discusses how to perform an in-depth assessment of Microsoft SQL Server Enterprise edition databases and convert them to SQL Server Standard edition during a migration to [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) on Amazon Web Services (AWS). The information presented also applies if your SQL Server Enterprise edition databases are already running on Amazon RDS.

This guide is for program or project managers, product owners, database and application administrators, database engineers, operations or infrastructure managers, and database and system architects.

## Overview
<a name="overview"></a>

In many organizations, SQL Server Enterprise edition is the default deployment option for production workloads. This might be due to a common misconception that a SQL Server Standard edition database is not capable of supporting enterprise-class applications. Both Enterprise edition and Standard edition share a common code base, so technically they offer the same SQL Server database functionalities.

SQL Server Enterprise edition offers additional options, but it is significantly more expensive than the Standard edition. Downgrading to Standard edition provides an opportunity to reduce the overall total cost of ownership of your databases. Applications with minimum or no usage of Enterprise edition features are good candidates for downgrades to SQL Server Standard edition.

Amazon RDS facilitates setting up, operating, and scaling a relational database in the cloud. It provides cost-efficient and [resizable capacity](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.InstanceClassesnceClasses) while automating time-consuming administration tasks such as hardware provisioning, database setup, patching, and backups. Amazon RDS for SQL Server offers the License Included (LI) model. For more details, see [Amazon RDS for SQL Server FAQs](https://aws.amazon.com/rds/sqlserver/faqs/).

SQL Server Standard edition on Amazon RDS delivers enterprise-class features and performance with options such as [Multi-AZ deployment](https://aws.amazon.com/rds/features/multi-az/) for high availability, [Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html) for performance tuning, and [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MonitoringOverview.html) for monitoring.

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

The goal of this guide is to provide the following business outcomes:
+ **Cost savings on SQL Server licensing fees** – Downgrading to Standard edition reduces the total cost of running your applications.
+ **Reduce the need for large capital outlays** – Amazon RDS for SQL Server offers License Included (LI) licensing, which allows you to pay only for what you use.
+ **Efficient assessment** – Bulk assessment of your database estate helps in determining the suitability of downgrading to Standard edition.

## Attachments
<a name="attachments-4f72b44a-289d-4c64-8325-b36e4aec7488"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
