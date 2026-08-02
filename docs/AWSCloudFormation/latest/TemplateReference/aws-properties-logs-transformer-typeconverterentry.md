---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-typeconverterentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer TypeConverterEntry
<a name="aws-properties-logs-transformer-typeconverterentry"></a>

This object defines one value type that will be converted using the [ typeConverter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-typeConverter) processor.

## Syntax
<a name="aws-properties-logs-transformer-typeconverterentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-typeconverterentry-syntax.json"></a>

```
{
  "[Key](#cfn-logs-transformer-typeconverterentry-key)" : {{String}},
  "[Type](#cfn-logs-transformer-typeconverterentry-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-logs-transformer-typeconverterentry-syntax.yaml"></a>

```
  [Key](#cfn-logs-transformer-typeconverterentry-key): {{String}}
  [Type](#cfn-logs-transformer-typeconverterentry-type): {{String}}
```

## Properties
<a name="aws-properties-logs-transformer-typeconverterentry-properties"></a>

`Key`  <a name="cfn-logs-transformer-typeconverterentry-key"></a>
The key with the value that is to be converted to a different type.
*Required*: Yes
*Type*: String
*Pattern*: `^.*[a-zA-Z0-9]+.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-logs-transformer-typeconverterentry-type"></a>
The type to convert the field value to. Valid values are `integer`, `double`, `string` and `boolean`.
*Required*: Yes
*Type*: String
*Allowed values*: `boolean | integer | double | string`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
