---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-serializer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream Serializer
<a name="aws-properties-kinesisfirehose-deliverystream-serializer"></a>

The serializer that you want Firehose to use to convert data to the target format before writing it to Amazon S3. Firehose supports two types of serializers: the ORC SerDe and the Parquet SerDe.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-serializer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-serializer-syntax.json"></a>

```
{
  "[OrcSerDe](#cfn-kinesisfirehose-deliverystream-serializer-orcserde)" : {{OrcSerDe}},
  "[ParquetSerDe](#cfn-kinesisfirehose-deliverystream-serializer-parquetserde)" : {{ParquetSerDe}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-serializer-syntax.yaml"></a>

```
  [OrcSerDe](#cfn-kinesisfirehose-deliverystream-serializer-orcserde): {{
    OrcSerDe}}
  [ParquetSerDe](#cfn-kinesisfirehose-deliverystream-serializer-parquetserde): {{
    ParquetSerDe}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-serializer-properties"></a>

`OrcSerDe`  <a name="cfn-kinesisfirehose-deliverystream-serializer-orcserde"></a>
A serializer to use for converting data to the ORC format before storing it in Amazon S3. For more information, see [Apache ORC](https://orc.apache.org/docs/).
*Required*: No
*Type*: [OrcSerDe](aws-properties-kinesisfirehose-deliverystream-orcserde.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParquetSerDe`  <a name="cfn-kinesisfirehose-deliverystream-serializer-parquetserde"></a>
A serializer to use for converting data to the Parquet format before storing it in Amazon S3. For more information, see [Apache Parquet](https://parquet.apache.org/docs/contribution-guidelines/).
*Required*: No
*Type*: [ParquetSerDe](aws-properties-kinesisfirehose-deliverystream-parquetserde.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
