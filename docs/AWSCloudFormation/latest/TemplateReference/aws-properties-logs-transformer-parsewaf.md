---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-parsewaf.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer ParseWAF
<a name="aws-properties-logs-transformer-parsewaf"></a>

Use this processor to parse AWS WAF vended logs, extract fields, and and convert them into a JSON format. This processor always processes the entire log event message. For more information about this processor including examples, see [ parseWAF](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-parsePostGres).

For more information about AWS WAF log format, see [ Log examples for web ACL traffic](https://docs.aws.amazon.com/waf/latest/developerguide/logging-examples.html).

**Important**
If you use this processor, it must be the first processor in your transformer.

## Syntax
<a name="aws-properties-logs-transformer-parsewaf-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-parsewaf-syntax.json"></a>

```
{
  "[Source](#cfn-logs-transformer-parsewaf-source)" : {{String}}
}
```

### YAML
<a name="aws-properties-logs-transformer-parsewaf-syntax.yaml"></a>

```
  [Source](#cfn-logs-transformer-parsewaf-source): {{String}}
```

## Properties
<a name="aws-properties-logs-transformer-parsewaf-properties"></a>

`Source`  <a name="cfn-logs-transformer-parsewaf-source"></a>
Omit this parameter and the whole log message will be processed by this processor. No other value than `@message` is allowed for `source`.
*Required*: No
*Type*: String
*Pattern*: `^.*[a-zA-Z0-9]+.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
