---
source_url: https://docs.aws.amazon.com/lexv2/latest/dg/analytics-permissions.html
---

# Managing access permissions for analytics
<a name="analytics-permissions"></a>

To provide a user access to analytics, attach a policy to an IAM role that permits the role to call the API operations for analytics. You can attach the [AWS managed policy: AmazonLexFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonLexFullAccess) to the IAM role to provide full access to Amazon Lex API operations, or you can create a custom policy allowing only permissions to analytics and attach it to an IAM role.

**To create a custom policy containing permissions for analytics**

1. If you need to first create an IAM role, follow the steps at [Creating a role to delegate permissions to an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html).

1. Follow the steps at [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) to create a policy using the following JSON object. To enable analytics access to specific bots for the IAM role, add the ARN of each bot to the `Resource` field. Replace the {{region}}, {{account-id}}, and {{BOTID}} with the values corresponding to the bots. You can also replace the statement identifier, {{AnalyticsActions}}, with a name of your choice.

1. Attach the policy you created to the role that you want to grant analytics permissions by following the steps at [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html).

1. The role should now have permissions to view analytics for the bots you specified.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
