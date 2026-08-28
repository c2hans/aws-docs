---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/getting-started-overview.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Overview
<a name="getting-started-overview"></a>

This chapter takes you from a new Python environment to two working asynchronous AWS calls. The first example creates a temporary Amazon DynamoDB table, writes and reads an item, and deletes the table. The second sends prerecorded audio to Amazon Transcribe and prints completed transcript segments as they arrive.

Both examples use the same basic workflow:

1. Install only the service client packages that your application needs.

1. Configure how the SDK authenticates with AWS.

1. Create an asynchronous client for the service.

1. Build typed input objects and await the client operation.

**Note**
The AWS SDK for Python is in Developer Preview. Use it for evaluation in development and test environments, not in production. APIs can change between preview releases, so pin and test the package versions that your application uses.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Python. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-python` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
