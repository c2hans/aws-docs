---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sap-ase-to-amazon-rds-sql-server-database-migration/introduction.html
---

# Migrating an on-premises SAP ASE database to Amazon RDS for SQL Server
<a name="introduction"></a>

*Amit Kumar, Jitendra Kumar, and Nishad Mankar, Amazon Web Services*

This guide describes options for migrating an SAP ASE database to [Amazon Relational Database Service (Amazon RDS) for SQL](https://aws.amazon.com/rds/sqlserver/) Server. Amazon RDS for SQL Server is a common migration choice for SAP ASE workloads because it supports Transact-SQL (T-SQL) commands and features. It also supports Tabular Data Stream (TDS), which is the native client-server communication protocol for SQL Server.

Organizations often migrate from [SAP Adaptive Server Enterprise (SAP ASE)](https://www.sap.com/products/technology-platform/sybase-ase.html) to Amazon RDS for SQL Server to reduce licensing costs and automate database management using AWS services. Amazon RDS automates administration tasks like backups, software patching, and high-availability features while maintaining performance and security.

## Objectives
<a name="objectives.258f5cdd-9c0b-5c51-84a5-b0f2402ed7fd"></a>

This guide describes how to migrate applications that run on SAP ASE databases to AWS. Learn about migration approaches, implementation phases, and specific steps for replatforming and refactoring your applications. Select a migration strategy that aligns with your business requirements and technical environment to help reduce downtime and optimize costs.

## Intended audience
<a name="intended-audience.15fc4996-da93-5bc2-a8ed-a3009da0ab8c"></a>

This guide is for database administrators, database engineers, and migration engineers who intend to migrate an SAP ASE database to the AWS Cloud. This guide assumes that you have knowledge of the following services and concepts:
+ Amazon RDS for SQL Server and related database technologies
+ AWS Database Migration Service (AWS DMS) features, limitations, and security requirements
+ Using SAP ASE as a source for AWS DMS, including limitations with SQL Server as a target
+ Network setup for AWS DMS replication
+ Schema conversion tools for SAP ASE and SQL Server
