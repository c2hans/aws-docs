---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesis-channel-recordconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kinesis::Channel RecordConfiguration
<a name="aws-properties-kinesis-channel-recordconfiguration"></a>

Specifies the format of records read from the source stream.

## Syntax
<a name="aws-properties-kinesis-channel-recordconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesis-channel-recordconfiguration-syntax.json"></a>

```
{
  "[GSRSchemaARN](#cfn-kinesis-channel-recordconfiguration-gsrschemaarn)" : {{String}},
  "[RecordFormatType](#cfn-kinesis-channel-recordconfiguration-recordformattype)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesis-channel-recordconfiguration-syntax.yaml"></a>

```
  [GSRSchemaARN](#cfn-kinesis-channel-recordconfiguration-gsrschemaarn): {{String}}
  [RecordFormatType](#cfn-kinesis-channel-recordconfiguration-recordformattype): {{String}}
```

## Properties
<a name="aws-properties-kinesis-channel-recordconfiguration-properties"></a>

`GSRSchemaARN`  <a name="cfn-kinesis-channel-recordconfiguration-gsrschemaarn"></a>
The Amazon Resource Name (ARN) of the AWS Glue Schema Registry schema used to validate records. Required when the channel destination is a streaming table.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:glue:[-a-z0-9]+:\d{12}:schema/[-a-zA-Z0-9_$#.]+/[-a-zA-Z0-9_$#.]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RecordFormatType`  <a name="cfn-kinesis-channel-recordconfiguration-recordformattype"></a>
The format of records on the source stream. Valid values:
+ `GSR_JSON` - Supported only for streaming table (Amazon S3 Tables) destinations.
+ `JSON` - Supported for both general purpose Amazon S3 and streaming table destinations.
+ `STRING` - Supported only for general purpose Amazon S3 destinations.
+ `BYTE_ARRAY` - Supported only for general purpose Amazon S3 destinations.
*Required*: Yes
*Type*: String
*Allowed values*: `GSR_JSON | JSON | STRING | BYTE_ARRAY`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
