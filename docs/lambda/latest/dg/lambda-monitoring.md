---
source_url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-monitoring.html
---

# Monitoring, debugging, and troubleshooting Lambda functions
<a name="lambda-monitoring"></a>

AWS Lambda integrates with other AWS services to help you monitor and troubleshoot your Lambda functions. Lambda automatically monitors Lambda functions on your behalf and reports metrics through Amazon CloudWatch. To help you monitor your code when it runs, Lambda automatically tracks the number of requests, the invocation duration per request, and the number of requests that result in an error.

You can use other AWS services to troubleshoot your Lambda functions. This section describes how to use these AWS services to monitor, trace, debug, and troubleshoot your Lambda functions and applications. For details about function logging and errors in each runtime, see individual runtime sections. Topics include [application monitoring](applications-console-monitoring.md), [Application Signals](monitoring-application-signals.md), and [logging Lambda API calls with CloudTrail](logging-using-cloudtrail.md).

**Topics**
+ [Pricing](#monitoring-console-metrics-pricing)
+ [Using CloudWatch metrics with Lambda](monitoring-metrics.md)
+ [Working with Lambda function logs](monitoring-logs.md)
+ [Logging AWS Lambda API calls using AWS CloudTrail](logging-using-cloudtrail.md)
+ [Visualize Lambda function invocations using AWS X-Ray](services-xray.md)
+ [Monitor function performance with Amazon CloudWatch Lambda Insights](monitoring-insights.md)
+ [Monitoring Lambda applications](applications-console-monitoring.md)
+ [Monitor application performance with Amazon CloudWatch Application Signals](monitoring-application-signals.md)
+ [Remotely debug Lambda functions with Visual Studio Code](debugging.md)

## Pricing
<a name="monitoring-console-metrics-pricing"></a>

CloudWatch has a perpetual free tier. Beyond the free tier threshold, CloudWatch charges for metrics, dashboards, alarms, logs, and insights. For more information, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/#Vended_Logs).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
