---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/getting-started-overview.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Overview
<a name="getting-started-overview"></a>

This chapter takes you from a new Python environment to two working AWS examples. The first example uses a synchronous client to create a temporary Amazon DynamoDB table, write and read an item, and delete the table. The second example uses an asynchronous client to send prerecorded audio to Amazon Transcribe and print completed transcript segments as they arrive.

Both examples use the same basic workflow:

1. Install only the service client packages that your application needs.

1. Configure how the SDK authenticates with AWS.

1. Create a client for the service.

1. Call the client's operations with keyword arguments. With an asynchronous client, you also `await` each call.
