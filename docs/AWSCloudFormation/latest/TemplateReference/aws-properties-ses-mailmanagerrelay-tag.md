---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerrelay-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRelay Tag
<a name="aws-properties-ses-mailmanagerrelay-tag"></a>

A key-value pair (the value is optional), that you can define and assign to AWS resources.

## Syntax
<a name="aws-properties-ses-mailmanagerrelay-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerrelay-tag-syntax.json"></a>

```
{
  "[Key](#cfn-ses-mailmanagerrelay-tag-key)" : {{String}},
  "[Value](#cfn-ses-mailmanagerrelay-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerrelay-tag-syntax.yaml"></a>

```
  [Key](#cfn-ses-mailmanagerrelay-tag-key): {{String}}
  [Value](#cfn-ses-mailmanagerrelay-tag-value): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagerrelay-tag-properties"></a>

`Key`  <a name="cfn-ses-mailmanagerrelay-tag-key"></a>
The key of the key-value tag.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9/_\+=\.:@\-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-ses-mailmanagerrelay-tag-value"></a>
The value of the key-value tag.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9/_\+=\.:@\-]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
