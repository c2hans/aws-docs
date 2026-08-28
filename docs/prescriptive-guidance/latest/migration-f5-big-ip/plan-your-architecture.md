---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-f5-big-ip/plan-your-architecture.html
---

# Planning the architecture
<a name="plan-your-architecture"></a>

The following diagram shows the baseline architecture of edge VPC and application VPCs that are connected by AWS Transit Gateway. The VPCs can be part of the same or different accounts.

![F5 architecture on the AWS Cloud.](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-f5-big-ip/images/guide-img/migration-f5-big-ip/images/F5-aws-architecture-2.png)

For example, a landing zone typically deploys a networking account that will control the edge VPCs. This architecture helps users leverage common policies, processes, and platforms across the application suite.

The following diagram shows two network interface (NIC) instances from an F5 BIG-IP workload deployed in an active standby cluster. You can add more elastic network interfaces to these systems, up to the instance limit. F5 recommends that you use a Multi-AZ pattern for your deployment to avoid Availability Zone failure.

![Overview of migration strategy decisions.](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-f5-big-ip/images/guide-img/migration-f5-big-ip/images/F5-aws-architecture.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
