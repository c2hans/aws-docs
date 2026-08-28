---
source_url: https://docs.aws.amazon.com/firehose/latest/dev/across.html
---

# Understand delivery across AWS accounts and regions
<a name="across"></a>

Amazon Data Firehose supports data delivery to HTTP endpoint destinations across AWS accounts. The Firehose stream and the HTTP endpoint that you choose as your destination can belong to different AWS accounts.

Amazon Data Firehose also supports data delivery to HTTP endpoint destinations across AWS regions. You can deliver data from a Firehose stream in one AWS region to an HTTP endpoint in another AWS region. You can also delivery data from a Firehose stream to an HTTP endpoint destination outside of AWS regions, for example to your own on-premises server by setting the HTTP endpoint URL to your desired destination. For these scenarios, additional data transfer charges are added to your delivery costs. For more information, see the [Data Transfer](https://aws.amazon.com/ec2/pricing/on-demand/#Data_Transfer) section in the "On-Demand Pricing" page.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
