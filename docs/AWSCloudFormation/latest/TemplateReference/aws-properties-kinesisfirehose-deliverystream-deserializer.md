---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-deserializer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream Deserializer
<a name="aws-properties-kinesisfirehose-deliverystream-deserializer"></a>

The deserializer you want Kinesis Data Firehose to use for converting the input data from JSON. Kinesis Data Firehose then serializes the data to its final format using the `Serializer`. Kinesis Data Firehose supports two types of deserializers: the [Apache Hive JSON SerDe](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL#LanguageManualDDL-JSON) and the [OpenX JSON SerDe](https://github.com/rcongiu/Hive-JSON-Serde).

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-deserializer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-deserializer-syntax.json"></a>

```
{
  "[HiveJsonSerDe](#cfn-kinesisfirehose-deliverystream-deserializer-hivejsonserde)" : {{HiveJsonSerDe}},
  "[OpenXJsonSerDe](#cfn-kinesisfirehose-deliverystream-deserializer-openxjsonserde)" : {{OpenXJsonSerDe}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-deserializer-syntax.yaml"></a>

```
  [HiveJsonSerDe](#cfn-kinesisfirehose-deliverystream-deserializer-hivejsonserde): {{
    HiveJsonSerDe}}
  [OpenXJsonSerDe](#cfn-kinesisfirehose-deliverystream-deserializer-openxjsonserde): {{
    OpenXJsonSerDe}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-deserializer-properties"></a>

`HiveJsonSerDe`  <a name="cfn-kinesisfirehose-deliverystream-deserializer-hivejsonserde"></a>
The native Hive / HCatalog JsonSerDe. Used by Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the OpenX SerDe.
*Required*: No
*Type*: [HiveJsonSerDe](aws-properties-kinesisfirehose-deliverystream-hivejsonserde.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OpenXJsonSerDe`  <a name="cfn-kinesisfirehose-deliverystream-deserializer-openxjsonserde"></a>
The OpenX SerDe. Used by Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the native Hive / HCatalog JsonSerDe.
*Required*: No
*Type*: [OpenXJsonSerDe](aws-properties-kinesisfirehose-deliverystream-openxjsonserde.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
