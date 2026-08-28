---
source_url: https://docs.aws.amazon.com/iot-mi/latest/devguide/interface-vpc-endpoints.html
---

# Use Managed Integrations with interface VPC endpoints
<a name="interface-vpc-endpoints"></a>

You can establish a private connection between your Amazon VPC and AWS IoT Managed Integrations by creating an interface Amazon VPC endpoint. Interface endpoints are powered by AWS PrivateLink, a technology that enables you to privately access services by using private IP addresses. AWS PrivateLink restricts all network traffic between your VPC and IoT Managed Integrations to the Amazon network. You don't need an internet gateway, NAT device, or VPN connection.

You are not required to use AWS PrivateLink, but it's recommended. For more information about AWS PrivateLink and VPC endpoints, see [ Accessing AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html) in the *AWS PrivateLink Guide*.

**Topics**
+ [Considerations for AWS IoT Managed Integrations VPC endpoints](vpc-endpoints-considerations.md)
+ [Creating an interface VPC endpoint for AWS IoT Managed Integrations](vpc-endpoints-creating.md)
+ [Testing your VPC endpoint](vpc-endpoints-testing.md)
+ [Controlling access to services over VPC endpoints](vpc-endpoints-access-control.md)
+ [Pricing](vpc-endpoints-pricing.md)
+ [Limitations](vpc-endpoints-limitations.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
