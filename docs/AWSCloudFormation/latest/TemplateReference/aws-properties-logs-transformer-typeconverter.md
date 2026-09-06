---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-typeconverter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer TypeConverter
<a name="aws-properties-logs-transformer-typeconverter"></a>

Use this processor to convert a value type associated with the specified key to the specified type. It's a casting processor that changes the types of the specified fields. Values can be converted into one of the following datatypes: `integer`, `double`, `string` and `boolean`.

For more information about this processor including examples, see [ trimString](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-trimString) in the *CloudWatch Logs User Guide*.

## Syntax
<a name="aws-properties-logs-transformer-typeconverter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-typeconverter-syntax.json"></a>

```
{
  "[Entries](#cfn-logs-transformer-typeconverter-entries)" : {{[ TypeConverterEntry, ... ]}}
}
```

### YAML
<a name="aws-properties-logs-transformer-typeconverter-syntax.yaml"></a>

```
  [Entries](#cfn-logs-transformer-typeconverter-entries): {{
    - TypeConverterEntry}}
```

## Properties
<a name="aws-properties-logs-transformer-typeconverter-properties"></a>

`Entries`  <a name="cfn-logs-transformer-typeconverter-entries"></a>
An array of `TypeConverterEntry` objects, where each object contains the information about one field to change the type of.
*Required*: Yes
*Type*: Array of [TypeConverterEntry](aws-properties-logs-transformer-typeconverterentry.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
