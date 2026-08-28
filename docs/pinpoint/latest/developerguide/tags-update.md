---
source_url: https://docs.aws.amazon.com/pinpoint/latest/developerguide/tags-update.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Update or overwrite tags for Amazon Pinpoint resources programmatically
<a name="tags-update"></a>

There are several ways to update (overwrite) a tag for an Amazon Pinpoint resource. The best way to update a tag depends on:
+ The type of resource that you want to update tags for.
+ Whether you want to update a tag for one or multiple resources at the same time.
+ Whether you want to update a tag key, a tag value, or both.

To update a tag for an Amazon Pinpoint project or for multiple resources at the same time, use the resource groups tagging operations of the AWS CLI or the [AWS Resource Groups Tagging API](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/Welcome.html). The Amazon Pinpoint API currently doesn’t provide direct support for either of those tasks.

To update a tag for one resource, you can [remove the current tag](tags-remove.md) and [add a new tag](tags-add.md) by using the Amazon Pinpoint API.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
