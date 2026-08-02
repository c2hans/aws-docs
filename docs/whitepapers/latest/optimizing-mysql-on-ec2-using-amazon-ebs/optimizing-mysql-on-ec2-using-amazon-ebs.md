---
source_url: https://docs.aws.amazon.com/whitepapers/latest/optimizing-mysql-on-ec2-using-amazon-ebs/optimizing-mysql-on-ec2-using-amazon-ebs.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Optimizing MySQL Running on Amazon EC2 Using Amazon EBS
<a name="optimizing-mysql-on-ec2-using-amazon-ebs"></a>

Publication date: **December 7, 2021** ([Document history](document-revisions.md))

 This whitepaper is intended for Amazon Web Services (AWS) customers who are considering deploying their MySQL database on Amazon Elastic Compute Cloud (Amazon EC2) using Amazon Elastic Block Store (Amazon EBS) volumes. This whitepaper describes the features of EBS volumes and how they can affect the security, availability, durability, cost, and performance of MySQL databases. There are many deployment options and configurations for MySQL on Amazon EC2. This whitepaper provides performance benchmark metrics and general guidance so AWS customers can make an informed decision about whether to deploy their MySQL workloads on Amazon EC2.

## Introduction
<a name="introduction"></a>

 MySQL is one of the world’s most popular open-source relational database engines. Its unique storage architecture provides you with many different ways of customizing database configuration according to the needs of your application. It supports transaction processing and high-volume operations. Apart from the robustness of the database engine, another benefit of MySQL is that the total cost of ownership is low. Several companies are moving their MySQL workloads into the cloud to extend the cost and performance benefits. AWS offers many compute and storage options that can help you optimize your MySQL deployments.
