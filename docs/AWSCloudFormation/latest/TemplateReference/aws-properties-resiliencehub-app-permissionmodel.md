---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resiliencehub-app-permissionmodel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHub::App PermissionModel
<a name="aws-properties-resiliencehub-app-permissionmodel"></a>

Defines the roles and credentials that AWS Resilience Hub would use while creating the application, importing its resources, and running an assessment.

## Syntax
<a name="aws-properties-resiliencehub-app-permissionmodel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resiliencehub-app-permissionmodel-syntax.json"></a>

```
{
  "[CrossAccountRoleArns](#cfn-resiliencehub-app-permissionmodel-crossaccountrolearns)" : {{[ String, ... ]}},
  "[InvokerRoleName](#cfn-resiliencehub-app-permissionmodel-invokerrolename)" : {{String}},
  "[Type](#cfn-resiliencehub-app-permissionmodel-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-resiliencehub-app-permissionmodel-syntax.yaml"></a>

```
  [CrossAccountRoleArns](#cfn-resiliencehub-app-permissionmodel-crossaccountrolearns): {{
    - String}}
  [InvokerRoleName](#cfn-resiliencehub-app-permissionmodel-invokerrolename): {{String}}
  [Type](#cfn-resiliencehub-app-permissionmodel-type): {{String}}
```

## Properties
<a name="aws-properties-resiliencehub-app-permissionmodel-properties"></a>

`CrossAccountRoleArns`  <a name="cfn-resiliencehub-app-permissionmodel-crossaccountrolearns"></a>
Defines a list of role Amazon Resource Names (ARNs) to be used in other accounts. These ARNs are used for querying purposes while importing resources and assessing your application.
+ These ARNs are required only when your resources are in other accounts and you have different role name in these accounts. Else, the invoker role name will be used in the other accounts.
+ These roles must have a trust policy with `iam:AssumeRole` permission to the invoker role in the primary account.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InvokerRoleName`  <a name="cfn-resiliencehub-app-permissionmodel-invokerrolename"></a>
Existing AWS IAM role name in the primary AWS account that will be assumed by AWS Resilience Hub Service Principle to obtain a read-only access to your application resources while running an assessment.
If your IAM role includes a path, you must include the path in the `invokerRoleName` parameter. For example, if your IAM role's ARN is `arn:aws:iam:123456789012:role/my-path/role-name`, you should pass `my-path/role-name`.
+ You must have `iam:passRole` permission for this role while creating or updating the application.
+ Currently, `invokerRoleName` accepts only `[A-Za-z0-9_+=,.@-]` characters.
*Required*: No
*Type*: String
*Pattern*: `((\u002F[\u0021-\u007E]+\u002F){1,511})?[A-Za-z0-9+=,.@_/-]{1,64}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-resiliencehub-app-permissionmodel-type"></a>
Defines how AWS Resilience Hub scans your resources. It can scan for the resources by using a pre-existing role in your AWS account, or by using the credentials of the current IAM user.
*Required*: Yes
*Type*: String
*Allowed values*: `LegacyIAMUser | RoleBased`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
