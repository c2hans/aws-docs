---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalytics-applicationreferencedatasource-recordcolumn.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalytics::ApplicationReferenceDataSource RecordColumn
<a name="aws-properties-kinesisanalytics-applicationreferencedatasource-recordcolumn"></a>

Describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.

Also used to describe the format of the reference data source.

## Syntax
<a name="aws-properties-kinesisanalytics-applicationreferencedatasource-recordcolumn-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalytics-applicationreferencedatasource-recordcolumn-syntax.json"></a>

```
{
  "[Mapping](#cfn-kinesisanalytics-applicationreferencedatasource-recordcolumn-mapping)" : {{String}},
  "[Name](#cfn-kinesisanalytics-applicationreferencedatasource-recordcolumn-name)" : {{String}},
  "[SqlType](#cfn-kinesisanalytics-applicationreferencedatasource-recordcolumn-sqltype)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisanalytics-applicationreferencedatasource-recordcolumn-syntax.yaml"></a>

```
  [Mapping](#cfn-kinesisanalytics-applicationreferencedatasource-recordcolumn-mapping): {{String}}
  [Name](#cfn-kinesisanalytics-applicationreferencedatasource-recordcolumn-name): {{String}}
  [SqlType](#cfn-kinesisanalytics-applicationreferencedatasource-recordcolumn-sqltype): {{String}}
```

## Properties
<a name="aws-properties-kinesisanalytics-applicationreferencedatasource-recordcolumn-properties"></a>

`Mapping`  <a name="cfn-kinesisanalytics-applicationreferencedatasource-recordcolumn-mapping"></a>
Reference to the data element in the streaming input or the reference data source. This element is required if the [RecordFormatType](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel) is `JSON`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-kinesisanalytics-applicationreferencedatasource-recordcolumn-name"></a>
Name of the column created in the in-application input stream or reference table.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SqlType`  <a name="cfn-kinesisanalytics-applicationreferencedatasource-recordcolumn-sqltype"></a>
Type of column created in the in-application input stream or reference table.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
