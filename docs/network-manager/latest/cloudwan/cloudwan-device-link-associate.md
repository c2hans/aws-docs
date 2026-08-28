---
source_url: https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-device-link-associate.html
---

# Associate or disassociate a device link in an AWS Cloud WAN global network
<a name="cloudwan-device-link-associate"></a>

Associate a link with a device in your Cloud WAN global network. In order to associate a link with a device, you must first create a link that can be used for the device connection. For more information on creating a ink, see [Create a link for a site in an AWS Cloud WAN global network](cloudwan-site-link-add.md).

You can only associate one link with one device. If a link is already associated with a device, and you want to use that link with another device, you must first disassociate the link the device it's associated with.

**To associate a link with a device**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Devices**.

1. Choose the link for the device **ID** that you want to add a link to, and then choose the **Links** tab.
**Note**
Choose the link. Do not select the check box.

1. Choose the **Links** tab, and then choose **Associate link**.

1. Choose the link that you want to associate with the device.

1. Choose **Associate link**.

   The link is available to use immediately.

If you to use a link with another device, you must first disassociate the link from its original device.

**To disassociate a link from a device**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Devices**.

1. Choose the link for the device **ID** that you want to add a link to, and then choose the **Links** tab.
**Note**
Choose the link. Do not select the check box.

1. Choose the **Links** tab, and then choose **Associate link**.

1. Choose the check box for the link that you want to disassociate from a device.

1. Choose **Disassociate link**.

   Disassociation occurs immediately.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
