---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-full-table-copy-options/introduction.html
---

# Cross-account full table copy options for Amazon DynamoDB
<a name="introduction"></a>

*Ramkumar Ramanujam, Amazon Web Services*

This guide covers different ways to perform full table copying of Amazon DynamoDB tables across multiple Amazon Web Services (AWS) accounts. This guide also lists the advantages and drawbacks of each solution and the scenarios for which each solution can be considered. It does not cover streaming-replication solutions.

This guide is intended for architects, managers, and technical leads who have a basic understanding of DynamoDB.

## Overview
<a name="overview"></a>

To improve application performance and to reduce operational costs and burdens, many organizations are switching over to DynamoDB.

A common use case while working with DynamoDB tables is the ability to copy full table data across multiple environments. Usually, each environment is owned by a different team using a different AWS account. An example of such a use case is the promotion of code from development to staging and then to production environments. The staging environment is refreshed with the data in production so that it is closest to that of production for conducting tests before promoting to production.

This guide gives a high-level overview of several approaches for copying a full refresh of a DynamoDB table from one account to another.

The best way to ensure that the target table has the same data as the source table is to delete and then recreate the table. (The exception to this approach is when the difference between the source and target tables is minimal—for example, less than 10 percent.) Deleting and recreating the table avoids the costs associated with the write capacity units (WCUs) required to delete individual items from the table. Each of the solutions discussed in this guide assumes that the target table is recreated before the data refresh.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
