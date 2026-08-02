---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-parsevpc.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer ParseVPC
<a name="aws-properties-logs-transformer-parsevpc"></a>

Use this processor to parse Amazon VPC vended logs, extract fields, and and convert them into a JSON format. This processor always processes the entire log event message.

This processor doesn't support custom log formats, such as NAT gateway logs. For more information about custom log formats in Amazon VPC, see [ parseVPC](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-records-examples.html#flow-log-example-tcp-flag) For more information about this processor including examples, see [ parseVPC](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseVPC).

**Important**
If you use this processor, it must be the first processor in your transformer.

## Syntax
<a name="aws-properties-logs-transformer-parsevpc-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-parsevpc-syntax.json"></a>

```
{
  "[Source](#cfn-logs-transformer-parsevpc-source)" : {{String}}
}
```

### YAML
<a name="aws-properties-logs-transformer-parsevpc-syntax.yaml"></a>

```
  [Source](#cfn-logs-transformer-parsevpc-source): {{String}}
```

## Properties
<a name="aws-properties-logs-transformer-parsevpc-properties"></a>

`Source`  <a name="cfn-logs-transformer-parsevpc-source"></a>
Omit this parameter and the whole log message will be processed by this processor. No other value than `@message` is allowed for `source`.
*Required*: No
*Type*: String
*Pattern*: `^.*[a-zA-Z0-9]+.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
