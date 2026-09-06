---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/query-best-practices-redshift/introduction.html
---

# Query best practices for Amazon Redshift
<a name="introduction"></a>

*Ethan Stark, Amazon Web Services*

## Overview
<a name="overview"></a>

This guide provides recommendations and best practices for optimizing query and table performance in [Amazon Redshift](https://docs.aws.amazon.com/redshift/). You can use Amazon Redshift to query petabytes of structured and semi-structured data across your data warehouse and your data lake by using standard SQL. This guide also provides an overview of the core architecture components of an Amazon Redshift data warehouse. This knowledge—along with an understanding of query performance factors such as table properties, cluster configuration, and query structure—can help you design efficient and effective tables and queries for your Amazon Redshift data warehouse.

## Intended audience
<a name="intended-audience"></a>

This guide is intended for data engineers, data architects, and data analysts who design or use tables and queries in Amazon Redshift.

## Objectives
<a name="objectives"></a>

This guide can help you and your organization achieve the following objectives:
+ Design tables for optimal data storage and retrieval operations
+ Design queries for optimal performance and cost savings
+ Optimize the performance of [Amazon Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-using-spectrum.html) to query data directly from files on [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
