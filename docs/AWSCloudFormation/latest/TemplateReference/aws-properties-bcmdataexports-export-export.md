---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bcmdataexports-export-export.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BCMDataExports::Export Export
<a name="aws-properties-bcmdataexports-export-export"></a>

The details that are available for an export.

## Syntax
<a name="aws-properties-bcmdataexports-export-export-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bcmdataexports-export-export-syntax.json"></a>

```
{
  "[DataQuery](#cfn-bcmdataexports-export-export-dataquery)" : {{DataQuery}},
  "[Description](#cfn-bcmdataexports-export-export-description)" : {{String}},
  "[DestinationConfigurations](#cfn-bcmdataexports-export-export-destinationconfigurations)" : {{DestinationConfigurations}},
  "[ExportArn](#cfn-bcmdataexports-export-export-exportarn)" : {{String}},
  "[Name](#cfn-bcmdataexports-export-export-name)" : {{String}},
  "[RefreshCadence](#cfn-bcmdataexports-export-export-refreshcadence)" : {{RefreshCadence}}
}
```

### YAML
<a name="aws-properties-bcmdataexports-export-export-syntax.yaml"></a>

```
  [DataQuery](#cfn-bcmdataexports-export-export-dataquery): {{
    DataQuery}}
  [Description](#cfn-bcmdataexports-export-export-description): {{String}}
  [DestinationConfigurations](#cfn-bcmdataexports-export-export-destinationconfigurations): {{
    DestinationConfigurations}}
  [ExportArn](#cfn-bcmdataexports-export-export-exportarn): {{String}}
  [Name](#cfn-bcmdataexports-export-export-name): {{String}}
  [RefreshCadence](#cfn-bcmdataexports-export-export-refreshcadence): {{
    RefreshCadence}}
```

## Properties
<a name="aws-properties-bcmdataexports-export-export-properties"></a>

`DataQuery`  <a name="cfn-bcmdataexports-export-export-dataquery"></a>
The data query for this specific data export.
*Required*: Yes
*Type*: [DataQuery](aws-properties-bcmdataexports-export-dataquery.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-bcmdataexports-export-export-description"></a>
The description for this specific data export.
*Required*: No
*Type*: String
*Pattern*: `^[\S\s]*$`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationConfigurations`  <a name="cfn-bcmdataexports-export-export-destinationconfigurations"></a>
The destination configuration for this specific data export.
*Required*: Yes
*Type*: [DestinationConfigurations](aws-properties-bcmdataexports-export-destinationconfigurations.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExportArn`  <a name="cfn-bcmdataexports-export-export-exportarn"></a>
The Amazon Resource Name (ARN) for this export.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:(bcm-data-exports):[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bcmdataexports-export-export-name"></a>
The name of this specific data export.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9A-Za-z\-_]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RefreshCadence`  <a name="cfn-bcmdataexports-export-export-refreshcadence"></a>
The cadence for AWS to update the export in your S3 bucket.
*Required*: Yes
*Type*: [RefreshCadence](aws-properties-bcmdataexports-export-refreshcadence.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
