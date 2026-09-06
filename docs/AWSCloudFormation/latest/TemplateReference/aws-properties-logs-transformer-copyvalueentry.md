---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-copyvalueentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer CopyValueEntry
<a name="aws-properties-logs-transformer-copyvalueentry"></a>

This object defines one value to be copied with the [ copyValue](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-copyValue) processor.

## Syntax
<a name="aws-properties-logs-transformer-copyvalueentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-copyvalueentry-syntax.json"></a>

```
{
  "[OverwriteIfExists](#cfn-logs-transformer-copyvalueentry-overwriteifexists)" : {{Boolean}},
  "[Source](#cfn-logs-transformer-copyvalueentry-source)" : {{String}},
  "[Target](#cfn-logs-transformer-copyvalueentry-target)" : {{String}}
}
```

### YAML
<a name="aws-properties-logs-transformer-copyvalueentry-syntax.yaml"></a>

```
  [OverwriteIfExists](#cfn-logs-transformer-copyvalueentry-overwriteifexists): {{Boolean}}
  [Source](#cfn-logs-transformer-copyvalueentry-source): {{String}}
  [Target](#cfn-logs-transformer-copyvalueentry-target): {{String}}
```

## Properties
<a name="aws-properties-logs-transformer-copyvalueentry-properties"></a>

`OverwriteIfExists`  <a name="cfn-logs-transformer-copyvalueentry-overwriteifexists"></a>
Specifies whether to overwrite the value if the destination key already exists. If you omit this, the default is `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-logs-transformer-copyvalueentry-source"></a>
The key to copy.
*Required*: Yes
*Type*: String
*Pattern*: `^.*[a-zA-Z0-9]+.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Target`  <a name="cfn-logs-transformer-copyvalueentry-target"></a>
The key of the field to copy the value to.
*Required*: Yes
*Type*: String
*Pattern*: `^.*[a-zA-Z0-9]+.*$`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
