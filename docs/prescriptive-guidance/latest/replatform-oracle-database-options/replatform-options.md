---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-oracle-database-options/replatform-options.html
---

# Replatforming options
<a name="replatform-options"></a>

When you replatform Oracle Database from on premises to managed database services on AWS, you have the following options:
+ Amazon RDS for Oracle
+ Amazon RDS Custom for Oracle

The following sections list important features of these options.

## Amazon RDS for Oracle
<a name="amazon-rds-oracle"></a>

[Amazon RDS for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.html) is a managed database service that simplifies the provisioning and management of Oracle databases on AWS. It has the following key advantages:
+ Provides a console for setting up, operating, managing and scaling Oracle database deployments.
+ Automates time-consuming database administration tasks, including provisioning, software patching, monitoring, hardware scaling, and failure detection.
+ Automates the backup and recovery process reliably and efficiently.
+ Provides high availability with a Multi-AZ deployment. The primary instance and a synchronous secondary instance can be used to switch over during planned events, and automatically fail over during unplanned events.
+ Provides provisioning of read replica databases to enhance availability, performance, and reliability.

Amazon RDS for Oracle supports both Enterprise Edition (EE) and Standard Edition 2 (SE2). Oracle Database EE offers enterprise-level features but is significantly more expensive than SE2 in license cost. It also requires the Bring Your Own License (BYOL) licensing model. Applications with no or minimum usage of EE features are good candidates for downgrading to Oracle Database SE2 to reduce total cost of ownership (TCO). For more information, see [Evaluate downgrading Oracle databases to Standard Edition 2 on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluate-downgrading-oracle-edition/welcome.html).

## Amazon RDS Custom for Oracle
<a name="rds-custom-oracle"></a>

[Amazon RDS Custom for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/working-with-custom-oracle.html) is a managed database service for legacy, custom, and packaged applications that require access to the database administrator privilege and underlying operating system. It has the following key features:
+ Automates setup, operation, and scaling of databases in the AWS Cloud.
+ Provides root access to the operating system of the underlying Amazon Elastic Compute Cloud (Amazon EC2) instance, and database access as built-in `SYS` and `SYSTEM` user
+ Provides the capability to configure settings, install patches, and enable native features manually to meet the dependent application and database requirements
+ Provides support on legacy Oracle Database versions (12.1, 12.2, and 18c)
