---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/archiving-mysql-data/introduction.html
---

# Archiving data in Amazon RDS for MySQL, Amazon RDS for MariaDB, and Aurora MySQL-Compatible
<a name="introduction"></a>

*Shyam Sunder Rakhecha, Oliver Francis, Abhishek Karmakar, and Saumya Singh, Amazon Web Services*

The need to archive historical data can stem from different use cases. Your application might have been designed without archiving capability, and growth in your business over time could result in large amounts of historical data. This inevitably leads to degraded performance. You might also retain historical data because of compliance requirements within your organization.

This guide discusses how to archive your historical data in Amazon Simple Storage Service (Amazon S3) with minimal impact to your application and retrieve archived information when you need it.

## Overview
<a name="overview"></a>

This guide covers different approaches for archiving historical data from large tables in Amazon Relational Database Service (Amazon RDS) for MySQL, Amazon RDS for MariaDB, and Amazon Aurora MySQL-Compatible Edition on the Amazon Web Services (AWS) Cloud. In this guide, you will learn how to archive both partitioned table data and data that is not partitioned and resides in large tables. You can implement the approaches presented in the guide to reduce the size of your live data while keeping important historical data for further analysis.

Archiving your table data regularly results in a slimmer set of live data in your tables, which leads to faster reads and writes and improves the performance of your application. Regular data archiving falls under the operational excellence and performance efficiency pillars of the [Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc&wa-guidance-whitepapers.sort-by=item.additionalFields.sortDate&wa-guidance-whitepapers.sort-order=desc). When you move older data to Amazon Simple Storage Service (Amazon S3) and clean up your archived data in your Amazon RDS instance or Aurora MySQL-Compatible cluster, you can save on storage costs. This fits the cost optimization pillar and helps you avoid unnecessary costs on AWS.
