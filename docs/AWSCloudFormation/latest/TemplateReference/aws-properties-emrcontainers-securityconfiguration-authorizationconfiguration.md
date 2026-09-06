---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-securityconfiguration-authorizationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::SecurityConfiguration AuthorizationConfiguration
<a name="aws-properties-emrcontainers-securityconfiguration-authorizationconfiguration"></a>

Authorization-related configuration inputs for the security configuration.

## Syntax
<a name="aws-properties-emrcontainers-securityconfiguration-authorizationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-securityconfiguration-authorizationconfiguration-syntax.json"></a>

```
{
  "[LakeFormationConfiguration](#cfn-emrcontainers-securityconfiguration-authorizationconfiguration-lakeformationconfiguration)" : {{LakeFormationConfiguration}}
}
```

### YAML
<a name="aws-properties-emrcontainers-securityconfiguration-authorizationconfiguration-syntax.yaml"></a>

```
  [LakeFormationConfiguration](#cfn-emrcontainers-securityconfiguration-authorizationconfiguration-lakeformationconfiguration): {{
    LakeFormationConfiguration}}
```

## Properties
<a name="aws-properties-emrcontainers-securityconfiguration-authorizationconfiguration-properties"></a>

`LakeFormationConfiguration`  <a name="cfn-emrcontainers-securityconfiguration-authorizationconfiguration-lakeformationconfiguration"></a>
AWS Lake Formation related configuration inputs for the security configuration.
*Required*: No
*Type*: [LakeFormationConfiguration](aws-properties-emrcontainers-securityconfiguration-lakeformationconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
