---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/create-sip-rule.html
---

# Creating a SIP rule
<a name="create-sip-rule"></a>

Before you can create a SIP rule, you need at least one DID or toll-free phone number with a **Product Type** set to **SIP Media Application Dial-In** in your Amazon Chime SDK inventory, or a Request URI hostname associated with an Amazon Chime SDK Voice Connector, and a SIP media application. For more about SIP applications, see [Creating a SIP media application](create-sip-app.md). Also, you can use rules created by other administrators.

**To create a SIP rule**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **Phone Numbers**, choose **SIP media applications**.

1. Choose the SIP application for which you want to create a rule, then choose the **Rules** tab.

1. Copy the phone number or **Outbound host name** value, paste the value into Notepad or a similar program, and keep that program open for later use.

1. In the navigation pane, choose **SIP rules**.

   The **SIP rules** page appears.

1. Choose **Create**.

   The **Create a SIP rule** dialog box appears.

1. In the **Name** box, enter a name for the rule, then do one of the following:

**Create a rule for a phone number**

   1. By default, the **Trigger type** list displays **To phone number**. If it doesn't, open the list and select that value.

   1. For **Phone number**, enter a phone number or choose one from the list. If you enter a number, use this format: **\+1**{{ten-digit number}}. For example: \+15095551212.

**Create a rule for a Request URI hostname**

   1. Open the **Trigger type** list and choose **Request URI hostname**.

   1. Paste the hostname that you copied in step 2 into the **Request URI hostname** box.

1. To use the rule immediately, leave the **Enabled** check box selected. To disable the rule—for example, until an Amazon Chime SDK Voice Connector and its hostname become available—clear the check box.

1. Choose **Next**, and on the **Step 2** page, open the **SIP media application** list and select the SIP media application that you want to use.

1. As needed, choose **Add a SIP media application** to use the rule with multiple applications.

1. Choose **Create.**

   A success message appears. If an error message appears, follow its instructions.
