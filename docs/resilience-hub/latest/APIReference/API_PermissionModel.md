---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_PermissionModel.html
---

# PermissionModel
<a name="API_PermissionModel"></a>

Defines the roles and credentials that AWS Resilience Hub would use while creating the application, importing its resources, and running an assessment.

## Contents
<a name="API_PermissionModel_Contents"></a>

 ** type **   <a name="resiliencehub-Type-PermissionModel-type"></a>
Defines how AWS Resilience Hub scans your resources. It can scan for the resources by using a pre-existing role in your AWS account, or by using the credentials of the current IAM user.
Type: String
Valid Values: `LegacyIAMUser | RoleBased`
Required: Yes

 ** crossAccountRoleArns **   <a name="resiliencehub-Type-PermissionModel-crossAccountRoleArns"></a>
Defines a list of role Amazon Resource Names (ARNs) to be used in other accounts. These ARNs are used for querying purposes while importing resources and assessing your application.
+ These ARNs are required only when your resources are in other accounts and you have different role name in these accounts. Else, the invoker role name will be used in the other accounts.
+ These roles must have a trust policy with `iam:AssumeRole` permission to the invoker role in the primary account.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):iam::[0-9]{12}:role/(([^/][!-~]+/){1,511})?[A-Za-z0-9_+=,.@-]{1,64}`
Required: No

 ** invokerRoleName **   <a name="resiliencehub-Type-PermissionModel-invokerRoleName"></a>
Existing AWS IAM role name in the primary AWS account that will be assumed by AWS Resilience Hub Service Principle to obtain a read-only access to your application resources while running an assessment.
If your IAM role includes a path, you must include the path in the `invokerRoleName` parameter. For example, if your IAM role's ARN is `arn:aws:iam:123456789012:role/my-path/role-name`, you should pass `my-path/role-name`.
+ You must have `iam:passRole` permission for this role while creating or updating the application.
+ Currently, `invokerRoleName` accepts only `[A-Za-z0-9_+=,.@-]` characters.
Type: String
Pattern: `([^/]([!-~]+/){1,511})?[A-Za-z0-9_+=,.@-]{1,64}`
Required: No

## See Also
<a name="API_PermissionModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/PermissionModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/PermissionModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/PermissionModel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
