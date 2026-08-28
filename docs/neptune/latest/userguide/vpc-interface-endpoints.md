---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/vpc-interface-endpoints.html
---

# Amazon Neptune and interface VPC endpoints (AWS PrivateLink)
<a name="vpc-interface-endpoints"></a>

You can use [AWS PrivateLink](https://aws.amazon.com/privatelink/) to create a private connection between your VPC and Amazon Neptune API endpoints. You can access Amazon Neptune API operations as though they were in your VPC, without the use of an internet gateway, NAT device, VPN connection, or connection. Traffic between your VPC and Amazon Neptune stays within the Amazon network.

Amazon Neptune shares API infrastructure with Amazon Relational Database Service. To set up interface VPC endpoints for Amazon Neptune, follow the instructions in [Amazon RDS API and interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/vpc-interface-endpoints.html) in the *Amazon Aurora User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
