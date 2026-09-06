---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-parseroute53.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer ParseRoute53
<a name="aws-properties-logs-transformer-parseroute53"></a>

Use this processor to parse Route 53 vended logs, extract fields, and and convert them into a JSON format. This processor always processes the entire log event message. For more information about this processor including examples, see [ parseRoute53](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-parseRoute53).

**Important**
If you use this processor, it must be the first processor in your transformer.

## Syntax
<a name="aws-properties-logs-transformer-parseroute53-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-parseroute53-syntax.json"></a>

```
{
  "[Source](#cfn-logs-transformer-parseroute53-source)" : {{String}}
}
```

### YAML
<a name="aws-properties-logs-transformer-parseroute53-syntax.yaml"></a>

```
  [Source](#cfn-logs-transformer-parseroute53-source): {{String}}
```

## Properties
<a name="aws-properties-logs-transformer-parseroute53-properties"></a>

`Source`  <a name="cfn-logs-transformer-parseroute53-source"></a>
Omit this parameter and the whole log message will be processed by this processor. No other value than `@message` is allowed for `source`.
*Required*: No
*Type*: String
*Pattern*: `^.*[a-zA-Z0-9]+.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
