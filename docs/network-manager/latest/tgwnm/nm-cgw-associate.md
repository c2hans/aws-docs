---
source_url: https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-cgw-associate.html
---

# Associate a customer gateway using AWS Network Manager
<a name="nm-cgw-associate"></a>

You can associate a customer gateway with a device and link using the Network Manager console on either of the following pages:
+ On the **Transit gateways** page
+ On the **Devices** page

------
#### [ Transit gateways page ]

**To associate a customer gateway using the Transit gateways page**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Transit gateways**, and then choose the ID of your transit gateway.

1. Choose **On-premises associations**.

1. Select your customer gateway and choose **Associate**.

1. For **Device**, select the ID of the device to associate. For **Link**, select the ID of the link to associate.

1. Choose **Edit on-premises association**.

------
#### [ Devices page ]

**To associate a customer gateway using the Devices page**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Devices**, and then choose the ID of your device.

1. Choose **On-premises associations**.

1. Choose **Associate**.

1. For **Customer gateway**, select the ID of the customer gateway to associate. For **Link**, select the ID of the link to associate.

1. Choose **Create on-premises association**.

------

**Create a customer gateway association using the AWS CLI**
You can view and create a customer gateway association using the following commands.
+ To associate a customer gateway with a device and link: [associate-customer-gateway](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/associate-customer-gateway.html)
+ To view your customer gateway associations: [get-customer-gateway-associations](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/get-customer-gateway-associations.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
