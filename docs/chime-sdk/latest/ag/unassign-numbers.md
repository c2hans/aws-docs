---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/unassign-numbers.html
---

# Unassigning Voice Connector phone numbers
<a name="unassign-numbers"></a>

The following procedures explain how to unassign phone numbers from Amazon Chime SDK Voice Connectors and Voice Connector groups. You can't unassign phone numbers used by SIP media applications. Instead, you delete the SIP rule. For more information about deleting SIP rules, refer to [Deleting a SIP rule](delete-sip-rule.md) in this guide.

**Note**
Unassigning numbers and deleting SIP rules disables the users' telephony capabilities. However, unassigned numbers remain available in your inventory, and you will be billed according to their product type.

**To unassign individual Voice Connector phone numbers**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **Phone Numbers**, choose **Phone number management**.

1. On the **Inventory** tab, choose the phone number that you want to unassign.

1. Choose **Edit**, and under **Assignment type**, choose **Voice connector** or **Voice connector group**.

1. Open the **Voice connector options** or **Voice connector group options** list and choose **None (unassign)**, the first option in the list.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
