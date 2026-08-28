---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-aws-data/aws-architecture.html
---

# AWS modern data architecture
<a name="aws-architecture"></a>

This guide doesn't describe how to implement a data strategy framework on AWS. That is an extensive topic that is covered in AWS documentation, blog posts, and other guides (see the *Resources* section). However, the following diagram provides a high-level overview. It illustrates the main components of a [modern data architecture on AWS](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/modern-data-architecture.html) and covers most of the services that can be in your roadmap.

![AWS data services](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-aws-data/images/guide-img/7eadad47-3e6a-4775-bcac-a88d1e364e51/images/4a390be6-431c-41b1-bbb2-2435a2e369da.png)

The main components of this architecture support the technical tenets for a modern data strategy that were [discussed earlier](data-strategy-framework.md):

1. Use an integrated, **cost-effective, and scalable storage layer**, so every data producer and consumer has the technical capabilities to interact with data.

   [Amazon Simple Storage Service (Amazon S3](https://aws.amazon.com/s3/)) is an object storage service that provides integration, scalability, data availability, security, and performance at a low cost.

1. **Security is mandatory**. Apply data privacy rules, provide data protection with encryption, enable auditing, and provide automated compliance.

   To apply data privacy, protection, and compliance in an automated manner, and to enable auditing, you can use [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms/), [AWS Identity and Access Management (IAM](https://aws.amazon.com/iam/)), [AWS Secrets Manager](https://aws.amazon.com/secrets-manager), [AWS Audit Manager](https://aws.amazon.com/audit-manager/), and [Amazon Macie](https://aws.amazon.com/macie/).

1. **Govern the data to share** it across the company. Provide a unique data catalog and a business glossary so users can find and use the data they need.

   [AWS Lake Formation](https://aws.amazon.com/lake-formation/) helps you govern data and share it across the company. In addition, you can create a unique data catalog on [AWS Glue](https://aws.amazon.com/glue/) and a business glossary by using [Amazon DataZone](https://aws.amazon.com/datazone/) (in preview) to enable your employees to find the data they need.

1. Select the **right service for the right job.** Consider functionality, scalability, data latency, the effort required to run the service, resilience, integration, and automation when you choose a component.

   You can consider [Amazon Athena](https://aws.amazon.com/athena/), [Amazon EMR](https://aws.amazon.com/emr/), [AWS Glue](https://aws.amazon.com/glue/), [Amazon OpenSearch Service](https://aws.amazon.com/what-is/opensearch), [Amazon Kinesis](https://aws.amazon.com/kinesis/), [Amazon Redshift](https://aws.amazon.com/redshift/), [Amazon Managed Streaming for Apache Kafka (Amazon MSK](https://aws.amazon.com/msk/)), and [Amazon Quick](https://aws.amazon.com/quicksuite/) to manage your tasks. For example, you can perform real-time streaming with Kinesis or Amazon MSK, data processing with Amazon EMR or AWS Glue, search with Amazon OpenSearch, ad-hoc queries with Athena, and data warehousing with Amazon Redshift.

1. Use **artificial intelligence (AI)** and **machine learning (ML)**.

   You can enable the usage of artificial intelligence with [AWS AI services](https://aws.amazon.com/machine-learning/ai-services/) and machine learning with** **[Amazon SageMaker](https://aws.amazon.com/sagemaker/)**.**

1. Provide **data literacy** and tools with **abstraction for business people**.

   Processes for providing data literacy, tools, and abstractions aren't part of the architecture, but you can use [Amazon DataZone](https://aws.amazon.com/datazone/) (in preview), [AWS Lake Formation](https://aws.amazon.com/lake-formation/), and [Amazon QuickSight](https://aws.amazon.com/quicksight/) as data abstraction tools.

1. **Test the hypotheses** of your data initiatives and **measure their results**.

   You can use the [Amazon OpenSearch Service](https://aws.amazon.com/what-is/opensearch) dashboard or [Amazon Quick](https://aws.amazon.com/quicksuite/) to work with business outcome metrics and test results, and validate your hypotheses.

For examples of sample architectures for different use cases, see the reference architecture diagrams in the [AWS Architecture Center](https://aws.amazon.com/architecture/). Your technical team should use these diagrams for reference only and customize them based on your own requirements, environments, and projects.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
