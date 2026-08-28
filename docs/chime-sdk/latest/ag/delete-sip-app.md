---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/delete-sip-app.html
---

# Deleting a SIP media application
<a name="delete-sip-app"></a>

You delete a SIP media application for several reasons, such as the following:
+ You stop using a phone number or a Request URI hostname.
+ You make a mistake creating a SIP media application.

**Note**
As a best practice, check to ensure that deleting the application won't disrupt the call flow. Also, deleting the application does not delete any associated phone numbers or SIP rules.

**To delete a SIP media application**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, choose **SIP media applications**.

   The **SIP media application** page appears.

1. Choose the option button next to the application name.

1. Choose **Delete**.

   The **Delete** *application name* dialog box appears.

1. Select **I understand that this action cannot be reversed**, then choose **Delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
