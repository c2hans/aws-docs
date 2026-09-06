---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-destination-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Destination Tag
<a name="aws-properties-logs-destination-tag"></a>

The tag value assigned to the log destination.

## Syntax
<a name="aws-properties-logs-destination-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-destination-tag-syntax.json"></a>

```
{
  "[Key](#cfn-logs-destination-tag-key)" : {{String}},
  "[Value](#cfn-logs-destination-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-logs-destination-tag-syntax.yaml"></a>

```
  [Key](#cfn-logs-destination-tag-key): {{String}}
  [Value](#cfn-logs-destination-tag-value): {{String}}
```

## Properties
<a name="aws-properties-logs-destination-tag-properties"></a>

`Key`  <a name="cfn-logs-destination-tag-key"></a>
An optional list of key-value pairs to associate with the resource.
For more information about tagging, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html)
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-logs-destination-tag-value"></a>
The list of tags associated with the requested resource.>
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
