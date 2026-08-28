---
source_url: https://docs.aws.amazon.com/braket/latest/developerguide/braket-using-boto3.html
---

# Working with AWS Boto3
<a name="braket-using-boto3"></a>

Boto3 is the AWS SDK for Python. With Boto3, Python developers can create, configure, and manage AWS services, such as Amazon Braket. Boto3 provides an object-oriented API, as well as low-level access to Amazon Braket.

Follow the instructions in the [Boto3 Quickstart guide](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) to learn how to install and configure Boto3.

Boto3 provides the core functionality that works along with the Amazon Braket Python SDK to help you configure and run your quantum tasks. Python customers always need to install Boto3, because that is the core implementation. If you want to make use of additional helper methods, you also need to install the Amazon Braket SDK.

For example, when you call `CreateQuantumTask`, the Amazon Braket SDK submits the request to Boto3, which then calls the AWS API.

**Topics**
+ [Turn on the Amazon Braket Boto3 client](braket-using-boto3-client.md)
+ [Configure AWS CLI profiles for Boto3 and the Braket SDK](braket-using-boto3-profiles.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Braket. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query braket` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
