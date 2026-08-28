---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/voice-connector-groups.html
---

# Managing Amazon Chime SDK Voice Connector groups
<a name="voice-connector-groups"></a>

**How an Amazon Chime SDK Voice Connector group works**
 Voice Connector groups only handle inbound PSTN calls to your SIP based phone system. The groups provide fault-tolerant, cross-region call routing. A Voice Connector group contains two or more Voice Connectors, and can include Voice Connectors created in different AWS Regions. This allows incoming PSTN calls to fail over across AWS Regions if availability events affect service in one region.

 For example, say that you create a Voice Connector group and assign two Voice Connectors to it, one in the US East (N. Virginia) Region, and the other in the US West (Oregon) Region. You configure both Voice Connectors with origination settings that point to your SIP host(s).

Now say that a call comes in to the Voice Connector in the US East (N. Virginia) Region. If that Region has a connectivity issue, the call automatically reroutes to the Voice Connector in the US West (Oregon) Region.

**Get started with an Amazon Chime SDK Voice Connector group**
To get started, first create Voice Connectors in different AWS Regions. Then, create a Voice Connector group and assign the Voice Connectors to it. You can also provision phone numbers for your Voice Connector group from your Amazon Chime SDK **Phone number management** inventory. For more information, see [Provisioning phone numbers](provision-phone.md). For more information about creating Amazon Chime SDK Voice Connectors in different AWS Regions, see [Managing Amazon Chime SDK Voice Connectors](voice-connectors.md).

**Topics**
+ [Creating an Amazon Chime SDK Voice Connector group](#create-voicecon-group)
+ [Editing an Amazon Chime SDK Voice Connector group](#edit-voicecon-group)
+ [Assigning and unassigning phone numbers to a Voice Connector group](#assign-voicecon-group)
+ [Deleting an Amazon Chime SDK Voice Connector group](#delete-voicecon-group)

## Creating an Amazon Chime SDK Voice Connector group
<a name="create-voicecon-group"></a>

You can create up to three Amazon Chime SDK Voice Connector groups for your account.

**To create a group**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **SIP Trunking**, choose **Voice connectors**.

1. Choose **Create group**.

1. In the dialog box that appears, under **Voice connector group name**, enter a name for the group.

1. Choose **Create**.

## Editing an Amazon Chime SDK Voice Connector group
<a name="edit-voicecon-group"></a>

After you create an Amazon Chime SDK Voice Connector group, you can add or remove Amazon Chime SDK Voice Connectors for it. You can also edit the priority for the Voice Connectors in the group.

**To add Voice Connectors to a group**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **SIP Trunking**, choose **Voice connectors**.

1. Choose the name of the Voice Connector group that you want to edit.

1. Choose the **Voice connectors** tab, open the **Actions** list, then choose **Add**.

1. In the dialog box that appears, select the checkbox next to the Voice Connector that you want to use.

1. Choose **Add**.

1. Repeat steps 4 through 6 to add Voice Connectors to the group.

**To edit Voice Connector priority in a group**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **SIP Trunking**, choose **Voice connectors**.

1. Choose the name of the Amazon Chime SDK Voice Connector group that you want to edit.

1. Under **Actions**, choose **Edit priority**.

1. In the dialog box that appears, enter a different priority ranking for each Voice Connector. 1 is the highest priority. Higher priority Voice Connectors are attempted first.

1. Choose **Save**.

**To remove Voice Connectors from a group**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **SIP Trunking**, choose **Voice connectors**.

1. Choose the name of the Voice Connector group that you want to edit.

1. Open the **Actions** list and choose **Remove**.

1. In the dialog box that appears, select the check boxes next to the Voice Connectors that you want to remove.

1. Choose **Remove**.

## Assigning and unassigning phone numbers to a Voice Connector group
<a name="assign-voicecon-group"></a>

You use the Amazon Chime SDK console to assign and unassign phone numbers to a Voice Connector group.

**To assign phone numbers to a Voice Connector group**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **SIP Trunking**, choose **Voice connectors**.

1. Choose the name of the Voice Connector group to edit.

1. Choose **Phone numbers**.

1. Choose **Assign from inventory**.

1. Select one or more phone numbers to assign to the Voice Connector group.

1. Choose **Assign from inventory**.

You can also choose **Reassign** to reassign phone numbers with the **Voice Connector** product type. This lets you reassign these numbers from one Voice Connector or Voice Connector group to another.

**To unassign phone numbers from a Voice Connector group**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **SIP Trunking**, choose **Voice connectors**.

1. Choose the name of the Voice Connector group to edit.

1. Choose **Phone numbers**.

1. Select the phone numbers that you want from the Voice Connector group, and choose **Unassign**.

1. Choose **Unassign**.

## Deleting an Amazon Chime SDK Voice Connector group
<a name="delete-voicecon-group"></a>

Before you can delete an Amazon Chime SDK Voice Connector group, you must unassign all Amazon Chime SDK Voice Connectors and phone numbers from it. For more information, see the previous section.

**To delete a Voice Connector group**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **SIP Trunking**, choose **Voice connectors**.

1. Choose the name of the Voice Connector group to delete.

1. Choose **Delete group**.

1. Select the check box, and choose **Delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
