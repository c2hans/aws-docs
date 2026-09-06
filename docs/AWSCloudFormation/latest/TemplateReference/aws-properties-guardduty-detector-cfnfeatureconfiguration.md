---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-guardduty-detector-cfnfeatureconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GuardDuty::Detector CFNFeatureConfiguration
<a name="aws-properties-guardduty-detector-cfnfeatureconfiguration"></a>

Information about the configuration of a feature in your account.

## Syntax
<a name="aws-properties-guardduty-detector-cfnfeatureconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-guardduty-detector-cfnfeatureconfiguration-syntax.json"></a>

```
{
  "[AdditionalConfiguration](#cfn-guardduty-detector-cfnfeatureconfiguration-additionalconfiguration)" : {{[ CFNFeatureAdditionalConfiguration, ... ]}},
  "[Name](#cfn-guardduty-detector-cfnfeatureconfiguration-name)" : {{String}},
  "[Status](#cfn-guardduty-detector-cfnfeatureconfiguration-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-guardduty-detector-cfnfeatureconfiguration-syntax.yaml"></a>

```
  [AdditionalConfiguration](#cfn-guardduty-detector-cfnfeatureconfiguration-additionalconfiguration): {{
    - CFNFeatureAdditionalConfiguration}}
  [Name](#cfn-guardduty-detector-cfnfeatureconfiguration-name): {{String}}
  [Status](#cfn-guardduty-detector-cfnfeatureconfiguration-status): {{String}}
```

## Properties
<a name="aws-properties-guardduty-detector-cfnfeatureconfiguration-properties"></a>

`AdditionalConfiguration`  <a name="cfn-guardduty-detector-cfnfeatureconfiguration-additionalconfiguration"></a>
Information about the additional configuration of a feature in your account.
*Required*: No
*Type*: Array of [CFNFeatureAdditionalConfiguration](aws-properties-guardduty-detector-cfnfeatureadditionalconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-guardduty-detector-cfnfeatureconfiguration-name"></a>
Name of the feature. For a list of allowed values, see [DetectorFeatureConfiguration](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DetectorFeatureConfiguration.html#guardduty-Type-DetectorFeatureConfiguration-name) in the *GuardDuty API Reference*.
*Required*: Yes
*Type*: String
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-guardduty-detector-cfnfeatureconfiguration-status"></a>
Status of the feature configuration.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
