---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-trimstring.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer TrimString
<a name="aws-properties-logs-transformer-trimstring"></a>

Use this processor to remove leading and trailing whitespace.

For more information about this processor including examples, see [ trimString](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-trimString) in the *CloudWatch Logs User Guide*.

## Syntax
<a name="aws-properties-logs-transformer-trimstring-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-trimstring-syntax.json"></a>

```
{
  "[WithKeys](#cfn-logs-transformer-trimstring-withkeys)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-logs-transformer-trimstring-syntax.yaml"></a>

```
  [WithKeys](#cfn-logs-transformer-trimstring-withkeys): {{
    - String}}
```

## Properties
<a name="aws-properties-logs-transformer-trimstring-properties"></a>

`WithKeys`  <a name="cfn-logs-transformer-trimstring-withkeys"></a>
The array containing the keys of the fields to trim.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
