---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/lambda.html
---

# AWS Lambda
<a name="lambda"></a>

[AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. For securing your environment variables, you can use server-side encryption to protect your data at rest and client-side encryption to protect your data in transit.

Consider the following encryption best practices for this service:
+ Lambda always provides server-side encryption at rest with an AWS KMS key. By default, Lambda uses an AWS managed key. We recommend you use a customer managed key because you have full control over the key, including management, rotation, and auditing.
+ For data in transit that requires encryption, enable helpers, which ensures that environment variables are encrypted client-side for protection in transit by using the preferred KMS key. For more information, see *Security in transit* in [Securing environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-encryption).
+ Lambda function environment variables that hold sensitive or critical data should be encrypted in transit to help protect the data that is dynamically passed to the functions (usually access information) from unauthorized access.
+ To prevent a user from viewing environment variables, add a statement to the user's permissions in the IAM policy or to the key policy that denies access to the default key, a customer managed key, or all keys. For more information, see [Using AWS Lambda environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
