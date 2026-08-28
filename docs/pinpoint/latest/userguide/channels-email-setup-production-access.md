---
source_url: https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-setup-production-access.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Amazon Pinpoint email sandbox
<a name="channels-email-setup-production-access"></a>

We use a sandbox environment to help protect our customers from fraud and abuse. The sandbox environment also helps you establish your sender reputation with ISPs and email recipients. New Amazon Pinpoint email user accounts are placed in the sandbox environment. While your account is in the sandbox, you have full access to Amazon Pinpoint email sending methods, with the following restrictions:
+ You can send email only from verified addresses and domains.
+ You can send email only to addresses that you have verified or addresses that are associated with the mailbox simulator.
+ You can send a maximum of 200 messages within 24 hours.
+ You can send a maximum of one message per second.

To learn how to remove these restrictions, see [Requesting a quota increase](channels-email-manage-limits.md#channels-email-manage-limits-increase-case).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
