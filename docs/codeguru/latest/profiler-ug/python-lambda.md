---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/python-lambda.html
---

# Profiling your applications that run on AWS Lambda
<a name="python-lambda"></a>

CodeGuru Profiler integration for AWS Lambda is currently available for applications that run on Python 3.7 up to Python 3.9. To start CodeGuru Profiler in your application running on Lambda, you can either apply the CodeGuru Profiler function decorator to your handler function, update your Lambda function configuration by adding layers, or enable profiling in the Lambda console.

If you enabled profiling in the Lambda console, you don't have to complete the procedure outlined in the following sections. To learn more about enabling profiling from the Lambda console, see [Set up in the Lambda console](setting-up-short.md).

**Note**
You can profile your Lambda functions running in Python if they are called often enough for CodeGuru Profiler to gather enough samples. CodeGuru Profiler collects data once per second, aggregated into 5-minute sampling buckets. For Lambda functions running for fewer than 5 minutes, your application must run multiple times so CodeGuru Profiler can collect enough data. If it runs too infrequently, CodeGuru Profiler can't generate enough data to provide recommendations and flame graphs. For long-running Lambda applications, processing can take up to 15 minutes to display graphs and information. If you are running your application in shorter durations, processing takes longer to display information.

**Topics**
+ [Apply the CodeGuru Profiler function decorator to your handler function](python-lambda-command-line.md)
+ [Use AWS Lambda layers](python-lambda-layers.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
