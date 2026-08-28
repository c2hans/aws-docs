---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-control-tower-landing-zone/cloud-wan.html
---

# AWS Cloud WAN
<a name="cloud-wan"></a>

Although you can create your own global network by interconnecting multiple transit gateways across Regions, you can also take advantage of [AWS Cloud WAN](https://aws.amazon.com/cloud-wan/).  This service provides built-in automation, segmentation, and configuration management features that are designed specifically for building and operating global networks, based on your core network policy.

Both AWS Transit Gateway and AWS Cloud WAN allow centralized connectivity between VPCs and on-premises locations. Transit Gateway is a Regional network connectivity hub and is optimal if you operate in a few AWS Regions and want to manage your own peering and routing configuration. AWS Cloud WAN is optimal for users who want to define their global network through policy and have the service implement the underlying components automatically.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
