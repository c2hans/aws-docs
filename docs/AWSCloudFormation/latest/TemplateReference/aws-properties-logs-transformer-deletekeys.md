---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-deletekeys.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer DeleteKeys
<a name="aws-properties-logs-transformer-deletekeys"></a>

This processor deletes entries from a log event. These entries are key-value pairs.

For more information about this processor including examples, see [ deleteKeys](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-deleteKeys) in the *CloudWatch Logs User Guide*.

## Syntax
<a name="aws-properties-logs-transformer-deletekeys-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-deletekeys-syntax.json"></a>

```
{
  "[WithKeys](#cfn-logs-transformer-deletekeys-withkeys)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-logs-transformer-deletekeys-syntax.yaml"></a>

```
  [WithKeys](#cfn-logs-transformer-deletekeys-withkeys): {{
    - String}}
```

## Properties
<a name="aws-properties-logs-transformer-deletekeys-properties"></a>

`WithKeys`  <a name="cfn-logs-transformer-deletekeys-withkeys"></a>
The list of keys to delete.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
