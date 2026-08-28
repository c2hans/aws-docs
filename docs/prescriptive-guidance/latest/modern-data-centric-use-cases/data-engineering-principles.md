---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-centric-use-cases/data-engineering-principles.html
---

# Data engineering principles
<a name="data-engineering-principles"></a>

We recommend that you adopt the principles in the following table when you build an architecture for a modern data pipeline.

|
|
| Principle | Example | Use case |
| --- |--- |--- |
| Flexibility | Use microservices | [FastGo enjoys flexibility and scalability with a microservices architecture on AWS](https://aws.amazon.com/solutions/case-studies/fastgo/) (AWS case study) |
| Reproducibility | Use infrastructure as code (IaC) to deploy your services | [Part 3: How NatWest Group built auditable, reproducible, and explainable ML models with Amazon SageMaker](https://aws.amazon.com/blogs/machine-learning/part-3-how-natwest-group-built-auditable-reproducible-and-explainable-ml-models-with-amazon-sagemaker/) (AWS Machine Learning Blog) |
| Reusability | Use libraries and references in a shared manner | [Create and reuse governed datasets in Amazon QuickSight with new Dataset-as-a-Source feature](https://aws.amazon.com/blogs/big-data/create-and-reuse-governed-datasets-in-amazon-quicksight-with-new-dataset-as-a-source-feature/) (AWS Big Data Blog) |
| Scalability | Choose service configurations to accommodate any data load | [Designing a data lake for growth and scale on the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/data-lake-for-growth-scale/welcome.html) (AWS Prescriptive Guidance) |
| Auditability | Keep an audit trail by using logs, versions, and dependencies | [How Parametric Built Audit Surveillance using AWS Data Lake Architecture](https://aws.amazon.com/blogs/architecture/how-parametric-built-audit-surveillance-using-aws-data-lake-architecture/) (AWS Architecture Blog) |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
