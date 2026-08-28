---
source_url: https://docs.aws.amazon.com/migrationhub/latest/ug/ec2-recommendation-prerequisites.html
---

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Prerequisites for getting Amazon EC2 instance recommendations in AWS Migration Hub
<a name="ec2-recommendation-prerequisites"></a>

Before you can get Amazon EC2 instance recommendations, you must have data about your on-premises servers in Migration Hub. This data can come from the discovery tools Application Discovery Service Agentless Collector (Agentless Collector) or AWS Application Discovery Agent (Discovery Agent), or from Migration Hub import.
+ [Migration Hub import](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-import.html) – This allows you to import details of your on-premises environment directly into Migration Hub using a predefined CSV template. For more information, see [Migration Hub import](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-import.html).
+ [Agentless Collector](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-connector.html) – This is a VMware appliance that can collect information only about VMware virtual machines (VMs). For more information, see [Application Discovery Service Agentless Collector](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector.html) in the *Application Discovery Service User Guide*
+ [Discovery Agent](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-agent.html) – This is AWS software that you install on on-premises servers and VMs targeted for discovery and migration. For more information, see [AWS Application Discovery Agent](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-agent.html) in the *Application Discovery Service User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Migration Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
