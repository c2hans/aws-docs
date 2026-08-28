---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aurora-replication-options/introduction.html
---

# Comparing Amazon Aurora Replicas, Aurora cross-Region Replicas, and Aurora global databases
<a name="introduction"></a>

*Naveen Garg, Amazon Web Services*

Amazon Aurora is a fully managed relational database engine that's compatible with MySQL and PostgreSQL. In addition to all the benefits of open source, Aurora combines a high-performance storage subsystem to offer you options in terms of choosing the right solution for your high availability (HA) and disaster recovery (DR) needs on Amazon Web Services (AWS). This guide provides an in-depth look at three powerful features:
+ Aurora Replicas
+ Cross-Region Aurora Replicas
+ Aurora global databases

Each of these three options support replicating your production Aurora database beyond the capabilities of a single machine. Choosing among these options can be challenging.

## Overview
<a name="overview"></a>

Database administrators have always wanted to replicate their production databases beyond a single machine for HA and DR purposes. Historically, setting up and managing a replication solution involved time-consuming tasks and often required a specialized skill set. Amazon Aurora simplifies these tasks, and it handles the underlying automation, fault tolerance, and monitoring on your behalf. Aurora extends the native replication solutions available in open source MySQL and PostgreSQL, giving you more choices to fit your business needs.

This document introduces each of these three replication solutions available with Aurora, and it provides a comparison table that you can use as a quick reference guide when deciding which solution best fits your business requirements.

## Aurora compute and storage
<a name="compute-storage"></a>

Understanding the terminology of Aurora compute and storage is essential to understanding the different replication solutions.

Aurora compute refers to the database instance (set of processes) running on a host. This is the set of processes that you see in Task Manager on Windows or in `"ps -ef"` output on Linux. When you restart a database, you are essentially restarting these processes on a [host](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.DBInstanceClass.html).

Aurora storage refers to the underlying storage subsystem. Think of this as your on-premises storage arrays, but with added durability and scalability. For more information about Aurora storage, see the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.StorageReliability.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
