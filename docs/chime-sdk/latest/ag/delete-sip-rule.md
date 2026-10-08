---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/delete-sip-rule.html
---

# Deleting a SIP rule
<a name="delete-sip-rule"></a>

**Note**
Amazon Chime SDK SIP media applications will no longer be open to new customers starting October 29, 2026. If you would like to use SIP media applications, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Amazon Chime SDK SIP media applications availability change](sip-applications-maintenance-mode.md).

Typically, you delete a SIP rule when you don't need the associated Request URI hostname or phone number. Also, you can delete a SIP rule when you make a mistake creating it.

**Note**
You must disable a rule before you can delete it. For more information about disabling rules, see [Disabling a SIP rule](disable-sip-rule.md).

**To delete a SIP rule**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **PSTN Audio**, choose **SIP rules**.

   The **SIP rules** page appears.

1. Choose the radio button next to the rule's name.

1. Open the **Actions** list and choose **Delete**.

   The **Delete rule(s)** dialog box appears.

1. Select **I understand that this action cannot be reversed**, then choose **Delete**.
