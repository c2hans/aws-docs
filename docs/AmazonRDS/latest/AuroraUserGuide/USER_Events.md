---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Events.html
---

# Working with Amazon RDS event notification
<a name="USER_Events"></a>

Amazon RDS uses the Amazon Simple Notification Service (Amazon SNS) to provide notification when an Amazon RDS event occurs. These notifications can be in any notification form supported by Amazon SNS for an AWS Region, such as an email, a text message, or a call to an HTTP endpoint.

**Topics**
+ [Overview of Amazon RDS event notification](USER_Events.overview.md)
+ [Granting permissions to publish notifications to an Amazon SNS topic](USER_Events.GrantingPermissions.md)
+ [Subscribing to Amazon RDS event notification](USER_Events.Subscribing.md)
+ [Amazon RDS event notification tags and attributes](USER_Events.TagsAttributesForFiltering.md)
+ [Listing Amazon RDS event notification subscriptions](USER_Events.ListSubscription.md)
+ [Modifying an Amazon RDS event notification subscription](USER_Events.Modifying.md)
+ [Adding a source identifier to an Amazon RDS event notification subscription](USER_Events.AddingSource.md)
+ [Removing a source identifier from an Amazon RDS event notification subscription](USER_Events.RemovingSource.md)
+ [Listing the Amazon RDS event notification categories](USER_Events.ListingCategories.md)
+ [Deleting an Amazon RDS event notification subscription](USER_Events.Deleting.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
