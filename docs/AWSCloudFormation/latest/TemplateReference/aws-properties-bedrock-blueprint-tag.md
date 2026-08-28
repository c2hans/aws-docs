---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-blueprint-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Blueprint Tag
<a name="aws-properties-bedrock-blueprint-tag"></a>

A tag associated with a resource. A tag consists of a key and value.

## Syntax
<a name="aws-properties-bedrock-blueprint-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-blueprint-tag-syntax.json"></a>

```
{
  "[Key](#cfn-bedrock-blueprint-tag-key)" : {{String}},
  "[Value](#cfn-bedrock-blueprint-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-blueprint-tag-syntax.yaml"></a>

```
  [Key](#cfn-bedrock-blueprint-tag-key): {{String}}
  [Value](#cfn-bedrock-blueprint-tag-value): {{String}}
```

## Properties
<a name="aws-properties-bedrock-blueprint-tag-properties"></a>

`Key`  <a name="cfn-bedrock-blueprint-tag-key"></a>
The key associated with a tag.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-bedrock-blueprint-tag-value"></a>
The value associated with a tag.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
