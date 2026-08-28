---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkmanager-connectattachment-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkManager::ConnectAttachment Tag
<a name="aws-properties-networkmanager-connectattachment-tag"></a>

Describes a tag.

## Syntax
<a name="aws-properties-networkmanager-connectattachment-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkmanager-connectattachment-tag-syntax.json"></a>

```
{
  "[Key](#cfn-networkmanager-connectattachment-tag-key)" : {{String}},
  "[Value](#cfn-networkmanager-connectattachment-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-networkmanager-connectattachment-tag-syntax.yaml"></a>

```
  [Key](#cfn-networkmanager-connectattachment-tag-key): {{String}}
  [Value](#cfn-networkmanager-connectattachment-tag-value): {{String}}
```

## Properties
<a name="aws-properties-networkmanager-connectattachment-tag-properties"></a>

`Key`  <a name="cfn-networkmanager-connectattachment-tag-key"></a>
The tag key.
Constraints: Maximum length of 128 characters.
*Required*: Yes
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `0`
*Maximum*: `10000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-networkmanager-connectattachment-tag-value"></a>
The tag value.
Constraints: Maximum length of 256 characters.
*Required*: Yes
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `0`
*Maximum*: `10000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
