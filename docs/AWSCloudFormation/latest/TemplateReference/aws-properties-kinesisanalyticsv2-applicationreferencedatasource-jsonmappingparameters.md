---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-jsonmappingparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource JSONMappingParameters
<a name="aws-properties-kinesisanalyticsv2-applicationreferencedatasource-jsonmappingparameters"></a>

For a SQL-based Kinesis Data Analytics application, provides additional mapping information when JSON is the record format on the streaming source.

## Syntax
<a name="aws-properties-kinesisanalyticsv2-applicationreferencedatasource-jsonmappingparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-applicationreferencedatasource-jsonmappingparameters-syntax.json"></a>

```
{
  "[RecordRowPath](#cfn-kinesisanalyticsv2-applicationreferencedatasource-jsonmappingparameters-recordrowpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-applicationreferencedatasource-jsonmappingparameters-syntax.yaml"></a>

```
  [RecordRowPath](#cfn-kinesisanalyticsv2-applicationreferencedatasource-jsonmappingparameters-recordrowpath): {{String}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-applicationreferencedatasource-jsonmappingparameters-properties"></a>

`RecordRowPath`  <a name="cfn-kinesisanalyticsv2-applicationreferencedatasource-jsonmappingparameters-recordrowpath"></a>
The path to the top-level parent that contains the records.
*Required*: Yes
*Type*: String
*Pattern*: `^(?=^\$)(?=^\S+$).*$`
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-kinesisanalyticsv2-applicationreferencedatasource-jsonmappingparameters--seealso"></a>
+ [JSONMappingParameters](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_JSONMappingParameters.html) in the *Amazon Kinesis Data Analytics API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
