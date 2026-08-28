---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-application-recordformat.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Application RecordFormat
<a name="aws-properties-kinesisanalyticsv2-application-recordformat"></a>

 For a SQL-based Kinesis Data Analytics application, describes the record format and relevant mapping information that should be applied to schematize the records on the stream.

## Syntax
<a name="aws-properties-kinesisanalyticsv2-application-recordformat-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-application-recordformat-syntax.json"></a>

```
{
  "[MappingParameters](#cfn-kinesisanalyticsv2-application-recordformat-mappingparameters)" : {{MappingParameters}},
  "[RecordFormatType](#cfn-kinesisanalyticsv2-application-recordformat-recordformattype)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-application-recordformat-syntax.yaml"></a>

```
  [MappingParameters](#cfn-kinesisanalyticsv2-application-recordformat-mappingparameters): {{
    MappingParameters}}
  [RecordFormatType](#cfn-kinesisanalyticsv2-application-recordformat-recordformattype): {{String}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-application-recordformat-properties"></a>

`MappingParameters`  <a name="cfn-kinesisanalyticsv2-application-recordformat-mappingparameters"></a>
When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.
*Required*: No
*Type*: [MappingParameters](aws-properties-kinesisanalyticsv2-application-mappingparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecordFormatType`  <a name="cfn-kinesisanalyticsv2-application-recordformat-recordformattype"></a>
The type of record format.
*Required*: Yes
*Type*: String
*Allowed values*: `CSV | JSON`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-kinesisanalyticsv2-application-recordformat--seealso"></a>
+ [RecordFormat](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_RecordFormat.html) in the *Amazon Kinesis Data Analytics API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
