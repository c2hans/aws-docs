---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-control-tower-landing-zone/dc-transit-vif.html
---

# Direct Connect with AWS Transit Gateway over transit VIF
<a name="dc-transit-vif"></a>

The following diagram shows how you can connect VPCs from multiple AWS Regions to an on-premises environment by using Direct Connect and AWS Transit Gateway over a transit VIF.

![Connecting VPCs from multiple Regions to on premises.](http://docs.aws.amazon.com/prescriptive-guidance/latest/designing-control-tower-landing-zone/images/guide-img/156d118c-ed00-4c5b-9a02-63c2673a3342/images/61ab0e94-aa26-4cbc-920a-a375dcb70048.png)

The transit gateway routes traffic through the centralized Direct Connect gateway for all AWS Regions. A transit VIF attachment to the Direct Connect gateway enables your network to connect up to six Regional, centralized transit gateways over a private, dedicated connection.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
