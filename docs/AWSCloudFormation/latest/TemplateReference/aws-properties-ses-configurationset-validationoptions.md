---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-configurationset-validationoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::ConfigurationSet ValidationOptions
<a name="aws-properties-ses-configurationset-validationoptions"></a>

Specifies the configuration settings for email automatic validation.

## Syntax
<a name="aws-properties-ses-configurationset-validationoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-configurationset-validationoptions-syntax.json"></a>

```
{
  "[ConditionThreshold](#cfn-ses-configurationset-validationoptions-conditionthreshold)" : {{ConditionThreshold}}
}
```

### YAML
<a name="aws-properties-ses-configurationset-validationoptions-syntax.yaml"></a>

```
  [ConditionThreshold](#cfn-ses-configurationset-validationoptions-conditionthreshold): {{
    ConditionThreshold}}
```

## Properties
<a name="aws-properties-ses-configurationset-validationoptions-properties"></a>

`ConditionThreshold`  <a name="cfn-ses-configurationset-validationoptions-conditionthreshold"></a>
The threshold configuration for the automatic validation settings.
*Required*: Yes
*Type*: [ConditionThreshold](aws-properties-ses-configurationset-conditionthreshold.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
