---
source_url: https://docs.aws.amazon.com/whitepapers/latest/strategies-migrating-oracle-db-to-aws/strategies-migrating-oracle-db-to-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Strategies for Migrating Oracle Databases to AWS
<a name="strategies-migrating-oracle-db-to-aws"></a>

Publication date: **January 27, 2022** ([Document history](document-revisions.md))

 Amazon Web Services (AWS) provides a comprehensive set of services and tools for deploying enterprise-grade solutions in a rapid, reliable, and cost-effective manner.

 [Oracle Database](https://www.oracle.com/database/) is a widely used relational database management system that is deployed in enterprises of all sizes. It manages various forms of data in many phases of business transactions. This whitepaper describes the preferred methods for migrating an Oracle Database to AWS, and helps you choose the method that is best for your business.

## Introduction
<a name="introduction"></a>

 This whitepaper presents best practices and methods for migrating [Oracle Database](https://www.oracle.com/database/) from servers that are on-premises or in your data center to AWS. Data, unlike application binaries, cannot be recreated or reinstalled, so you should carefully plan your data migration and base it on proven best practices.

 AWS offers its customers the flexibility of running Oracle Database on [Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS), the managed database service in the cloud, as well as [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2):
+  **Amazon RDS** makes it simple to set up, operate, and scale a relational database in the cloud. It provides cost-efficient, resizable capacity for an open standard relational database, and manages common database administration tasks.
+  **Amazon EC2** provides scalable computing capacity in the cloud. Using Amazon EC2 removes the need to invest in hardware up front, so you can develop and deploy applications faster. You can use Amazon EC2 to launch as many or as few virtual servers as you need, configure security and networking, and manage storage.

 Running the database on Amazon EC2 is very similar to running the database on your own servers. Depending on whether you choose to run your Oracle Database on Amazon EC2 or Amazon RDS, the process for data migration can differ. For example, users don’t have OS-level access in Amazon RDS instances. It’s important to understand the different possible strategies, so you can choose the one that best fits your needs.
