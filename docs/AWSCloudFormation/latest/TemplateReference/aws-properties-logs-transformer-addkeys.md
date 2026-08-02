---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-addkeys.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer AddKeys
<a name="aws-properties-logs-transformer-addkeys"></a>

This processor adds new key-value pairs to the log event.

For more information about this processor including examples, see [ addKeys](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-addKeys) in the *CloudWatch Logs User Guide*.

## Syntax
<a name="aws-properties-logs-transformer-addkeys-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-addkeys-syntax.json"></a>

```
{
  "[Entries](#cfn-logs-transformer-addkeys-entries)" : {{[ AddKeyEntry, ... ]}}
}
```

### YAML
<a name="aws-properties-logs-transformer-addkeys-syntax.yaml"></a>

```
  [Entries](#cfn-logs-transformer-addkeys-entries): {{
    - AddKeyEntry}}
```

## Properties
<a name="aws-properties-logs-transformer-addkeys-properties"></a>

`Entries`  <a name="cfn-logs-transformer-addkeys-entries"></a>
An array of objects, where each object contains the information about one key to add to the log event.
*Required*: Yes
*Type*: Array of [AddKeyEntry](aws-properties-logs-transformer-addkeyentry.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
