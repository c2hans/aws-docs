---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/agent-tutorial-prereq.html
---

# Prerequisites
<a name="agent-tutorial-prereq"></a>

Before you begin this tutorial, make sure you have the following:
+ AWS account with the following managed policies:
  + [AmazonBedrockFullAccess](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonBedrockFullAccess)
  + [AWSLambda\_FullAccess](https://docs.aws.amazon.com/lambda/latest/dg/security-iam-awsmanpol.html#lambda-security-iam-awsmanpol-AWSLambda_FullAccess)
  + [IAMFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/IAMFullAccess.html)
**Important**
These permissions allow you to run this tutorial and other, unrelated, tasks. In production environments be sure to assign only those permissions that your users need to run your application.
+ Basic understanding of IAM roles and permissions ([IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html))
+ Familiarity with AWS Lambda functions ([Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html))

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
