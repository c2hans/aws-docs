---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/welcome.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# What is the AWS SDK for Python?
<a name="welcome"></a>

AWS provides two SDKs for building Python applications on AWS:
+ **AWS SDK for Python (Boto3)** — General Availability. The established, production-ready SDK with synchronous access to all AWS services. Use Boto3 for production workloads. [Boto3 Developer Guide](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html) \| [SDK source](https://github.com/boto/boto3) on GitHub
+ **AWS SDK for Python** — Developer Preview. A next-generation SDK with native asynchronous support, modular per-service packages, and bidirectional HTTP/2 streaming. Use this SDK to evaluate these capabilities and provide feedback in development and test environments only. [SDK source](https://github.com/aws/aws-sdk-python) on GitHub

You can install both SDKs in the same application. Separate Python namespaces allow them to coexist without conflicts.

**Developer Preview**
The AWS SDK for Python is currently in Developer Preview. Use it to evaluate supported features and provide feedback in development and test environments. Do not use it for production workloads. APIs and behavior might change before general availability. Pin package versions and test your application when you upgrade. For guidance on choosing between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

## About this guide
<a name="about-this-guide"></a>

This guide covers the AWS SDK for Python (Developer Preview). It provides native asynchronous service clients designed for [`asyncio`](https://docs.python.org/3/library/asyncio.html), the standard Python library for asynchronous programming, including support for APIs that use bidirectional HTTP/2 streaming. Service clients are distributed as modular packages, so you can install only the clients that your application needs.

## Key features
<a name="key-features"></a>
+ **Native asynchronous APIs**: Service clients use Python `async` and `await` for non-blocking operations and concurrent I/O.
+ **Bidirectional streaming**: Supported clients can send and receive event streams concurrently over HTTP/2.
+ **Modular packages**: Each service client is available as a separate package, reducing the dependencies that you install and deploy.
+ **Generated types**: Generated clients, request and response models, and type annotations provide editor completion and static-analysis support.
+ **Configurable clients**: Configure Regions, endpoints, credential resolvers, retry behavior, plugins, and interceptors for your application.

## Supported services
<a name="supported-services"></a>

The Developer Preview supports a selected and growing set of AWS service clients. It does not yet provide clients for every AWS service or all of the features available in Boto3.

Each supported client is published as a service-specific package whose name begins with `aws-sdk-`. Before you adopt the SDK, verify that the service and operations that your application requires are available. For the current client packages and their release status, see the [AWS SDK for Python repository](https://github.com/aws/aws-sdk-python) on GitHub.

For guidance on supported AWS services, see [Working with AWS services](working-with-services.md).

## Get started with the SDK
<a name="first-time-user"></a>

To begin evaluating the AWS SDK for Python, use the following resources:
+ Follow [Getting started with the AWS SDK for Python](getting-started.md) to install the SDK, configure authentication, and run your first examples.
+ See [Configuration](configuring.md) to configure service clients for your environment.
+ Explore [Using the AWS SDK for Python](using.md) to make requests, use asynchronous operations, handle errors, and customize SDK behavior.

## Additional documentation and resources
<a name="additional-resources"></a>

In addition to this guide, the following are valuable online resources for AWS SDK for Python developers:
+ [AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/): Contains settings, features, and other foundational concepts common to AWS SDKs.
+ GitHub:
  + [SDK source](https://github.com/aws/aws-sdk-python) on GitHub
  + [SDK issues](https://github.com/aws/aws-sdk-python/issues) on GitHub
+ []()
+ [Python developer blog](https://aws.amazon.com/blogs/developer/category/programing-language/python/)
+ The [AWS Code Sample Catalog](https://docs.aws.amazon.com/code-samples/latest/catalog/)
+ [SDK License](https://aws.amazon.com/apache2.0/)

## Maintenance and support for SDK major versions
<a name="sdks-major-versions-maintenance-support"></a>

For information about maintenance and support for SDK major versions and their underlying dependencies, see the following in the [AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/overview.html):
+ [AWS SDKs and tools maintenance policy](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html)
+ [AWS SDKs and tools version support matrix](https://docs.aws.amazon.com/sdkref/latest/guide/version-support-matrix.html)
