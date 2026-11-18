---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/welcome.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# What is the AWS SDK for Python v4?
<a name="welcome"></a>

The AWS SDK for Python v4 is a set of Python packages for calling AWS services from your applications. It's the successor to the AWS SDK for Python (Boto3) and is in Developer Preview. Until it's generally available, use Boto3 for production workloads.

To compare the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

## About this guide
<a name="about-this-guide"></a>

This guide explains how to install, configure, and use the AWS SDK for Python v4.

The examples in this guide use synchronous clients unless a feature requires an asynchronous client. To compare the two client types, see [Synchronous and asynchronous clients](using-sync-async.md).

## Key features
<a name="key-features"></a>
+ **Synchronous and asynchronous clients.** Every service package includes a synchronous client, such as `DynamoDBClient`, and an asynchronous client, such as `AsyncDynamoDBClient`.
+ **Bidirectional streaming.** Asynchronous clients for supported services, such as Amazon Transcribe Streaming, send and receive event streams concurrently over HTTP/2.
+ **Modular packages.** Each service client is a separate package, so you install and deploy only the dependencies that your application uses.
+ **Generated types.** The SDK generates each client and its data types from the service's Smithy model. Operations take keyword arguments named after the request members. Each operation returns a typed output object instead of a dictionary.
+ **Configurable clients.** You can set the AWS Region, credential resolver, retry behavior, plugins, and interceptors for each client. Each client resolves its endpoint locally from the service's endpoint rules. You can set a custom endpoint when you need one.

## Supported services
<a name="supported-services"></a>

The Developer Preview provides clients for a subset of AWS services, including Amazon S3, Amazon EC2, Amazon DynamoDB, Amazon Bedrock Runtime, Amazon Simple Queue Service (Amazon SQS), AWS Lambda, and Amazon Transcribe Streaming. It doesn't yet support every AWS service or every feature available in Boto3.

Each client is a separate package whose name begins with `aws-sdk-`, such as `aws-sdk-dynamodb`. Before you adopt the SDK, verify that the service and operations that your application requires are available. For the current client packages and their release status, see the [AWS SDK for Python v4 repository](https://github.com/aws/aws-sdk-python) on GitHub.

For examples that use specific AWS services, see [Working with AWS services](working-with-services.md).

## Get started with the SDK
<a name="first-time-user"></a>

To begin evaluating the AWS SDK for Python v4, use the following resources:
+ Follow [Getting started with the AWS SDK for Python v4](getting-started.md) to install the SDK, configure authentication, and run your first examples.
+ See [Configuration](configuring.md) to configure service clients for your environment.
+ Explore [Using the AWS SDK for Python v4](using.md) to make requests, choose between synchronous and asynchronous clients, handle errors, and customize SDK behavior.

## Additional documentation and resources
<a name="additional-resources"></a>

In addition to this guide, the following online resources are available to AWS SDK for Python v4 developers:
+ [AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/)
+ [SDK source](https://github.com/aws/aws-sdk-python) on GitHub
+ [SDK issues](https://github.com/aws/aws-sdk-python/issues) on GitHub
+ [AWS SDK for Python v4 API Reference](https://docs.aws.amazon.com/sdk-for-python/v4/reference/)
+ [Python developer blog](https://aws.amazon.com/blogs/developer/category/programing-language/python/)
+ [AWS Code Sample Catalog](https://docs.aws.amazon.com/code-samples/latest/catalog/)
+ [SDK License](https://aws.amazon.com/apache2.0/)

## Maintenance and support for SDK major versions
<a name="sdks-major-versions-maintenance-support"></a>

For information about maintenance and support for SDK major versions and their underlying dependencies, see the following in the [AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/overview.html):
+ [AWS SDKs and tools maintenance policy](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html)
+ [AWS SDKs and tools version support matrix](https://docs.aws.amazon.com/sdkref/latest/guide/version-support-matrix.html)
