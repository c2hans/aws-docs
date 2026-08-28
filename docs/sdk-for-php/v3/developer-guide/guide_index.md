---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_index.html
---

# Configuring service clients in the AWS SDK for PHP Version 3
<a name="guide_index"></a>

To programmatically access AWS services, the AWS SDK for PHP Version 3 uses a client object for each AWS service. For example, if your application needs to access Amazon EC2, you create an Amazon EC2 client object—an instance of the [Ec2Client](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.Ec2.Ec2Client.html) class—to interface with that service. You then use the service client to make requests to that AWS service.

There are many ways to configure SDK behavior, but ultimately everything has to do with the behavior of service clients. Any configuration has no effect until your code creates a service client that uses the configuration.

Examples of the configuration that you provide are:
+ How your code authenticates with AWS when you call a service
+ The AWS Region you want a service client to use
+ Retry and timeout settings for service calls
+ HTTP proxy configuration

Refer to the [AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/) for settings, features, and other foundational concepts common to many of the AWS SDKs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for PHP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-php` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
