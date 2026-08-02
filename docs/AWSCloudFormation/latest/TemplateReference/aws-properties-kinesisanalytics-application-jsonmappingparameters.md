---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalytics-application-jsonmappingparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalytics::Application JSONMappingParameters
<a name="aws-properties-kinesisanalytics-application-jsonmappingparameters"></a>

Provides additional mapping information when JSON is the record format on the streaming source.

## Syntax
<a name="aws-properties-kinesisanalytics-application-jsonmappingparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalytics-application-jsonmappingparameters-syntax.json"></a>

```
{
  "[RecordRowPath](#cfn-kinesisanalytics-application-jsonmappingparameters-recordrowpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisanalytics-application-jsonmappingparameters-syntax.yaml"></a>

```
  [RecordRowPath](#cfn-kinesisanalytics-application-jsonmappingparameters-recordrowpath): {{String}}
```

## Properties
<a name="aws-properties-kinesisanalytics-application-jsonmappingparameters-properties"></a>

`RecordRowPath`  <a name="cfn-kinesisanalytics-application-jsonmappingparameters-recordrowpath"></a>
Path to the top-level parent that contains the records.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
