---
source_url: https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-register-tgw.html
---

# Register a transit gateway in an AWS Cloud WAN global network
<a name="cloudwan-register-tgw"></a>

**Prerequisite:** A transit gateway must first be created on the Amazon Virtual Private Cloud console at [https://console.aws.amazon.com/vpc/home](https://console.aws.amazon.com/vpc/home). For the steps to create a transit gateway, see [Working with transit gateways](https://docs.aws.amazon.com/vpc/latest/tgw/working-with-transit-gateways.html) in the *Amazon VPC Transit Gateways Guide*

Transit gateways that you've created in Amazon VPC can be registered in AWS Cloud WAN to be part of your AWS Cloud WAN global network.

**To register a transit gateway in AWS Cloud WAN**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. Choose **Transit gateways**.

1. For **Select Transit Gateway**, choose the transit gateway that you want to register.

1. Choose **Register Transit Gateway**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
