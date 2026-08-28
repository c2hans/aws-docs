---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/database-refactor-prioritization/introduction.html
---

# Prioritization guide for refactoring Microsoft SQL Server and Oracle databases on AWS
<a name="introduction"></a>

*Sagar Patel, Amazon Web Services*

The adoption of open-source databases, which provide lower costs, speed, and agility, is growing at a rapid pace.  You might be planning to migrate your on-premises Microsoft SQL Server or Oracle commercial databases to open-source database engines such as PostgreSQL and MySQL on Amazon Web Services (AWS). However, the lack of tools, lack of resources, and time constraints might make it difficult to quickly identify databases that will require minimal effort to migrate.

This guide outlines a process that automates data collection and analysis, and prioritizes targets to better identify candidate databases. This process helps minimize the resources, cost, and effort that are involved in identifying the databases that can be migrated to an open-source database engine. The guide explains how to iterate through low-effort tasks to analyze database compatibility with an open-source engine, and helps you generate a prioritized list of databases that can be migrated with minimal effort.

The guide is for program or project managers, database administrators, database engineers, and operations or infrastructure managers who are planning to migrate their Oracle or SQL Server databases to open-source databases on AWS.

## Selection and prioritization process
<a name="selection-and-prioritization-process"></a>

The database replatform prioritization process discussed in this guide includes three main steps:

1. [Collect configuration management database (CMDB) data](cmdb.md)

1. [Collect schema-based PL/SQL objects and sizing](https://aws.amazon.com/prescriptive-guidance/latest/database-refactor-prioritization/pl-sql.html)

1. [Run AWS Schema Conversion Tool (AWS SCT) reports to identify candidate databases](https://aws.amazon.com/prescriptive-guidance/latest/database-refactor-prioritization/sct.html)

![Three steps for selecting and prioritizing SQL Server and Oracle databases to refactor on AWS](http://docs.aws.amazon.com/prescriptive-guidance/latest/database-refactor-prioritization/images/guide-img/d514dcdf-d1f9-43a2-ac0b-46dc109cf9b2/images/48a36a80-084f-4641-9b3f-6ee87d4ea2be.png)

## Attachments
<a name="attachments-d514dcdf-d1f9-43a2-ac0b-46dc109cf9b2"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
