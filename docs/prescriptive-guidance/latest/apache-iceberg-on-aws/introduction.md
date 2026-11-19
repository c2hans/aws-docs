---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/introduction.html
---

# Using Apache Iceberg on AWS

*Diego Garcia Garcia and Stefano Sandona, Amazon Web Services*

[Apache Iceberg](https://iceberg.apache.org/) is an open-source table format that simplifies table management while improving performance. AWS analytics services such as Amazon EMR, AWS Glue, Amazon Athena, and Amazon Redshift include native support for Iceberg, so you can easily build transactional data lakes on top of Amazon Simple Storage Service (Amazon S3) on AWS. Beyond native AWS integrations, any Iceberg-compatible client (for example, DuckDB or PyIceberg) can also read and write the same tables through the standardized [Apache Iceberg REST Catalog Open API](https://iceberg.apache.org/rest-catalog-spec/).

This technical guide provides guidance on getting started with Iceberg on different AWS services, and includes best practices and recommendations for running Iceberg on AWS at scale while optimizing cost and performance.

Whether you're just starting out with Iceberg or you're an experienced user looking to optimize your existing Iceberg workloads on AWS, this guide offers valuable insights for every stage of your project.
