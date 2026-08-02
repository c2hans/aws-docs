---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-accountauditconfiguration-devicecertexpirationauditcheckconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::AccountAuditConfiguration DeviceCertExpirationAuditCheckConfiguration
<a name="aws-properties-iot-accountauditconfiguration-devicecertexpirationauditcheckconfiguration"></a>

Configuration for the device certificate expiration audit check.

## Syntax
<a name="aws-properties-iot-accountauditconfiguration-devicecertexpirationauditcheckconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-accountauditconfiguration-devicecertexpirationauditcheckconfiguration-syntax.json"></a>

```
{
  "[Configuration](#cfn-iot-accountauditconfiguration-devicecertexpirationauditcheckconfiguration-configuration)" : {{CertExpirationCheckCustomConfiguration}},
  "[Enabled](#cfn-iot-accountauditconfiguration-devicecertexpirationauditcheckconfiguration-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-iot-accountauditconfiguration-devicecertexpirationauditcheckconfiguration-syntax.yaml"></a>

```
  [Configuration](#cfn-iot-accountauditconfiguration-devicecertexpirationauditcheckconfiguration-configuration): {{
    CertExpirationCheckCustomConfiguration}}
  [Enabled](#cfn-iot-accountauditconfiguration-devicecertexpirationauditcheckconfiguration-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-iot-accountauditconfiguration-devicecertexpirationauditcheckconfiguration-properties"></a>

`Configuration`  <a name="cfn-iot-accountauditconfiguration-devicecertexpirationauditcheckconfiguration-configuration"></a>
Configuration settings for the device certificate expiration check, including the threshold in days before expiration. This configuration is of type `CertExpirationCheckCustomConfiguration`
*Required*: No
*Type*: [CertExpirationCheckCustomConfiguration](aws-properties-iot-accountauditconfiguration-certexpirationcheckcustomconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-iot-accountauditconfiguration-devicecertexpirationauditcheckconfiguration-enabled"></a>
True if this audit check is enabled for this account.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
