---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-application-inputschema.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Application InputSchema
<a name="aws-properties-kinesisanalyticsv2-application-inputschema"></a>

For a SQL-based Kinesis Data Analytics application, describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.

## Syntax
<a name="aws-properties-kinesisanalyticsv2-application-inputschema-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-application-inputschema-syntax.json"></a>

```
{
  "[RecordColumns](#cfn-kinesisanalyticsv2-application-inputschema-recordcolumns)" : {{[ RecordColumn, ... ]}},
  "[RecordEncoding](#cfn-kinesisanalyticsv2-application-inputschema-recordencoding)" : {{String}},
  "[RecordFormat](#cfn-kinesisanalyticsv2-application-inputschema-recordformat)" : {{RecordFormat}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-application-inputschema-syntax.yaml"></a>

```
  [RecordColumns](#cfn-kinesisanalyticsv2-application-inputschema-recordcolumns): {{
    - RecordColumn}}
  [RecordEncoding](#cfn-kinesisanalyticsv2-application-inputschema-recordencoding): {{String}}
  [RecordFormat](#cfn-kinesisanalyticsv2-application-inputschema-recordformat): {{
    RecordFormat}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-application-inputschema-properties"></a>

`RecordColumns`  <a name="cfn-kinesisanalyticsv2-application-inputschema-recordcolumns"></a>
A list of `RecordColumn` objects.
*Required*: Yes
*Type*: Array of [RecordColumn](aws-properties-kinesisanalyticsv2-application-recordcolumn.md)
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecordEncoding`  <a name="cfn-kinesisanalyticsv2-application-inputschema-recordencoding"></a>
Specifies the encoding of the records in the streaming source. For example, UTF-8.
*Required*: No
*Type*: String
*Allowed values*: `UTF-8`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecordFormat`  <a name="cfn-kinesisanalyticsv2-application-inputschema-recordformat"></a>
Specifies the format of the records on the streaming source.
*Required*: Yes
*Type*: [RecordFormat](aws-properties-kinesisanalyticsv2-application-recordformat.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-kinesisanalyticsv2-application-inputschema--seealso"></a>
+ [SourceSchema](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_SourceSchema.html) in the *Amazon Kinesis Data Analytics API Reference*
