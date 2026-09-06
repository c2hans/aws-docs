---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-securityconfiguration-encryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::SecurityConfiguration EncryptionConfiguration
<a name="aws-properties-emrcontainers-securityconfiguration-encryptionconfiguration"></a>

Configurations related to encryption for the security configuration.

## Syntax
<a name="aws-properties-emrcontainers-securityconfiguration-encryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-securityconfiguration-encryptionconfiguration-syntax.json"></a>

```
{
  "[AtRestEncryptionConfiguration](#cfn-emrcontainers-securityconfiguration-encryptionconfiguration-atrestencryptionconfiguration)" : {{AtRestEncryptionConfiguration}},
  "[InTransitEncryptionConfiguration](#cfn-emrcontainers-securityconfiguration-encryptionconfiguration-intransitencryptionconfiguration)" : {{InTransitEncryptionConfiguration}}
}
```

### YAML
<a name="aws-properties-emrcontainers-securityconfiguration-encryptionconfiguration-syntax.yaml"></a>

```
  [AtRestEncryptionConfiguration](#cfn-emrcontainers-securityconfiguration-encryptionconfiguration-atrestencryptionconfiguration): {{
    AtRestEncryptionConfiguration}}
  [InTransitEncryptionConfiguration](#cfn-emrcontainers-securityconfiguration-encryptionconfiguration-intransitencryptionconfiguration): {{
    InTransitEncryptionConfiguration}}
```

## Properties
<a name="aws-properties-emrcontainers-securityconfiguration-encryptionconfiguration-properties"></a>

`AtRestEncryptionConfiguration`  <a name="cfn-emrcontainers-securityconfiguration-encryptionconfiguration-atrestencryptionconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [AtRestEncryptionConfiguration](aws-properties-emrcontainers-securityconfiguration-atrestencryptionconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InTransitEncryptionConfiguration`  <a name="cfn-emrcontainers-securityconfiguration-encryptionconfiguration-intransitencryptionconfiguration"></a>
In-transit encryption-related input for the security configuration.
*Required*: No
*Type*: [InTransitEncryptionConfiguration](aws-properties-emrcontainers-securityconfiguration-intransitencryptionconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
