---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-guardduty-detector-cfnfeatureadditionalconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GuardDuty::Detector CFNFeatureAdditionalConfiguration
<a name="aws-properties-guardduty-detector-cfnfeatureadditionalconfiguration"></a>

Information about the additional configuration of a feature in your account.

## Syntax
<a name="aws-properties-guardduty-detector-cfnfeatureadditionalconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-guardduty-detector-cfnfeatureadditionalconfiguration-syntax.json"></a>

```
{
  "[Name](#cfn-guardduty-detector-cfnfeatureadditionalconfiguration-name)" : {{String}},
  "[Status](#cfn-guardduty-detector-cfnfeatureadditionalconfiguration-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-guardduty-detector-cfnfeatureadditionalconfiguration-syntax.yaml"></a>

```
  [Name](#cfn-guardduty-detector-cfnfeatureadditionalconfiguration-name): {{String}}
  [Status](#cfn-guardduty-detector-cfnfeatureadditionalconfiguration-status): {{String}}
```

## Properties
<a name="aws-properties-guardduty-detector-cfnfeatureadditionalconfiguration-properties"></a>

`Name`  <a name="cfn-guardduty-detector-cfnfeatureadditionalconfiguration-name"></a>
Name of the additional configuration.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-guardduty-detector-cfnfeatureadditionalconfiguration-status"></a>
Status of the additional configuration.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
