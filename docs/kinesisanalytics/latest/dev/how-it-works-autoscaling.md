---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-autoscaling.html
---

After careful consideration, we have decided to discontinue Amazon Kinesis Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md).

# Automatically Scaling Applications to Increase Throughput
<a name="how-it-works-autoscaling"></a>

Amazon Kinesis Data Analytics elastically scales your application to accommodate the data throughput of your source stream and your query complexity for most scenarios. Kinesis Data Analytics provisions capacity in the form of Kinesis Processing Units (KPU). A single KPU provides you with the memory (4 GB) and corresponding computing and networking.

The default limit for KPUs for your application is 64. For instructions on how to request an increase to this limit, see **To request a limit increase** in [Amazon Service Limits](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
