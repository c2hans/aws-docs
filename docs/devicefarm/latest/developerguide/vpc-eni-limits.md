---
source_url: https://docs.aws.amazon.com/devicefarm/latest/developerguide/vpc-eni-limits.html
---

# Limits
<a name="vpc-eni-limits"></a>

The following limitations are applicable to the VPC-ENI feature:
+ You can provide up to five security groups in the VPC configuration of a Device Farm project.
+ You can provide up to eight subnets in the VPC configuration of a Device Farm project.
+ When configuring a Device Farm project to work with your VPC, the smallest subnet you can provide must have a minimum of five available IPv4 addresses.
+ Public IP addresses aren’t supported at this time. Instead, we recommend that you use private subnets in your Device Farm projects. If your need public internet access during your tests, use a [ network address translation (NAT) gateway](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html#vpc-internet). Configuring a Device Farm project with a public subnet doesn't give your tests internet access or a public IP address.
+ VPC-ENI integration only supports private subnets in your VPC.
+ Only outgoing traffic from the service-managed ENI is supported. This means that the ENI cannot receive unsolicited inbound requests from the VPC.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
