---
source_url: https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-discard.html
---

# Discard a registration's current version in AWS End User Messaging SMS
<a name="registrations-discard"></a>

You can discard the current version of your registration and make any needed updates. If you find an error in the registration that you have submitted you can use this feature to correct the error and resubmit instead of waiting to have your registration denied and then correct the error. You can only discard the registration if its status is `Submitted`. This will permanently delete the current version of the registration.

**To discard a registration**

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Configurations**, choose **Registrations**.

1. On the **Registrations** table, select the **Registration ID** that you want.

1. Choose **Discard version** and in the window enter **discard**.

1. Choose **Discard version**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
