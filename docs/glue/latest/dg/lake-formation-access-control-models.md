---
source_url: https://docs.aws.amazon.com/glue/latest/dg/lake-formation-access-control-models.html
---

# AWS Lake Formation access control models
<a name="lake-formation-access-control-models"></a>

AWS Glue 5.0 and above supports two models for accessing data through AWS Lake Formation:

**Topics**
+ [Using AWS Glue with AWS Lake Formation for Full Table Access](security-access-control-fta.md)
+ [Using AWS Glue with AWS Lake Formation for fine-grained access control](security-lf-enable.md)

The following table describes summary of how to choose between Fine-grained access control (FGAC) and Full table access (FTA) for your workload.

| Feature | Fine-grained access control (FGAC) | Full table access (FTA) |
| --- |--- |--- |
| Access Level | Column/row level | Full table |
| Use Case | Queries and ETL with limited permissions | ETL |
| Performance Impact | Requires system/user space transitions for access control evaluation, adding latency | Optimized performance |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
