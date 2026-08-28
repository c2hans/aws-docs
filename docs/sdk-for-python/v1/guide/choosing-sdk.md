---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/choosing-sdk.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Choosing the right AWS SDK for Python
<a name="choosing-sdk"></a>

AWS offers two SDKs for Python developers. This page helps you understand the differences and choose the right SDK for your needs.

## Overview
<a name="choosing-sdk-overview"></a>

**Boto3** is the established, production-ready AWS SDK for Python with full coverage of all AWS services. It has been the standard for Python developers building on AWS for years and remains fully supported.

**AWS SDK for Python (Developer Preview)** is the next-generation SDK covered in this guide, rebuilt from the ground up with an async-first, modular architecture. It is currently in Developer Preview for evaluation and early feedback, and is not intended for production use.

Boto3 is generally available and recommended for production workloads. The AWS SDK for Python is in Developer Preview and intended for evaluation and testing only, it is not yet production-ready. Both SDKs coexist in the same project without conflicts, and you can use either or both based on your requirements.

## Key differences
<a name="choosing-sdk-differences"></a>

| Capability | **Boto3** | **AWS SDK for Python (Developer Preview)** |
| --- | --- | --- |
| Release status | General Availability (GA) | Developer Preview |
| Production use | Yes | Not recommended |
| Architecture | Synchronous, monolithic package | Async-first, modular per-service packages |
| Async support | Via community wrappers (aiobotocore/aioboto3) | Native async/await with asyncio |
| Packaging | Single boto3 package for all services | Per-service packages (e.g., aws-sdk-dynamodb) |
| HTTP/2 streaming | Not supported | Native bidirectional event streaming |
| Service coverage | All AWS services | 24 services (expanding) |
| Paginators & waiters | Available | Coming soon |
| Presigned URLs | Available | Coming soon |
| S3 Transfer Manager | Available | Coming soon |
| Synchronous client | Default mode | Coming soon |
| Credential support | Full (SSO, Web Identity, etc.) | Default credential chain (SSO, Web Identity coming soon) |
| Code generation | Partial | Fully auto-generated from Smithy service models |

## Decision guide
<a name="choosing-sdk-decision"></a>

### Choose Boto3 if you:
<a name="choosing-sdk-boto3"></a>
+ **Need production stability** — Boto3 is battle-tested, GA, and backed by complete AWS service coverage.
+ **Require services not yet in the Developer Preview** — If your application depends on services beyond the current 24, Boto3 is your path.
+ **Run synchronous workloads** — If your application doesn't have concurrency performance bottlenecks, Boto3's synchronous model is mature and well-suited.
+ **Need full credential provider support** — If you rely on SSO via IAM Identity Center or Web Identity (EKS/GitHub Actions OIDC).
+ **Depend on paginators, waiters, or presigned URLs** — These features are not yet available in the Developer Preview.

### Choose AWS SDK for Python (Developer Preview) if you:
<a name="choosing-sdk-python-sdk"></a>
+ **Are building high-throughput async applications** — Native async/await with asyncio eliminates the overhead of community wrappers and delivers true concurrency for multiple simultaneous AWS service calls.
+ **Work with streaming services** — Bedrock Runtime, Transcribe Streaming, and SageMaker Runtime are designed for async, and the new SDK's HTTP/2 bidirectional streaming support provides first-class handling.
+ **Need minimal deployment size** — Per-service packages (e.g., `aws-sdk-dynamodb`) with granular dependencies help you stay within AWS Lambda deployment size limits.
+ **Want to influence SDK direction** — Developer Preview feedback directly shapes feature prioritization and the GA release.
+ **Are evaluating for future migration** — Getting familiar with the new SDK's API patterns early helps you plan a smooth transition.

### Use both SDKs together if you:
<a name="choosing-sdk-both"></a>
+ Want to use the new SDK for async workloads (e.g., Bedrock streaming) while relying on Boto3 for everything else.
+ Are incrementally evaluating the new SDK in non-production paths while maintaining Boto3 for production code.
+ Need services from both SDKs in the same application.

**Important**
When using both SDKs together, be aware that mixing synchronous Boto3 calls inside an async event loop can block the loop and negate the performance benefits of async. Keep sync and async code paths separated. Refer to the [Working with Boto3](working-with-boto3.md) page for additional details.

## Services available in the Developer Preview
<a name="choosing-sdk-services"></a>

The Developer Preview currently supports 24 service clients, including:
+ Amazon Bedrock & Bedrock Runtime
+ Amazon DynamoDB
+ AWS Lambda
+ Amazon SQS
+ Amazon SNS
+ AWS STS
+ Amazon Transcribe Streaming
+ Amazon SageMaker Runtime
+ And more — see the [aws-sdk-python repository](https://github.com/aws/aws-sdk-python) on GitHub for the full list

## What's coming next
<a name="choosing-sdk-coming-next"></a>

The AWS SDK for Python is being developed incrementally. Planned additions include:
+ **Expanded service coverage** — Support for Amazon S3 and additional AWS services.
+ **Complete credential chain** — SSO via IAM Identity Center, Web Identity, AWS Login, process credentials, and SigV4a multi-region signing.
+ **Core SDK features** — Paginators, waiters, presigned URLs, S3 Transfer Manager, and synchronous client support.
+ **Observability** — Adaptive retries, logging, metrics, OpenTelemetry tracing, proxy configuration, and connection pooling.

## Lifecycle and support
<a name="choosing-sdk-lifecycle"></a>

| Question | Answer |
| --- | --- |
| Is Boto3 being retired? | Not until the new SDK reaches feature parity with Boto3's synchronous support. AWS will provide ample notice, migration guidance, and support throughout any transition. |
| When will the new SDK reach GA? | The GA release will be informed by Developer Preview feedback. No date has been set. |
| Can I use the Developer Preview in production? | No. It is intended for evaluation and testing in pre-production environments only. |
| Will both SDKs be supported simultaneously? | Yes. Both SDKs are fully supported, and you can confidently choose the one that best meets your current needs. |

## Getting started
<a name="choosing-sdk-getting-started"></a>
+ **Boto3**: [Developer Guide](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html) \| [SDK source](https://github.com/boto/boto3) on GitHub
+ **AWS SDK for Python (Developer Preview)**: [Getting started with the AWS SDK for Python](getting-started.md) \| [SDK source](https://github.com/aws/aws-sdk-python) on GitHub

## Feedback
<a name="choosing-sdk-feedback"></a>

We want your feedback to guide feature prioritization and service coverage. File issues in the [aws-sdk-python repository](https://github.com/aws/aws-sdk-python/issues) on GitHub, or reach out through AWS Support.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Python. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-python` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
