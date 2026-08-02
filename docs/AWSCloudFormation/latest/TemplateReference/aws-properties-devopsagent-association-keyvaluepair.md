---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-keyvaluepair.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association KeyValuePair
<a name="aws-properties-devopsagent-association-keyvaluepair"></a>

A key-value pair for tags.

## Syntax
<a name="aws-properties-devopsagent-association-keyvaluepair-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-keyvaluepair-syntax.json"></a>

```
{
  "[Key](#cfn-devopsagent-association-keyvaluepair-key)" : {{String}},
  "[Value](#cfn-devopsagent-association-keyvaluepair-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-keyvaluepair-syntax.yaml"></a>

```
  [Key](#cfn-devopsagent-association-keyvaluepair-key): {{String}}
  [Value](#cfn-devopsagent-association-keyvaluepair-value): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-association-keyvaluepair-properties"></a>

`Key`  <a name="cfn-devopsagent-association-keyvaluepair-key"></a>
The key name of the tag.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-devopsagent-association-keyvaluepair-value"></a>
The value for the tag.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
