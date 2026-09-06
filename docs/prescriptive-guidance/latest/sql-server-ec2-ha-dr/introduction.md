---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-ec2-ha-dr/introduction.html
---

# Building a high availability and disaster recovery architecture for SQL Server on Amazon EC2
<a name="introduction"></a>

*Ram Yellapragada, Priya Nair, and Alysia Tran, Amazon Web Services*

Microsoft SQL Server has many native options to support high availability (HA) and disaster recovery (DR), to help ensure business continuity for your database workloads. This guide outlines an ideal configuration for SQL Server on Amazon Elastic Compute Cloud (Amazon EC2) in the Amazon Web Services (AWS) Cloud. Rehosting SQL Server on Amazon EC2 provides a self-managed system where you can retain full control over database operations and configuration.

The guide discusses SQL Server hybrid HA/DR options that include various AWS services and infrastructure, and provides guidance on infrastructure components and settings, including instance classes, storage options, configuration, and HA/DR setup. This document also explains how a given HA/DR strategy might fit into an example use case that has specific recovery time objective (RTO) and recovery point objective (RPO) requirements, and covers a few recovery scenarios, including relevant architecture diagrams. This guide doesn't provide solutions designed for specific applications or requirements. It presents some HA/DR options based on RTO and RPO, so you can choose an architecture that matches your requirements.

In addition, as a sizing exercise, the guide defines HA/DR options for a typical SQL Server online transaction processing (OLTP) workload and provides a side-by-side comparison of these options. For a discussion on rehosting SQL Server on AWS, see the section [Amazon EC2 for SQL Server](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/ec2-sql.html) in the guide *Migrating Microsoft SQL Server databases to the AWS Cloud*. For information about other migration options, see the section [SQL Server database migration strategies](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/strategies.html) in that guide. For additional reading, see the [Next steps and resources](next-steps-and-resources.md) section.
