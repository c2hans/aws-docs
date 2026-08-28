---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.ListingCategories.html
---

# Listing the Amazon RDS event notification categories
<a name="USER_Events.ListingCategories"></a>

All events for a resource type are grouped into categories. To view the list of categories available, use the following procedures.

## Console
<a name="USER_Events.ListingCategories.Console"></a>

When you create or modify an event notification subscription, the event categories are displayed in the Amazon RDS console. For more information, see [Modifying an Amazon RDS event notification subscription](USER_Events.Modifying.md).

![List DB event notification categories.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/EventNotification-Categories.png)

## AWS CLI
<a name="USER_Events.ListingCategories.CLI"></a>

To list the Amazon RDS event notification categories, use the AWS CLI [`describe-event-categories`](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-event-categories.html) command. This command has no required parameters.

**Example**

```
aws rds describe-event-categories
```

## API
<a name="USER_Events.ListingCategories.API"></a>

To list the Amazon RDS event notification categories, use the Amazon RDS API [`DescribeEventCategories`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeEventCategories.html) command. This command has no required parameters.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
