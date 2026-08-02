---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-addkeyentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer AddKeyEntry
<a name="aws-properties-logs-transformer-addkeyentry"></a>

This object defines one key that will be added with the [ addKeys](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-addKey) processor.

## Syntax
<a name="aws-properties-logs-transformer-addkeyentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-addkeyentry-syntax.json"></a>

```
{
  "[Key](#cfn-logs-transformer-addkeyentry-key)" : {{String}},
  "[OverwriteIfExists](#cfn-logs-transformer-addkeyentry-overwriteifexists)" : {{Boolean}},
  "[Value](#cfn-logs-transformer-addkeyentry-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-logs-transformer-addkeyentry-syntax.yaml"></a>

```
  [Key](#cfn-logs-transformer-addkeyentry-key): {{String}}
  [OverwriteIfExists](#cfn-logs-transformer-addkeyentry-overwriteifexists): {{Boolean}}
  [Value](#cfn-logs-transformer-addkeyentry-value): {{String}}
```

## Properties
<a name="aws-properties-logs-transformer-addkeyentry-properties"></a>

`Key`  <a name="cfn-logs-transformer-addkeyentry-key"></a>
The key of the new entry to be added to the log event
*Required*: Yes
*Type*: String
*Pattern*: `^.*[a-zA-Z0-9]+.*$`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OverwriteIfExists`  <a name="cfn-logs-transformer-addkeyentry-overwriteifexists"></a>
Specifies whether to overwrite the value if the key already exists in the log event. If you omit this, the default is `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-logs-transformer-addkeyentry-value"></a>
The value of the new entry to be added to the log event
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
