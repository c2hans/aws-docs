---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/security_iam_id-based-policy-examples.html
---

# Amazon Chime SDK identity-based policy examples
<a name="security_iam_id-based-policy-examples"></a>

By default, IAM users and roles don't have permission to create or modify Amazon Chime SDK resources. They also can't perform tasks using the AWS Management Console, AWS CLI, or AWS API. An IAM administrator must create IAM policies that grant users and roles permission to perform specific API operations on the specified resources they need. The administrator must then attach those policies to the IAM users or groups that require those permissions.

To learn how to create an IAM identity-based policy using these example JSON policy documents, see [Creating policies on the JSON tab](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html#access_policies_create-json-editor) in the *IAM User Guide*.

**Topics**
+ [Policy best practices](security_iam_service-with-iam-policy-best-practices.md)
+ [AWS managed Amazon Chime SDK policy](security_iam_id-based-policy-examples-chime-sdk.md)
+ [AWS managed policy: AmazonChimeVoiceConnectorServiceLinkedRolePolicy](cvc-linked-role-policy.md)
+ [AWS managed policy: AmazonChimeSDKMediaPipelinesServiceLinkedRolePolicy](media-pipeline-service-linked-role-policy.md)
+ [Amazon Chime updates to AWS managed policies](security-iam-awsmanpol-updates.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
