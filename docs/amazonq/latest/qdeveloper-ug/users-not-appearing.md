---
source_url: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/users-not-appearing.html
---

# Can't see subscribed users
<a name="users-not-appearing"></a>

**Problem: Subscribed users are not appearing in the Amazon Q Developer console.**

You have subscribed one or more users to the Pro tier, but when you navigate to the Amazon Q Developer console's **Subscriptions** page, you can't see them.

**Solutions:**
+ Make sure you're signed in to the correct AWS account and AWS Region.
+ Try switching to the **Amazon Q** console. The Amazon Q console is able to display users who were subscribed as part of a group, and is also able to display subscriptions across multiple accounts in an organization managed by AWS Organizations.
+ If you switched to the **Amazon Q** console, and still can't see users, do the following:
  + Make sure you're in the correct AWS Region. You will need to be in the Region where your IAM Identity Center instance is deployed. This might be a different Region from your Amazon Q Developer console and profile.
  + If you're using AWS Organizations, try enabling trusted access so that you can see subscriptions in both management and member accounts. For more information, see [Viewing an aggregated list of Amazon Q Developer subscriptions](subscribe-visibility.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
