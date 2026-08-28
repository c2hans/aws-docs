---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/problem-notification-rule-fails-to-exist-error.html
---

# Problem: AWS::CodeStarNotifications::NotificationRule fails to create during deployment
<a name="problem-notification-rule-fails-to-exist-error"></a>

When deploying a solution that uses the `AWS::CodeStarNotifications::NotificationRule` resource, the resource creation may fail with the error "Invalid request provided: AWS::CodeStarNotifications::NotificationRule". The `AWS::CodeStarNotifications::NotificationRule` resource is attempting to create a notification rule, but the necessary service role has not been fully created yet. This is due to a timing issue, where the resource is trying to create the rule before the service role is ready.

## Resolution
<a name="resolution-notification-rule"></a>

If you encounter this issue, you can try manually retrying the failed resource creation. After approximately 15 minutes, the service role should be fully created, and the `AWS::CodeStarNotifications::NotificationRule` resource should be able to create the notification rule successfully.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
