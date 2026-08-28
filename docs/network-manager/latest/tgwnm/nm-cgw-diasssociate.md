---
source_url: https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-cgw-diasssociate.html
---

# Disassociate a customer gateway using AWS Network Manager
<a name="nm-cgw-diasssociate"></a>

You can disassociate a customer gateway from a device or link using the Network Manager console on either of the following pages:
+ On the **Transit gateways** page
+ On the **Devices** page

------
#### [ Transit gateways page ]

**To disassociate a customer gateway using the Transit gateways page**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Transit gateways**, and then choose **On-premises associations**.

1. Select your customer gateway and choose **Disassociate**.

------
#### [ Devices page ]

**To disassociate a customer gateway using the Devices page**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Devices**, and then choose the ID of your device.

1. Choose **On-premises associations**.

1. Select your customer gateway and choose **Disassociate**.

------

**Disassociate a customer gateway association using the AWS CLI**
You can view and disassociate a customer gateway association using the following command.
+ To view your customer gateway associations: [get-customer-gateway-associations](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/get-customer-gateway-associations.html)
+ To disassociate a customer gateway from a device and link: [disassociate-customer-gateway](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/disassociate-customer-gateway.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
