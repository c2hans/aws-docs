---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/query-lifecycle-redshift/introduction.html
---

# Understanding the query lifecycle in Amazon Redshift
<a name="introduction"></a>

*Ethan Stark, Amazon Web Services*

## Overview
<a name="overview"></a>

You can use Amazon Redshift to query petabytes of structured and semi-structured data across your data warehouse and your data lake by using standard SQL. A deeper understanding of the SQL query lifecycle can help you optimize your SQL queries and get more out of Amazon Redshift. This guide provides you with an overview of the SQL query lifecycle that explains the following:
+ How the core architecture components of an Amazon Redshift data warehouse work
+ How query processing works
+ How to develop a query plan and use the `EXPLAIN` statement
+ How to use system tables and views

You can use what you learn in this guide to design or use more efficient and effective queries in Amazon Redshift.

## Intended audience
<a name="audience"></a>

This guide is intended for data engineers, data architects, and data analysts who design or use queries in Amazon Redshift.

## Objectives
<a name="objectives"></a>

This guide can help you and your organization achieve the following objectives:
+ Develop an efficient and effective query plan
+ Learn to use the `EXPLAIN` statement to maximize the effectiveness of your queries
+ Optimize the performance of queries in Amazon Redshift
