---
source_url: https://docs.aws.amazon.com/pinpoint/latest/userguide/message-templates-managing-add-tag.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Adding a tag to a template
<a name="message-templates-managing-add-tag"></a>

A tag is a label that you can define and associate with AWS resources, including certain types of Amazon Pinpoint resources.

Adding a tag to a template can help you categorize and manage templates in different ways, such as by purpose, owner, environment, or other criteria. You can use tags to quickly find existing templates, or to control which users can access specific templates. You can add at most 50 key-value pairs, with each key being unique.

**To add a tag**

1. Open the Amazon Pinpoint console at [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/).

1. In the navigation pane, choose **Message templates**.

1. On the **Message templates** page, choose the template that you want to add a tag to.

1. Under **Tags**, choose **Manage tags**.

1. Choose **Add new tag**.

1. Enter the tag key and value pair that you want to add.

1. (Optional) To add additional tags, choose **Add new tag**.

1. When you finish, choose **Save tags**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
