---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/getting-started-overview.html
---

**Experimental**: This documentation covers the AWS SDK for Python v4, which is experimental, non-GA software intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Overview
<a name="getting-started-overview"></a>

This chapter takes you from a new Python environment to two working asynchronous AWS calls. The first example creates a temporary Amazon DynamoDB table, writes and reads an item, and deletes the table. The second sends prerecorded audio to Amazon Transcribe and prints completed transcript segments as they arrive.

Both examples use the same basic workflow:

1. Install only the service client packages that your application needs.

1. Configure how the SDK authenticates with AWS.

1. Create an asynchronous client for the service.

1. Build typed input objects and await the client operation.
