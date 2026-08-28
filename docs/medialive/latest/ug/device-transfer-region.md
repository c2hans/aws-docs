---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/device-transfer-region.html
---

# Transferring a Link device to another Region
<a name="device-transfer-region"></a>

You can transfer a device to a different AWS Region. (If instead you want to transfer the device to a different Availability Zone in the existing Region, see [Configuring a Link device](device-edit.md).)

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/).

1. In the navigation pane, choose **Input devices**. Find the card for the Link that you want to transfer, and choose the hyperlink.

1. On the **Device details** page for the device, choose **Other device actions** then **Transfer device**.

1. On the **Transfer input device** dialog, choose **Transfer to another AWS Region**, and enter the Region. Then choose **Transfer**. The transfer occurs immediately. There is no need to confirm the transfer.

1. To locate the moved device, switch to the target Region. Choose **Input devices** in the left navigation pane. The devices that you have access to appear.

   You should [review the configuration](device-edit.md) because any customizations (such as the Availability Zone) are deleted during the transfer.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
