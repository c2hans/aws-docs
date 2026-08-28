---
source_url: https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-edit.html
---

# Edit a registration in AWS End User Messaging SMS
<a name="registrations-edit"></a>

After you submit your registration, the **registration status** will display as **Requires Updates** if there is an issue with the registration. In this state, the registration form is editable. Fields that require updates have a warning icon and a brief description of the issue.

**To edit a registration**

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Configurations**, choose **Registrations**.

1. On the **Registrations** table, select the **Registration ID** that you want to edit.

1. Choose **Update registration** to edit the form and correct fields that have a warning icon.
**Note**
If your registration was rejected and requires updates the banner lists the reason the registration was rejected and which fields need to be updated. For more information about registration rejections, see [Toll-free number registration rejection reasons](registrations-tfn-rejection-reason.md) and [Gen-AI Feedback on Registrations (Preview)](registrations-genai-feedback.md).

1. Choose **Submit registration** to resubmit when you're done.
**Important**
Recheck all fields to confirm that they're correct.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
