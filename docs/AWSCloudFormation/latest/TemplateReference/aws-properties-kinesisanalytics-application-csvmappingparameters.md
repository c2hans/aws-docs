---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalytics-application-csvmappingparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalytics::Application CSVMappingParameters
<a name="aws-properties-kinesisanalytics-application-csvmappingparameters"></a>

Provides additional mapping information when the record format uses delimiters, such as CSV. For example, the following sample records use CSV format, where the records use the *'\\n'* as the row delimiter and a comma (",") as the column delimiter:

 `"name1", "address1"`

 `"name2", "address2"`

## Syntax
<a name="aws-properties-kinesisanalytics-application-csvmappingparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalytics-application-csvmappingparameters-syntax.json"></a>

```
{
  "[RecordColumnDelimiter](#cfn-kinesisanalytics-application-csvmappingparameters-recordcolumndelimiter)" : {{String}},
  "[RecordRowDelimiter](#cfn-kinesisanalytics-application-csvmappingparameters-recordrowdelimiter)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisanalytics-application-csvmappingparameters-syntax.yaml"></a>

```
  [RecordColumnDelimiter](#cfn-kinesisanalytics-application-csvmappingparameters-recordcolumndelimiter): {{String}}
  [RecordRowDelimiter](#cfn-kinesisanalytics-application-csvmappingparameters-recordrowdelimiter): {{String}}
```

## Properties
<a name="aws-properties-kinesisanalytics-application-csvmappingparameters-properties"></a>

`RecordColumnDelimiter`  <a name="cfn-kinesisanalytics-application-csvmappingparameters-recordcolumndelimiter"></a>
Column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecordRowDelimiter`  <a name="cfn-kinesisanalytics-application-csvmappingparameters-recordrowdelimiter"></a>
Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
