---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/introduction.html
---

# Using Apache Iceberg on AWS
<a name="introduction"></a>

*Diego Garcia Garcia and Stefano Sandona, Amazon Web Services*

Apache Iceberg is an open-source table format that simplifies table management while improving performance. AWS analytics services such as Amazon EMR, AWS Glue, Amazon Athena, and Amazon Redshift include native support for Iceberg, so you can easily build transactional data lakes on top of Amazon Simple Storage Service (Amazon S3) on AWS.

In addition, the next generation of Amazon SageMaker is built on an [open lakehouse architecture](https://aws.amazon.com/sagemaker/lakehouse/) that unifies data access across AWS data lakes, data warehouses, and third-party and federated sources. The lakehouse is fully compatible with Iceberg and gives you the flexibility to access and query data in place by using the Iceberg REST API.

This technical guide provides guidance on getting started with Iceberg on different AWS services, and includes best practices and recommendations for running Iceberg on AWS at scale while optimizing cost and performance.

Whether you're just starting out with Iceberg or you're an experienced user looking to optimize your existing Iceberg workloads on AWS, this guide offers valuable insights for every stage of your project.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
