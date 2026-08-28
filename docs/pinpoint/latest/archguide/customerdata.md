---
source_url: https://docs.aws.amazon.com/pinpoint/latest/archguide/customerdata.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Synchronizing customer data across AWS Regions
<a name="customerdata"></a>

Regardless of the architecture design that you choose, make sure that your customer data is synchronized across the AWS Regions that you intend to use. In this case, "customer data" refers to the contact information for your customers (such as their email addresses, phone numbers, name, or company). It also refers to the preference data for your customers—that is, their opt-in and opt-out preferences. Finally, it refers to information about whether they're able to receive messages from you.

In a resilient architecture, it's important to keep all of this information synchronized across all of the AWS Regions in which you use Amazon Pinpoint. This chapter contains example architectures that you can use to keep this information synchronized.

**Topics**
+ [Synchronizing endpoint information](customerdata-endpoints.md)
+ [Synchronizing event data](customerdata-events.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
