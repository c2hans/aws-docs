---
source_url: https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-nova-capabilities.html
---

# Using Amazon Nova 2 capabilities
<a name="using-nova-capabilities"></a>

This guide provides task-based recipes and practical examples to help you integrate Nova's capabilities into your applications quickly and effectively. It is designed for developers and engineers who want to:
+ Integrate Nova models into their applications via API
+ Understand preprocessing requirements and optimization strategies
+ Implement multimodal understanding workflows

Each section provides:
+ Key technical information about supported formats, size limits, and token estimation
+ Code examples that demonstrate how to use API with both direct upload and Amazon S3
+ Use cases that show practical applications
+ Limitations to consider when designing your application

**Prerequisites**

Before you begin, ensure you have:
+ An AWS account with access to Amazon Bedrock
+ Appropriate IAM permissions for invoking Bedrock models
+ AWS SDK installed (Boto3 for Python examples)
+ Basic familiarity with AWS services, such as Amazon S3 (for large file handling)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
