---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-hivejsonserde.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream HiveJsonSerDe
<a name="aws-properties-kinesisfirehose-deliverystream-hivejsonserde"></a>

The native Hive / HCatalog JsonSerDe. Used by Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the OpenX SerDe.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-hivejsonserde-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-hivejsonserde-syntax.json"></a>

```
{
  "[TimestampFormats](#cfn-kinesisfirehose-deliverystream-hivejsonserde-timestampformats)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-hivejsonserde-syntax.yaml"></a>

```
  [TimestampFormats](#cfn-kinesisfirehose-deliverystream-hivejsonserde-timestampformats): {{
    - String}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-hivejsonserde-properties"></a>

`TimestampFormats`  <a name="cfn-kinesisfirehose-deliverystream-hivejsonserde-timestampformats"></a>
Indicates how you want Firehose to parse the date and timestamps that may be present in your input data JSON. To specify these format strings, follow the pattern syntax of JodaTime's DateTimeFormat format strings. For more information, see [Class DateTimeFormat](https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html). You can also use the special value `millis` to parse timestamps in epoch milliseconds. If you don't specify a format, Firehose uses `java.sql.Timestamp::valueOf` by default.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
