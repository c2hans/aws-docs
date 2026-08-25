---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-securityconfiguration-securityconfigurationdata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::SecurityConfiguration SecurityConfigurationData
<a name="aws-properties-emrcontainers-securityconfiguration-securityconfigurationdata"></a>

Configurations related to the security configuration for the request.

## Syntax
<a name="aws-properties-emrcontainers-securityconfiguration-securityconfigurationdata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-securityconfiguration-securityconfigurationdata-syntax.json"></a>

```
{
  "[AuthenticationConfiguration](#cfn-emrcontainers-securityconfiguration-securityconfigurationdata-authenticationconfiguration)" : {{AuthenticationConfiguration}},
  "[AuthorizationConfiguration](#cfn-emrcontainers-securityconfiguration-securityconfigurationdata-authorizationconfiguration)" : {{AuthorizationConfiguration}},
  "[EncryptionConfiguration](#cfn-emrcontainers-securityconfiguration-securityconfigurationdata-encryptionconfiguration)" : {{EncryptionConfiguration}}
}
```

### YAML
<a name="aws-properties-emrcontainers-securityconfiguration-securityconfigurationdata-syntax.yaml"></a>

```
  [AuthenticationConfiguration](#cfn-emrcontainers-securityconfiguration-securityconfigurationdata-authenticationconfiguration): {{
    AuthenticationConfiguration}}
  [AuthorizationConfiguration](#cfn-emrcontainers-securityconfiguration-securityconfigurationdata-authorizationconfiguration): {{
    AuthorizationConfiguration}}
  [EncryptionConfiguration](#cfn-emrcontainers-securityconfiguration-securityconfigurationdata-encryptionconfiguration): {{
    EncryptionConfiguration}}
```

## Properties
<a name="aws-properties-emrcontainers-securityconfiguration-securityconfigurationdata-properties"></a>

`AuthenticationConfiguration`  <a name="cfn-emrcontainers-securityconfiguration-securityconfigurationdata-authenticationconfiguration"></a>
Authentication-related configuration input for the security configuration.
*Required*: No
*Type*: [AuthenticationConfiguration](aws-properties-emrcontainers-securityconfiguration-authenticationconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AuthorizationConfiguration`  <a name="cfn-emrcontainers-securityconfiguration-securityconfigurationdata-authorizationconfiguration"></a>
Authorization-related configuration input for the security configuration.
*Required*: No
*Type*: [AuthorizationConfiguration](aws-properties-emrcontainers-securityconfiguration-authorizationconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EncryptionConfiguration`  <a name="cfn-emrcontainers-securityconfiguration-securityconfigurationdata-encryptionconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [EncryptionConfiguration](aws-properties-emrcontainers-securityconfiguration-encryptionconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
