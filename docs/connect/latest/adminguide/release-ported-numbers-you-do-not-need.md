---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/release-ported-numbers-you-do-not-need.html
---

# Release numbers that you ported to Connect Customer that you no longer need
<a name="release-ported-numbers-you-do-not-need"></a>

You do not have to keep phone numbers assigned to your Connect Customer instance.

When a phone number is released from your Connect Customer instance:
+ You will no longer be charged for it.
+ You cannot reclaim the phone number.
+ Connect Customer reserves the right to allow it to be claimed by another customer.

**To release a phone number**

1. Log in to Connect Customer admin website with an Admin account or a user account that has **Phone numbers - Release** security profile permission.

1. On the navigation menu, choose **Channels**, **Phone numbers**. This option appears only if you have the **Phone numbers - View** permission in your security profile.

1. Choose the phone number you want to release, and then choose **Release**. This option appears only if you have the **Phone numbers - Release** permission in your security profile.

If the phone number is associated with a flow, that flow will be deactivated until another number is associated with it.

When customers call the phone number you have released, they will get a message that it is not a working phone number.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
