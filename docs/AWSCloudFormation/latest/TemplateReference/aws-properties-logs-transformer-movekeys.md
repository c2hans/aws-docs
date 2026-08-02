---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-movekeys.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer MoveKeys
<a name="aws-properties-logs-transformer-movekeys"></a>

This processor moves a key from one field to another. The original key is deleted.

For more information about this processor including examples, see [ moveKeys](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-moveKeys) in the *CloudWatch Logs User Guide*.

## Syntax
<a name="aws-properties-logs-transformer-movekeys-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-movekeys-syntax.json"></a>

```
{
  "[Entries](#cfn-logs-transformer-movekeys-entries)" : {{[ MoveKeyEntry, ... ]}}
}
```

### YAML
<a name="aws-properties-logs-transformer-movekeys-syntax.yaml"></a>

```
  [Entries](#cfn-logs-transformer-movekeys-entries): {{
    - MoveKeyEntry}}
```

## Properties
<a name="aws-properties-logs-transformer-movekeys-properties"></a>

`Entries`  <a name="cfn-logs-transformer-movekeys-entries"></a>
An array of objects, where each object contains the information about one key to move.
*Required*: Yes
*Type*: Array of [MoveKeyEntry](aws-properties-logs-transformer-movekeyentry.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
