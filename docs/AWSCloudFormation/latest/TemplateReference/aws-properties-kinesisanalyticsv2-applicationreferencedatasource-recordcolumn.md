---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource RecordColumn
<a name="aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn"></a>

For a SQL-based Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.

Also used to describe the format of the reference data source.

## Syntax
<a name="aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-syntax.json"></a>

```
{
  "[Mapping](#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-mapping)" : {{String}},
  "[Name](#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-name)" : {{String}},
  "[SqlType](#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-sqltype)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-syntax.yaml"></a>

```
  [Mapping](#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-mapping): {{String}}
  [Name](#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-name): {{String}}
  [SqlType](#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-sqltype): {{String}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-properties"></a>

`Mapping`  <a name="cfn-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-mapping"></a>
A reference to the data element in the streaming input or the reference data source.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-name"></a>
The name of the column that is created in the in-application input stream or reference table.
*Required*: Yes
*Type*: String
*Pattern*: `[^-\s<>&]*`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SqlType`  <a name="cfn-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-sqltype"></a>
The type of column created in the in-application input stream or reference table.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn--seealso"></a>
+ [RecordColumn](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_RecordColumn.html) in the *Amazon Kinesis Data Analytics API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
