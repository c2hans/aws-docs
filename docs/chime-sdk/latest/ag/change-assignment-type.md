---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/change-assignment-type.html
---

# Changing a phone number's assignment type
<a name="change-assignment-type"></a>

If you have unassigned Amazon Chime SDK Voice Connector, or Amazon Chime SDK SIP media application phone numbers, you can switch them from one product type to another.

**Note**
For non-US numbers, you must use the **SIP Media Application Dial-In** product type.

**To change assignment types**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **Phone Numbers**, choose **Phone number management**.

1. On the **Inventory** tab, select the phone number that you want to change.

1. On the **Details** page, choose **Edit**.

1. Under **Assignment type**, choose **Voice Connector**, or **Voice Connector group**.

   Depending on your choice, the **Voice Connector options** or **Voice Connector group options** list appears.

1. Open the list and choose a Voice Connector or Voice Connector group.

1. Choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
