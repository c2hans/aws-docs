---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/delete-phone.html
---

# Deleting phone numbers
<a name="delete-phone"></a>

**Important**
You must unassign phone numbers before you can delete them. Do one of the following:
If you use a Voice Connector or Voice Connector group, you unassign the number. For more information, refer to [Unassigning Voice Connector phone numbers](unassign-numbers.md) in this guide.
If you use a SIP media application, you delete the SIP rule that contains the number. For more information, refer to [Deleting a SIP rule](delete-sip-rule.md) in this guide.

Deleting a number moves it your deletion queue where it's held for 7 days. During that time, you can move the number back to your inventory. After 7 days, the system automatically deletes the number from the holding queue and disassociates it from your account. That returns the number to the Amazon Chime SDK number pool. If you need to reclaim a number after the system deletes it from the holding queue, follow the steps in [Provisioning phone numbers](provision-phone.md), but be aware that the number may not be available.

**To delete unassigned phone numbers**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **Phone Numbers**, choose **Phone number management**.

1. On the **Inventory** tab, choose the number that you want to delete, then choose **Delete**.

1. In the **Delete phone numbers** dialog box, select the check box next to **I understand the impact of this action**, and choose **Delete**.

The system holds deleted phone numbers in the **Deletion queue** for 7 days, then permanently deletes them.
