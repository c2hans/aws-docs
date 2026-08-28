---
source_url: https://docs.aws.amazon.com/datazone/latest/userguide/security-iam-awsmanpol-AmazonDataZoneSageMakerManageAccessRolePolicy.html
---

# AWS managed policy: AmazonDataZoneSageMakerManageAccessRolePolicy
<a name="security-iam-awsmanpol-AmazonDataZoneSageMakerManageAccessRolePolicy"></a>

This policy gives Amazon DataZone permissions to publish Amazon SageMaker assets to the catalog. It also gives Amazon DataZone permissions to grant access or revoke access to the Amazon SageMaker published assets in the catalog.

This policy includes permissions to do the following:
+ cloudtrail – retrieve information about CloudTrail trails.
+ cloudwatch – retrieve the current CloudWatch alarms.
+ logs – retrieve the metric filters for CloudWatch logs.
+ sns – retrieve the list of subscriptions to an SNS topic.
+ config – retrieve information about configuration recorders, resources, and AWS Config rules. Also allows the service-linked role to create and delete AWS Config rules, and to run evaluations against the rules.
+ iam – get and generate credential reports for accounts.
+ organizations – retrieve account and organizational unit (OU) information for an organization.
+ securityhub – retrieve information about how the Security Hub service, standards, and controls are configured.
+ tag – retrieve information about resource tags.

To view the permissions for this policy, see [AmazonDataZoneSageMakerManageAccessRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonDataZoneSageMakerManageAccessRolePolicy.html) in the *AWS Managed Policy Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
