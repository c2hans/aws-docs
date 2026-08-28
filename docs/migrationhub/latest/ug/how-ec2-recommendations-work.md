---
source_url: https://docs.aws.amazon.com/migrationhub/latest/ug/how-ec2-recommendations-work.html
---

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# How Amazon EC2 instance recommendations work in AWS Migration Hub
<a name="how-ec2-recommendations-work"></a>

This feature recommends the most cost-effective Amazon Elastic Compute Cloud instance type that can satisfy your existing server specifications and utilization requirements while taking into account your selected instance preferences. The server specifications that are used to generate your recommendations are:
+ Number of processors
+ Number of logical cores
+ Total amount of RAM
+ Operating system family
+ Usage data including peak, average, and percentiles of CPU and RAM

Amazon EC2 instance recommendations returns the best Amazon EC2 instance type match based on server specification as well as the performance dimensions you provided. To match the performance dimensions, the service adjusts the server’s specification by multiplying the original CPU and RAM values by the usage percentage.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Migration Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
