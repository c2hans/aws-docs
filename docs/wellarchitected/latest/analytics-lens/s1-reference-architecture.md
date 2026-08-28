---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/s1-reference-architecture.html
---

# Reference architecture
<a name="s1-reference-architecture"></a>

 The following diagram illustrates the solution architecture and its key components for data cataloging, security, compliance, and data access requirements using DataHub.

![Reference architecture for data discovery](http://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/images/scenario-1-ref.png)

1.  DataHub is an open-source metadata management platform which enables end-to-end discovery, data observability, data governance , data lineage and many more. It runs on an Amazon EKS cluster, using Amazon OpenSearch Service, Amazon Managed Streaming for Apache Kafka (Amazon MSK), and RDS for MySQL as the storage layer for the underlying data model and indexes.

1.  Pull technical metadata from AWS Glue and Amazon Redshift to DataHub.

1.  Enrich the technical metadata with a business glossary.

1.  Run an AWS Glue job to transform the data and observe the data lineage in DataHub.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
