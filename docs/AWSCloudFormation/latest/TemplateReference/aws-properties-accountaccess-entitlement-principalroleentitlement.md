---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-accountaccess-entitlement-principalroleentitlement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AccountAccess::Entitlement PrincipalRoleEntitlement
<a name="aws-properties-accountaccess-entitlement-principalroleentitlement"></a>

Specifies a principal-to-role entitlement that grants an IAM Identity Center principal permission to assume an IAM role.

## Syntax
<a name="aws-properties-accountaccess-entitlement-principalroleentitlement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-accountaccess-entitlement-principalroleentitlement-syntax.json"></a>

```
{
  "[Account](#cfn-accountaccess-entitlement-principalroleentitlement-account)" : {{String}},
  "[Principal](#cfn-accountaccess-entitlement-principalroleentitlement-principal)" : {{Principal}},
  "[RoleArn](#cfn-accountaccess-entitlement-principalroleentitlement-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-accountaccess-entitlement-principalroleentitlement-syntax.yaml"></a>

```
  [Account](#cfn-accountaccess-entitlement-principalroleentitlement-account): {{String}}
  [Principal](#cfn-accountaccess-entitlement-principalroleentitlement-principal): {{
    Principal}}
  [RoleArn](#cfn-accountaccess-entitlement-principalroleentitlement-rolearn): {{String}}
```

## Properties
<a name="aws-properties-accountaccess-entitlement-principalroleentitlement-properties"></a>

`Account`  <a name="cfn-accountaccess-entitlement-principalroleentitlement-account"></a>
The 12-digit AWS account ID where the IAM role resides.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Principal`  <a name="cfn-accountaccess-entitlement-principalroleentitlement-principal"></a>
The principal (user or group) that is granted access to assume the IAM role.
*Required*: Yes
*Type*: [Principal](aws-properties-accountaccess-entitlement-principal.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-accountaccess-entitlement-principalroleentitlement-rolearn"></a>
The ARN of the IAM role that the principal can assume.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z0-9-]+:iam::[0-9]{12}:role\/([a-zA-Z0-9+=,.@_-]+\/)*[a-zA-Z0-9+=,.@_-]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
