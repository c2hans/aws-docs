---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-accountauditconfiguration-certagecheckcustomconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::AccountAuditConfiguration CertAgeCheckCustomConfiguration
<a name="aws-properties-iot-accountauditconfiguration-certagecheckcustomconfiguration"></a>

Configuration structure containing settings for the device certificate age check.

## Syntax
<a name="aws-properties-iot-accountauditconfiguration-certagecheckcustomconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-accountauditconfiguration-certagecheckcustomconfiguration-syntax.json"></a>

```
{
  "[CertAgeThresholdInDays](#cfn-iot-accountauditconfiguration-certagecheckcustomconfiguration-certagethresholdindays)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-accountauditconfiguration-certagecheckcustomconfiguration-syntax.yaml"></a>

```
  [CertAgeThresholdInDays](#cfn-iot-accountauditconfiguration-certagecheckcustomconfiguration-certagethresholdindays): {{String}}
```

## Properties
<a name="aws-properties-iot-accountauditconfiguration-certagecheckcustomconfiguration-properties"></a>

`CertAgeThresholdInDays`  <a name="cfn-iot-accountauditconfiguration-certagecheckcustomconfiguration-certagethresholdindays"></a>
The number of days that defines when a device certificate is considered to have aged. The check will report a finding if a certificate has been active for a number of days greater than or equal to this threshold value.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
