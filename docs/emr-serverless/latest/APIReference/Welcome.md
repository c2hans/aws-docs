---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/Welcome.html
---

# Welcome
<a name="Welcome"></a>

Amazon EMR Serverless is a new deployment option for Amazon EMR. Amazon EMR Serverless provides a serverless runtime environment that simplifies running analytics applications using the latest open source frameworks such as Apache Spark and Apache Hive. With Amazon EMR Serverless, you don’t have to configure, optimize, secure, or operate clusters to run applications with these frameworks.

The API reference to Amazon EMR Serverless is `emr-serverless`. The `emr-serverless` prefix is used in the following scenarios:
+ It is the prefix in the CLI commands for Amazon EMR Serverless. For example, `aws emr-serverless start-job-run`.
+ It is the prefix before IAM policy actions for Amazon EMR Serverless. For example, `"Action": ["emr-serverless:StartJobRun"]`. For more information, see [Policy actions for Amazon EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-actions).
+ It is the prefix used in Amazon EMR Serverless service endpoints. For example, `emr-serverless.us-east-2.amazonaws.com`.

This document was last published on September 1, 2026.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
