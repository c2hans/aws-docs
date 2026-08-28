---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/aft-pricing.html
---

# Cost
<a name="aft-pricing"></a>

No additional charge exists for AFT. You pay only for the resources deployed by AFT, the AWS services enabled by AFT, and the resources you deploy in your AFT environment.

The default AFT configuration includes the allocation of AWS PrivateLink endpoints, for enhanced data protection and security, and a NAT gateway that is required to support AWS CodeBuild. For details on the pricing of this infrastructure, see the [AWS PrivateLink pricing](https://aws.amazon.com/privatelink/pricing/) and the [Amazon VPC pricing for the NAT Gateway](https://aws.amazon.com/vpc/pricing/). Contact your AWS account representative for more specific information about managing these costs. You can change these default settings for AFT.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
