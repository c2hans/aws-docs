---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/cw-examples.html
---

# Amazon CloudWatch examples using the AWS SDK for PHP Version 3
<a name="cw-examples"></a>

Amazon CloudWatch (CloudWatch) is a web service that monitors your Amazon Web Services resources and the applications you run on AWS in real time. You can use CloudWatch to collect and track metrics, which are variables you can measure for your resources and applications. CloudWatch alarms send notifications or automatically make changes to the resources you are monitoring based on rules that you define.

All the example code for the AWS SDK for PHP is available [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code).

## Credentials
<a name="examplecredentials"></a>

Before running the example code, configure your AWS credentials, as described in [Authenticating with AWS using AWS SDK for PHP Version 3](credentials.md). Then import the AWS SDK for PHP, as described in [Installing the AWS SDK for PHP Version 3](getting-started_installation.md).

**Topics**
+ [Credentials](#examplecredentials)
+ [Working with Amazon CloudWatch alarms](cw-examples-work-with-alarms.md)
+ [Getting metrics from CloudWatch](cw-examples-getting-metrics.md)
+ [Publishing custom metrics in Amazon CloudWatch](cw-examples-publishing-custom-metrics.md)
+ [Sending events to Amazon CloudWatch events](cw-examples-sending-events.md)
+ [Using alarm actions with Amazon CloudWatch alarms](cw-examples-using-alarm-actions.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for PHP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-php` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
