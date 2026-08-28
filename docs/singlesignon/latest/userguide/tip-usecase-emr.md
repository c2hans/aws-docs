---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/tip-usecase-emr.html
---

# Trusted identity propagation with Amazon EMR
<a name="tip-usecase-emr"></a>

The following diagram shows a trusted identity propagation configuration for Amazon EMR Studio using Amazon EMR on Amazon EC2 with access control provided by AWS Lake Formation and Amazon S3 Access Grants.

![Diagram of trusted identity propagation using Amazon EMR, Lake Formation, and IAM Identity Center](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/emr-tip-diagram.png)

**Supported client-facing applications**
+ Amazon EMR Studio

**To enable trusted identity propagation, follow these steps:**
+ [Set up Amazon EMR Studio](setting-up-tip-emr.md) as the client-facing application for Amazon EMR cluster.
+ Set up [Amazon EMR Cluster on Amazon EC2 with Apache Spark](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-idc-start.html).
+ *Recommended*: [AWS Lake Formation](tip-tutorial-lf.md) and [Amazon S3 Access Grants](tip-tutorial-s3.md) to provide fine-grained access control to AWS Glue Data Catalog and underlying data locations in S3.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
