---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sso-application-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSO::Application Tag
<a name="aws-properties-sso-application-tag"></a>

A set of key-value pairs that are used to manage the resource. Tags can only be applied to permission sets and cannot be applied to corresponding roles that IAM Identity Center creates in AWS accounts.

## Syntax
<a name="aws-properties-sso-application-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sso-application-tag-syntax.json"></a>

```
{
  "[Key](#cfn-sso-application-tag-key)" : {{String}},
  "[Value](#cfn-sso-application-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-sso-application-tag-syntax.yaml"></a>

```
  [Key](#cfn-sso-application-tag-key): {{String}}
  [Value](#cfn-sso-application-tag-value): {{String}}
```

## Properties
<a name="aws-properties-sso-application-tag-properties"></a>

`Key`  <a name="cfn-sso-application-tag-key"></a>
The key for the tag.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w+=,.@-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-sso-application-tag-value"></a>
The value of the tag.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w+=,.@-]+$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
