---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-index-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::Index Tag
<a name="aws-properties-qbusiness-index-tag"></a>

A list of key/value pairs that identify an index, FAQ, or data source. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: \_ . : / = \+ - @.

## Syntax
<a name="aws-properties-qbusiness-index-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-index-tag-syntax.json"></a>

```
{
  "[Key](#cfn-qbusiness-index-tag-key)" : {{String}},
  "[Value](#cfn-qbusiness-index-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-qbusiness-index-tag-syntax.yaml"></a>

```
  [Key](#cfn-qbusiness-index-tag-key): {{String}}
  [Value](#cfn-qbusiness-index-tag-value): {{String}}
```

## Properties
<a name="aws-properties-qbusiness-index-tag-properties"></a>

`Key`  <a name="cfn-qbusiness-index-tag-key"></a>
 The key for the tag. Keys are not case sensitive and must be unique for the Amazon Q Business application or data source.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-qbusiness-index-tag-value"></a>
The value associated with the tag. The value may be an empty string but it can't be null.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
