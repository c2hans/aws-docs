---
source_url: https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/security_iam_fgac-lf.html
---

# Using Amazon EMR on EKS with AWS Lake Formation for fine-grained access control
<a name="security_iam_fgac-lf"></a>

With Amazon EMR release 7.7 and higher, you can leverage AWS Lake Formation to apply fine-grained access controls on AWS Glue Data Catalog tables that are backed by Amazon S3 buckets. This capability lets you configure table, row, column, and cell-level access controls for read and write queries within your Amazon EMR on EKS Spark Jobs.

**Topics**
+ [How Amazon EMR on EKS works with AWS Lake Formation](security_iam_fgac-lf-works.md)
+ [Enable Lake Formation with Amazon EMR on EKS](security_iam_fgac-lf-enable.md)
+ [Considerations and limitations](security_iam_fgac-considerations.md)
+ [Troubleshooting](security_iam_fgac-troubleshooting.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
