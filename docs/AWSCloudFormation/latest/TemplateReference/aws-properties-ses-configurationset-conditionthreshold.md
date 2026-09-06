---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-configurationset-conditionthreshold.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::ConfigurationSet ConditionThreshold
<a name="aws-properties-ses-configurationset-conditionthreshold"></a>

Specifies the threshold conditions for the automatic validation settings.

## Syntax
<a name="aws-properties-ses-configurationset-conditionthreshold-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-configurationset-conditionthreshold-syntax.json"></a>

```
{
  "[ConditionThresholdEnabled](#cfn-ses-configurationset-conditionthreshold-conditionthresholdenabled)" : {{String}},
  "[OverallConfidenceThreshold](#cfn-ses-configurationset-conditionthreshold-overallconfidencethreshold)" : {{OverallConfidenceThreshold}}
}
```

### YAML
<a name="aws-properties-ses-configurationset-conditionthreshold-syntax.yaml"></a>

```
  [ConditionThresholdEnabled](#cfn-ses-configurationset-conditionthreshold-conditionthresholdenabled): {{String}}
  [OverallConfidenceThreshold](#cfn-ses-configurationset-conditionthreshold-overallconfidencethreshold): {{
    OverallConfidenceThreshold}}
```

## Properties
<a name="aws-properties-ses-configurationset-conditionthreshold-properties"></a>

`ConditionThresholdEnabled`  <a name="cfn-ses-configurationset-conditionthreshold-conditionthresholdenabled"></a>
Enables or disables the automatic validation feature. When enabled, SES validates recipients to calculate a confidence score regarding their validity.
*Required*: Yes
*Type*: String
*Pattern*: `ENABLED|DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OverallConfidenceThreshold`  <a name="cfn-ses-configurationset-conditionthreshold-overallconfidencethreshold"></a>
The validation settings that define the minimum score required for SES to allow an email to be sent.
*Required*: No
*Type*: [OverallConfidenceThreshold](aws-properties-ses-configurationset-overallconfidencethreshold.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
