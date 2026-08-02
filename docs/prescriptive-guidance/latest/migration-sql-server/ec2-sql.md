---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/ec2-sql.html
---

# Amazon EC2 for SQL Server
<a name="ec2-sql"></a>

Amazon Elastic Compute Cloud (Amazon EC2) supports a self-managed SQL Server database. That is, it gives you full control over the setup of the infrastructure and the database environment. Running the database on Amazon EC2 is very similar to running the database on your own server. You have full control of the database and operating system-level access, so you can use your choice of tools to manage the operating system, database software, patches, data replication, backup, and restoration. This migration option requires you to set up, configure, manage, and tune all the components, including Amazon EC2 instances, storage volumes, scalability, networking, and security, based on AWS architecture best practices. You are responsible for data replication and recovery across your instances in the same or different AWS Regions.
