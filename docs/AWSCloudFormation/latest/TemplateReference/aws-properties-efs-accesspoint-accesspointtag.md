---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-efs-accesspoint-accesspointtag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EFS::AccessPoint AccessPointTag
<a name="aws-properties-efs-accesspoint-accesspointtag"></a>

A tag is a key-value pair attached to a file system. Allowed characters in the `Key` and `Value` properties are letters, white space, and numbers that can be represented in UTF-8, and the following characters:` + - = . _ : /`

## Syntax
<a name="aws-properties-efs-accesspoint-accesspointtag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-efs-accesspoint-accesspointtag-syntax.json"></a>

```
{
  "[Key](#cfn-efs-accesspoint-accesspointtag-key)" : {{String}},
  "[Value](#cfn-efs-accesspoint-accesspointtag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-efs-accesspoint-accesspointtag-syntax.yaml"></a>

```
  [Key](#cfn-efs-accesspoint-accesspointtag-key): {{String}}
  [Value](#cfn-efs-accesspoint-accesspointtag-value): {{String}}
```

## Properties
<a name="aws-properties-efs-accesspoint-accesspointtag-properties"></a>

`Key`  <a name="cfn-efs-accesspoint-accesspointtag-key"></a>
The tag key (String). The key can't start with `aws:`.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-efs-accesspoint-accesspointtag-value"></a>
The value of the tag key.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
