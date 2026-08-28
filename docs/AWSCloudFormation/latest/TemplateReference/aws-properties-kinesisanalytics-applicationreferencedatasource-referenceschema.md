---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalytics-applicationreferencedatasource-referenceschema.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalytics::ApplicationReferenceDataSource ReferenceSchema
<a name="aws-properties-kinesisanalytics-applicationreferencedatasource-referenceschema"></a>

The ReferenceSchema property type specifies the format of the data in the reference source for a SQL-based Amazon Kinesis Data Analytics application.

## Syntax
<a name="aws-properties-kinesisanalytics-applicationreferencedatasource-referenceschema-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalytics-applicationreferencedatasource-referenceschema-syntax.json"></a>

```
{
  "[RecordColumns](#cfn-kinesisanalytics-applicationreferencedatasource-referenceschema-recordcolumns)" : {{[ RecordColumn, ... ]}},
  "[RecordEncoding](#cfn-kinesisanalytics-applicationreferencedatasource-referenceschema-recordencoding)" : {{String}},
  "[RecordFormat](#cfn-kinesisanalytics-applicationreferencedatasource-referenceschema-recordformat)" : {{RecordFormat}}
}
```

### YAML
<a name="aws-properties-kinesisanalytics-applicationreferencedatasource-referenceschema-syntax.yaml"></a>

```
  [RecordColumns](#cfn-kinesisanalytics-applicationreferencedatasource-referenceschema-recordcolumns): {{
    - RecordColumn}}
  [RecordEncoding](#cfn-kinesisanalytics-applicationreferencedatasource-referenceschema-recordencoding): {{String}}
  [RecordFormat](#cfn-kinesisanalytics-applicationreferencedatasource-referenceschema-recordformat): {{
    RecordFormat}}
```

## Properties
<a name="aws-properties-kinesisanalytics-applicationreferencedatasource-referenceschema-properties"></a>

`RecordColumns`  <a name="cfn-kinesisanalytics-applicationreferencedatasource-referenceschema-recordcolumns"></a>
A list of RecordColumn objects.
*Required*: Yes
*Type*: Array of [RecordColumn](aws-properties-kinesisanalytics-applicationreferencedatasource-recordcolumn.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecordEncoding`  <a name="cfn-kinesisanalytics-applicationreferencedatasource-referenceschema-recordencoding"></a>
Specifies the encoding of the records in the reference source. For example, UTF-8.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecordFormat`  <a name="cfn-kinesisanalytics-applicationreferencedatasource-referenceschema-recordformat"></a>
Specifies the format of the records on the reference source.
*Required*: Yes
*Type*: [RecordFormat](aws-properties-kinesisanalytics-applicationreferencedatasource-recordformat.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
