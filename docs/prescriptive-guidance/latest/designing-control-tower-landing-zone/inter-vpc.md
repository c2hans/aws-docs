---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-control-tower-landing-zone/inter-vpc.html
---

# Inter-VPC connectivity through AWS Transit Gateway
<a name="inter-vpc"></a>

The following diagram shows how you can interconnect VPCs through a transit gateway in the same AWS Region.

![Connecting VPCs in the same Region](http://docs.aws.amazon.com/prescriptive-guidance/latest/designing-control-tower-landing-zone/images/guide-img/156d118c-ed00-4c5b-9a02-63c2673a3342/images/bf5f6380-6194-4290-9822-47624426ccc6.png)

A transit gateway is a network transit hub that you can use to connect your VPCs and on-premises networks. As your organization grows, you can peer transit gateways from different AWS Regions to allow connectivity between them.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
