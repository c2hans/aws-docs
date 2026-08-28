---
source_url: https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/Welcome.html
---

# Welcome
<a name="Welcome"></a>

This AWS CodeStar Notifications API Reference provides descriptions and usage examples of the operations and data types for the AWS CodeStar Notifications API. You can use the AWS CodeStar Notifications API to work with the following objects:

Notification rules, by calling the following:
+  [CreateNotificationRule](API_CreateNotificationRule.md), which creates a notification rule for a resource in your account.
+  [DeleteNotificationRule](API_DeleteNotificationRule.md), which deletes a notification rule.
+  [DescribeNotificationRule](API_DescribeNotificationRule.md), which provides information about a notification rule.
+  [ListNotificationRules](API_ListNotificationRules.md), which lists the notification rules associated with your account.
+  [UpdateNotificationRule](API_UpdateNotificationRule.md), which changes the name, events, or targets associated with a notification rule.
+  [Subscribe](API_Subscribe.md), which subscribes a target to a notification rule.
+  [Unsubscribe](API_Unsubscribe.md), which removes a target from a notification rule.

Targets, by calling the following:
+  [DeleteTarget](API_DeleteTarget.md), which removes a notification rule target from a notification rule.
+  [ListTargets](API_ListTargets.md), which lists the targets associated with a notification rule.

Events, by calling the following:
+  [ListEventTypes](API_ListEventTypes.md), which lists the event types you can include in a notification rule.

Tags, by calling the following:
+  [ListTagsForResource](API_ListTagsForResource.md), which lists the tags already associated with a notification rule in your account.
+  [TagResource](API_TagResource.md), which associates a tag you provide with a notification rule in your account.
+  [UntagResource](API_UntagResource.md), which removes a tag from a notification rule in your account.

 For information about how to use AWS CodeStar Notifications, see the [AWS Developer Tools Console User Guide](https://docs.aws.amazon.com/dtconsole/latest/userguide/what-is-dtconsole.html).

This document was last published on August 28, 2026.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeStar Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codestar-notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
