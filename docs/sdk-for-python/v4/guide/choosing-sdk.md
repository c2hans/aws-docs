---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/choosing-sdk.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Choosing the right AWS SDK for Python

AWS provides two SDKs for building Python applications on AWS. This page compares them to help you choose the right SDK for your needs.

## Overview
<a name="choosing-sdk-overview"></a>
+ **AWS SDK for Python (Boto3)**: This SDK is generally available and provides synchronous clients for all AWS services. Use it for production workloads.
+ **AWS SDK for Python v4**: This SDK is in Developer Preview. Each service package includes a synchronous and an asynchronous client. The asynchronous clients also support bidirectional HTTP/2 streaming. Use this SDK only in development and test environments to evaluate these capabilities and provide feedback.

You can install both SDKs in the same application. They use separate Python namespaces, so they don't conflict.

## Key differences
<a name="choosing-sdk-differences"></a>

| Capability | AWS SDK for Python (Boto3) | AWS SDK for Python v4 |
| --- | --- | --- |
| Release status | Generally available | Developer Preview |
| Production use | Yes | No |
| Synchronous clients | Yes | Available in every service package |
| Asynchronous support | Through community wrappers, such as aiobotocore and aioboto3 | Native async and await with asyncio |
| Packaging | Single boto3 package for all services | Per-service packages (for example, aws-sdk-dynamodb) |
| HTTP/2 streaming | Not supported | Bidirectional HTTP/2 event streaming in asynchronous clients |
| Service coverage | All AWS services | A subset of AWS services |
| Paginators and waiters | Available | Not yet available |
| Presigned URLs | Available | Not yet available |
| Amazon S3 Transfer Manager | Available | Not yet available |
| Credential support | All standard credential sources, including IAM Identity Center and web identity | Environment variables, shared config and credentials files, process, and static credentials. Optional packages add container, instance metadata, assume role, and web identity credentials. IAM Identity Center and console sign-in credentials aren't supported yet. |
| Code generation | Partial | Fully generated from Smithy service models |

## Decision guide
<a name="choosing-sdk-decision"></a>

Choose AWS SDK for Python (Boto3) if any of the following apply:
+ **Your workload runs in production.** Boto3 is generally available and widely used in production.
+ **Your application uses a service that the Developer Preview doesn't support yet.** Boto3 supports every AWS service.
+ **Your application gets credentials from IAM Identity Center or console sign-in.** The Developer Preview doesn't support these sources yet.
+ **Your application depends on paginators, waiters, presigned URLs, or the Amazon S3 Transfer Manager.** The Developer Preview doesn't provide these features yet.

Choose the AWS SDK for Python v4 if any of the following apply:
+ **You want to write synchronous code, asynchronous code, or both.** Each service package includes both client types.
+ **You're building an `asyncio` application that makes many concurrent AWS calls.** The asynchronous clients use native `async` and `await`, without a community wrapper.
+ **You use bidirectional streaming operations, such as those in Amazon Transcribe, Amazon Bedrock Runtime, and Amazon SageMaker Runtime.** The asynchronous clients support bidirectional event streams over HTTP/2.
+ **You need a small deployment, for example to stay within AWS Lambda deployment package size limits.** You install only the service packages that you use, such as `aws-sdk-dynamodb`.
+ **You want to influence the SDK before general availability.** We use feedback on the Developer Preview to prioritize features for the GA release.
+ **You're planning a future migration from Boto3.** Trying the new SDK's API patterns now helps you plan that migration.

Use both SDKs together if any of the following apply:
+ You want to use the new SDK for streaming workloads, such as Amazon Bedrock Runtime streaming, and Boto3 for everything else.
+ You're evaluating the new SDK in non-production code paths and keeping Boto3 for production code.
+ Your application needs services from both SDKs.

**Note**
If you use both SDKs together, don't make synchronous calls from code that runs in an `asyncio` event loop. A synchronous call, from Boto3 or from a synchronous client in this SDK, blocks the event loop until it returns. Keep synchronous and asynchronous code paths separate. For more information, see [Working with AWS SDK for Python (Boto3)](working-with-boto3.md).

## Services available in the Developer Preview
<a name="choosing-sdk-services"></a>

The Developer Preview provides clients for a subset of AWS services, including the following:
+ Amazon S3
+ Amazon EC2
+ Amazon DynamoDB
+ Amazon Bedrock and Amazon Bedrock Runtime
+ AWS Lambda
+ Amazon SQS
+ Amazon SNS
+ AWS STS
+ AWS Sign-In
+ Amazon Transcribe Streaming
+ Amazon SageMaker Runtime

For the full list of clients, see the [aws-sdk-python repository](https://github.com/aws/aws-sdk-python) on GitHub.

## What's coming next
<a name="choosing-sdk-coming-next"></a>

AWS is developing the AWS SDK for Python v4 incrementally. Planned additions include the following:
+ Clients for additional AWS services.
+ More credential sources, including IAM Identity Center and console sign-in credentials from the **aws login** command.
+ SigV4a signing for multi-Region requests.
+ Paginators, waiters, presigned URLs, and the Amazon S3 Transfer Manager.
+ Observability features, including logging, metrics, and OpenTelemetry tracing.
+ More HTTP client settings, including timeouts, connection pooling, and proxy configuration.

## Lifecycle and support
<a name="choosing-sdk-lifecycle"></a>

| Question | Answer |
| --- | --- |
| Is AWS SDK for Python (Boto3) being retired? | Not until the new SDK reaches feature parity with the synchronous support in Boto3. We will provide ample notice, migration guidance, and support throughout any transition. |
| When will the new SDK reach GA? | We haven't set a date. Feedback on the Developer Preview informs the GA release. |
| Can I use the Developer Preview in production? | No. It is intended for evaluation and testing in pre-production environments only. |
| Will both SDKs be supported simultaneously? | Yes. Both SDKs are supported. You can choose the one that meets your current needs. |

## Getting started
<a name="choosing-sdk-getting-started"></a>
+ To get started with AWS SDK for Python (Boto3), see the [*Boto3 Developer Guide*](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html) and the [Boto3 source](https://github.com/boto/boto3) on GitHub.
+ To get started with the AWS SDK for Python v4, see [Getting started with the AWS SDK for Python v4](getting-started.md) and the [SDK source](https://github.com/aws/aws-sdk-python) on GitHub.

## Feedback
<a name="choosing-sdk-feedback"></a>

Your feedback guides feature prioritization and service coverage. File issues in the [aws-sdk-python repository](https://github.com/aws/aws-sdk-python/issues) on GitHub, or reach out through AWS Support.
