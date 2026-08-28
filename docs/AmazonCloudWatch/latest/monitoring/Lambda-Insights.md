---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights.html
---

# Lambda Insights
<a name="Lambda-Insights"></a>

CloudWatch Lambda Insights is a monitoring and troubleshooting solution for serverless applications running on AWS Lambda. The solution collects, aggregates, and summarizes system-level metrics including CPU time, memory, disk, and network. It also collects, aggregates, and summarizes diagnostic information such as cold starts and Lambda worker shutdowns to help you isolate issues with your Lambda functions and resolve them quickly.

Lambda Insights uses a new CloudWatch Lambda extension, which is provided as a Lambda layer. When you install this extension on a Lambda function, it collects system-level metrics and emits a single performance log event for every invocation of that Lambda function. CloudWatch uses embedded metric formatting to extract metrics from the log events.

**Note**
The Lambda Insights agent is supported only on Lambda runtimes that use Amazon Linux 2 and Amazon Linux 2023.

For more information about Lambda extensions, see [ Using AWS Lambda extensions](https://docs.aws.amazon.com/lambda/latest/dg/using-extensions.html). For more information about embedded metric format, see [Embedding metrics within logs](CloudWatch_Embedded_Metric_Format.md).

You can use Lambda Insights with any Lambda function that uses a Lambda runtime that supports Lambda extensions. For a list of these runtimes, see [ Lambda Extensions API](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-extensions-api.html).

**Pricing**

For each Lambda function enabled for Lambda Insights, you only pay for what you use for metrics and logs. For a pricing example, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

You are charged for the execution time consumed by the Lambda extension, in 1ms increments. For more information about Lambda pricing, see [AWS Lambda Pricing](https://aws.amazon.com/lambda/pricing/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
