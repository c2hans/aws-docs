---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/using.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Using the AWS SDK for Python v4
<a name="using"></a>

This chapter describes programming patterns that apply to every AWS service that the SDK supports. It goes beyond the examples in [Getting started with the AWS SDK for Python v4](getting-started.md). For service-specific operations, see [Working with AWS services](working-with-services.md).

Most examples use the synchronous client. Topics about asynchronous programming, concurrency, and event streams use the asynchronous client. For how the two clients differ, see [Synchronous and asynchronous clients](using-sync-async.md).

Before using these patterns, configure credentials and an AWS Region as described in [Configuration](configuring.md).

**Topics**
+ [Synchronous and asynchronous clients](using-sync-async.md)
+ [Making requests and handling responses](using-requests.md)
+ [Using the SDK asynchronously](using-async.md)
+ [Running concurrent operations](using-concurrency.md)
+ [Working with event streams](using-streaming.md)
+ [Handling errors](using-errors.md)
+ [Customizing SDK behavior with plugins and interceptors](using-extensions.md)
+ [Testing applications that use the SDK](using-testing.md)
