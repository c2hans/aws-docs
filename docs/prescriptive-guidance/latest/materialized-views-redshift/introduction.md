---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/materialized-views-redshift/introduction.html
---

# Using materialized views in Amazon Redshift
<a name="introduction"></a>

*Ethan Stark, Srinivasan Krishnasamy, and Kelly Ragan, Amazon Web Services*

## Overview
<a name="overview"></a>

Data warehouse applications often require you to perform complex queries on large tables. Processing these queries can be time-consuming and expensive. For example, when you run a query in Amazon Redshift, the leader node parses, validates, plans, optimizes, and runs your query. This process can increase your opportunity costs and actual costs by using up a significant amount of wall-clock time, CPU time, and memory.

This guide shows you how to use materialized views in Amazon Redshift to speed up queries, especially predictable and frequently repeated queries. Materialized views reduce query time by storing a precomputed result set, so that you don't have to directly access underlying base tables. Reduced query times, in turn, can reduce the cost of query processing so that you can cost-effectively scale your application. This guide is intended for data engineers, data architects, and data analysts.

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

You can use this guide to achieve the following business outcomes:
+ Reduce the cost of processing Amazon Redshift queries
+ Grow your application efficiently and cost-effectively
+ Free up users to spend time on higher-value tasks

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
