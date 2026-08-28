---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/reassign-vc-numbers.html
---

# Reassigning Voice Connector numbers
<a name="reassign-vc-numbers"></a>

You can reassign phone numbers from one Amazon Chime SDK Voice Connector or Amazon Chime SDK Voice Connector group to another. The numbers must have the **Voice Connector** product type.

You can reassign individual numbers or groups of numbers, and the following steps explain how to do both.

**To reassign individual numbers**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **Phone Numbers**, choose **Phone number management**.

1. On the **Inventory** tab, select the phone number that you want to reassign.

1. Choose **Edit**.

1. Under **Assignment type** choose **Voice Connector** or **Voice Connector group**. **Next**.

1. Do one of the following:

   1. If you chose **Voice Connector**, open the **Voice Connector options** list and select a new Voice Connector.

   1. If you chose **Voice Connector group**, open the **Voice Connector group options** list and select a new Voice Connector group.

1. Choose **Save**.

**To reassign groups of phone numbers**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **Phone Numbers**, choose **Phone number management**.

1. On the **Inventory** tab, select the check boxes next to the phone numbers that you want to reassign, then choose **Reassign**.

1. In the **Reassign** dialog box, choose **Voice Connector** or **Voice Connector group**, then choose **Next**.

1. Select a Voice Connector or Voice Connector group, then choose **Reassign**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
