---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sso-permissionset-customermanagedpolicyreference.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSO::PermissionSet CustomerManagedPolicyReference
<a name="aws-properties-sso-permissionset-customermanagedpolicyreference"></a>

Specifies the name and path of a customer managed policy. You must have an IAM policy that matches the name and path in each AWS account where you want to deploy your permission set.

## Syntax
<a name="aws-properties-sso-permissionset-customermanagedpolicyreference-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sso-permissionset-customermanagedpolicyreference-syntax.json"></a>

```
{
  "[Name](#cfn-sso-permissionset-customermanagedpolicyreference-name)" : {{String}},
  "[Path](#cfn-sso-permissionset-customermanagedpolicyreference-path)" : {{String}}
}
```

### YAML
<a name="aws-properties-sso-permissionset-customermanagedpolicyreference-syntax.yaml"></a>

```
  [Name](#cfn-sso-permissionset-customermanagedpolicyreference-name): {{String}}
  [Path](#cfn-sso-permissionset-customermanagedpolicyreference-path): {{String}}
```

## Properties
<a name="aws-properties-sso-permissionset-customermanagedpolicyreference-properties"></a>

`Name`  <a name="cfn-sso-permissionset-customermanagedpolicyreference-name"></a>
The name of the IAM policy that you have configured in each account where you want to deploy your permission set.
*Required*: Yes
*Type*: String
*Pattern*: `[\w+=,.@-]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Path`  <a name="cfn-sso-permissionset-customermanagedpolicyreference-path"></a>
The path to the IAM policy that you have configured in each account where you want to deploy your permission set. The default is `/`. For more information, see [Friendly names and paths](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names) in the *IAM User Guide*.
*Required*: No
*Type*: String
*Pattern*: `((/[A-Za-z0-9\.,\+@=_-]+)*)/`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
