---
source_url: https://docs.aws.amazon.com/awssupport/latest/user/prerequisites-support-app-for-slack.html
---

# Prerequisites
<a name="prerequisites-support-app-for-slack"></a>

You must meet the following requirements to use the AWS Support App in Slack:
+ You have a AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan. You can find your support plan from the AWS Support Center Console or from the [Support plans](https://console.aws.amazon.com/support/plans) page. For more information, see [Compare AWS Support plans](https://aws.amazon.com/premiumsupport/plans/).
+ You have a [Slack](https://slack.com/) workspace and channel for your organization. You must be a Slack workspace administrator, or have permission to add apps to that Slack workspace. For more information, see the [Slack Help Center](https://slack.com/help/articles/222386767-Manage-app-approval-for-your-workspace).
+ You sign in to the AWS account as an AWS Identity and Access Management (IAM) user or role with the required permissions. For more information, see [Managing access to the AWS Support App widget](slack-authorization-permissions.md).
+ You will need to create an IAM role that has the required permissions to perform actions for you. The AWS Support App uses this role to make API calls to different services. For more information, see [Managing access to the AWS Support App](support-app-permissions.md).

**Topics**
+ [Managing access to the AWS Support App widget](slack-authorization-permissions.md)
+ [Managing access to the AWS Support App](support-app-permissions.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awssupport` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
