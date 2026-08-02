---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalytics-applicationreferencedatasource-csvmappingparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalytics::ApplicationReferenceDataSource CSVMappingParameters
<a name="aws-properties-kinesisanalytics-applicationreferencedatasource-csvmappingparameters"></a>

Provides additional mapping information when the record format uses delimiters, such as CSV. For example, the following sample records use CSV format, where the records use the *'\\n'* as the row delimiter and a comma (",") as the column delimiter:

 `"name1", "address1"`

 `"name2", "address2"`

## Syntax
<a name="aws-properties-kinesisanalytics-applicationreferencedatasource-csvmappingparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalytics-applicationreferencedatasource-csvmappingparameters-syntax.json"></a>

```
{
  "[RecordColumnDelimiter](#cfn-kinesisanalytics-applicationreferencedatasource-csvmappingparameters-recordcolumndelimiter)" : {{String}},
  "[RecordRowDelimiter](#cfn-kinesisanalytics-applicationreferencedatasource-csvmappingparameters-recordrowdelimiter)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisanalytics-applicationreferencedatasource-csvmappingparameters-syntax.yaml"></a>

```
  [RecordColumnDelimiter](#cfn-kinesisanalytics-applicationreferencedatasource-csvmappingparameters-recordcolumndelimiter): {{String}}
  [RecordRowDelimiter](#cfn-kinesisanalytics-applicationreferencedatasource-csvmappingparameters-recordrowdelimiter): {{String}}
```

## Properties
<a name="aws-properties-kinesisanalytics-applicationreferencedatasource-csvmappingparameters-properties"></a>

`RecordColumnDelimiter`  <a name="cfn-kinesisanalytics-applicationreferencedatasource-csvmappingparameters-recordcolumndelimiter"></a>
Column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecordRowDelimiter`  <a name="cfn-kinesisanalytics-applicationreferencedatasource-csvmappingparameters-recordrowdelimiter"></a>
Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
