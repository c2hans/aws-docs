---
source_url: https://docs.aws.amazon.com/network-manager/latest/tgwnm/tgw-registrations.html
---

# Transit gateway registrations in AWS Global Networks for Transit Gateways
<a name="tgw-registrations"></a>

You can register your existing transit gateways with a global network. Any transit gateway attachments (such as VPCs, VPN connections, and Direct Connect gateways) are automatically included in your global network.

## Transit gateway limitations
<a name="tgw-limitations"></a>

Note the following about registering transit gateways in a global network:
+ A transit gateway must first be created in Amazon Virtual Private Cloud (VPC) before it can be registered in a global network. For more information about transit gateways and creating one, see [Transit gateways](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html) in the *Amazon VPC Transit Gateways User Guide*.
+ You can have multiple global networks, but you can only register one transit gateway with one global network.
+ You can register transit gateways that are in the same AWS account as the global network.
+ You cannot create, delete, or modify your transit gateways and their attachments using the Network Manager console or APIs. To work with transit gateways, use the Amazon VPC console or the Amazon EC2 APIs.

**Topics**
+ [Transit gateway limitations](#tgw-limitations)
+ [Register a transit gateway](register-tgw.md)
+ [View registered transit gateways](view-registered-tgws.md)
+ [Deregister a transit gateway](deregister-tgw.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
