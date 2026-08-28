---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalytics-applicationoutput-destinationschema.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalytics::ApplicationOutput DestinationSchema
<a name="aws-properties-kinesisanalytics-applicationoutput-destinationschema"></a>

Describes the data format when records are written to the destination. For more information, see [Configuring Application Output](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html).

## Syntax
<a name="aws-properties-kinesisanalytics-applicationoutput-destinationschema-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalytics-applicationoutput-destinationschema-syntax.json"></a>

```
{
  "[RecordFormatType](#cfn-kinesisanalytics-applicationoutput-destinationschema-recordformattype)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisanalytics-applicationoutput-destinationschema-syntax.yaml"></a>

```
  [RecordFormatType](#cfn-kinesisanalytics-applicationoutput-destinationschema-recordformattype): {{String}}
```

## Properties
<a name="aws-properties-kinesisanalytics-applicationoutput-destinationschema-properties"></a>

`RecordFormatType`  <a name="cfn-kinesisanalytics-applicationoutput-destinationschema-recordformattype"></a>
Specifies the format of the records on the output stream.
*Required*: No
*Type*: String
*Allowed values*: `JSON | CSV`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
