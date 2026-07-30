---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bcmdataexports-export-refreshcadence.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BCMDataExports::Export RefreshCadence
<a name="aws-properties-bcmdataexports-export-refreshcadence"></a>

The cadence for AWS to update the data export in your S3 bucket.

## Syntax
<a name="aws-properties-bcmdataexports-export-refreshcadence-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bcmdataexports-export-refreshcadence-syntax.json"></a>

```
{
  "[Frequency](#cfn-bcmdataexports-export-refreshcadence-frequency)" : {{String}}
}
```

### YAML
<a name="aws-properties-bcmdataexports-export-refreshcadence-syntax.yaml"></a>

```
  [Frequency](#cfn-bcmdataexports-export-refreshcadence-frequency): {{String}}
```

## Properties
<a name="aws-properties-bcmdataexports-export-refreshcadence-properties"></a>

`Frequency`  <a name="cfn-bcmdataexports-export-refreshcadence-frequency"></a>
The frequency that data exports are updated. The export refreshes each time the source data updates, up to three times daily.
*Required*: Yes
*Type*: String
*Allowed values*: `SYNCHRONOUS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
