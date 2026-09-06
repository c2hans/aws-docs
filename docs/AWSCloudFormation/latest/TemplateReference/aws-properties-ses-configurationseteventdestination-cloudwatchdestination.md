---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-configurationseteventdestination-cloudwatchdestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::ConfigurationSetEventDestination CloudWatchDestination
<a name="aws-properties-ses-configurationseteventdestination-cloudwatchdestination"></a>

An object that defines an Amazon CloudWatch destination for email events. You can use Amazon CloudWatch to monitor and gain insights on your email sending metrics.

## Syntax
<a name="aws-properties-ses-configurationseteventdestination-cloudwatchdestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-configurationseteventdestination-cloudwatchdestination-syntax.json"></a>

```
{
  "[DimensionConfigurations](#cfn-ses-configurationseteventdestination-cloudwatchdestination-dimensionconfigurations)" : {{[ DimensionConfiguration, ... ]}}
}
```

### YAML
<a name="aws-properties-ses-configurationseteventdestination-cloudwatchdestination-syntax.yaml"></a>

```
  [DimensionConfigurations](#cfn-ses-configurationseteventdestination-cloudwatchdestination-dimensionconfigurations): {{
    - DimensionConfiguration}}
```

## Properties
<a name="aws-properties-ses-configurationseteventdestination-cloudwatchdestination-properties"></a>

`DimensionConfigurations`  <a name="cfn-ses-configurationseteventdestination-cloudwatchdestination-dimensionconfigurations"></a>
An array of objects that define the dimensions to use when you send email events to Amazon CloudWatch.
*Required*: No
*Type*: Array of [DimensionConfiguration](aws-properties-ses-configurationseteventdestination-dimensionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
