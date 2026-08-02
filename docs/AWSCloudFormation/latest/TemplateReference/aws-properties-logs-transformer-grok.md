---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-grok.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer Grok
<a name="aws-properties-logs-transformer-grok"></a>

This processor uses pattern matching to parse and structure unstructured data. This processor can also extract fields from log messages.

For more information about this processor including examples, see [ grok](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-Grok) in the *CloudWatch Logs User Guide*.

## Syntax
<a name="aws-properties-logs-transformer-grok-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-grok-syntax.json"></a>

```
{
  "[Match](#cfn-logs-transformer-grok-match)" : {{String}},
  "[Source](#cfn-logs-transformer-grok-source)" : {{String}}
}
```

### YAML
<a name="aws-properties-logs-transformer-grok-syntax.yaml"></a>

```
  [Match](#cfn-logs-transformer-grok-match): {{String}}
  [Source](#cfn-logs-transformer-grok-source): {{String}}
```

## Properties
<a name="aws-properties-logs-transformer-grok-properties"></a>

`Match`  <a name="cfn-logs-transformer-grok-match"></a>
The grok pattern to match against the log event. For a list of supported grok patterns, see [Supported grok patterns](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#Grok-Patterns).
*Required*: Yes
*Type*: String
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-logs-transformer-grok-source"></a>
The path to the field in the log event that you want to parse. If you omit this value, the whole log message is parsed.
*Required*: No
*Type*: String
*Pattern*: `^.*[a-zA-Z0-9]+.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
