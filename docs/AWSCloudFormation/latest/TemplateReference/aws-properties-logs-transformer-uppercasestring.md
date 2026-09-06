---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-uppercasestring.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer UpperCaseString
<a name="aws-properties-logs-transformer-uppercasestring"></a>

This processor converts a string field to uppercase.

For more information about this processor including examples, see [ upperCaseString](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-upperCaseString) in the *CloudWatch Logs User Guide*.

## Syntax
<a name="aws-properties-logs-transformer-uppercasestring-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-uppercasestring-syntax.json"></a>

```
{
  "[WithKeys](#cfn-logs-transformer-uppercasestring-withkeys)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-logs-transformer-uppercasestring-syntax.yaml"></a>

```
  [WithKeys](#cfn-logs-transformer-uppercasestring-withkeys): {{
    - String}}
```

## Properties
<a name="aws-properties-logs-transformer-uppercasestring-properties"></a>

`WithKeys`  <a name="cfn-logs-transformer-uppercasestring-withkeys"></a>
The array of containing the keys of the field to convert to uppercase.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
