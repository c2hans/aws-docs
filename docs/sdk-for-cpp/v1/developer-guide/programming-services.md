---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/programming-services.html
---

# Guided examples for calling AWS services using the AWS SDK for C\+\+
<a name="programming-services"></a>

If you are new to AWS or the AWS code examples, we recommend you start with [Getting started on code examples](getting-started-code-examples.md).

Source code that shows how to work with AWS services using the AWS SDK for C\+\+ is available in the [Code examples](cpp_code_examples.md) chapter of this guide or directly in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code) on GitHub.

This section selects several AWS services and guides you through the examples using them. The following guided examples are a subset of what is available on Github.

**Service examples with additional explanation (see [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code) for full list)**

| Service | Summary of what the service provides to your program |
| --- | --- |
| [Amazon CloudWatch](examples-cloudwatch.md) | Collects and monitors metrics for AWS resources you are using |
| [Amazon DynamoDB](examples-dynamodb.md) | A NoSQL database service |
| [Amazon Elastic Compute Cloud](examples-ec2.md) (Amazon EC2) | Secure, resizable compute capacity |
| [Amazon Simple Storage Service](examples-s3.md) (Amazon S3) | Data storage and retrieval (objects into buckets) |
| [Amazon Simple Queue Service](examples-sqs.md) (Amazon SQS) | Message queuing service to send, store, and receive messages between software components |

There are also examples that show how to use [Asynchronous methods](async-methods.md).

To propose a new code example to the AWS documentation team, see [Contributing guidelines](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/CONTRIBUTING.md) on GitHub to create a new request. The team prefers to create code examples that show broad scenarios rather than individual API calls.

**Using the Code Examples on Windows**

If you are building the examples on Windows with SDK version 1.9, see [Troubleshooting AWS SDK for C\+\+ build issues](troubleshooting-cmake.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for C++. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-cpp` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
