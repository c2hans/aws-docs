---
source_url: https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-10dlc-associate.html
---

# Associating a long code with a 10DLC campaign
<a name="registrations-10dlc-associate"></a>

After your 10DLC campaign is approved, you have provisioned a new long code or have an existing long code you can then associate that long code with the approved 10DLC campaign. The long code that you associate with the 10DLC campaign can only be used with that campaign, and you can't use it for any other 10DLC campaign.

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Registrations**, choose the 10DLC campaign(US\_TEN\_DLC\_CAMPAIGN\_REGISTRATION) to associate the long code with.

1. Choose the **Associated resourced** tab and **Add resource**.

1. For **Supported association**, choose **TEN\_DLC** from the dropdown list.

1. For **Available resources**, choose the 10DLC phone number to add.

1. Choose **Associate resource**.

You can associate more than one long code with the 10DLC campaign.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
