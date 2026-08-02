---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-environmentblueprintconfiguration-provisioningconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::EnvironmentBlueprintConfiguration ProvisioningConfiguration
<a name="aws-properties-datazone-environmentblueprintconfiguration-provisioningconfiguration"></a>

The provisioning configuration of the blueprint.

## Syntax
<a name="aws-properties-datazone-environmentblueprintconfiguration-provisioningconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-environmentblueprintconfiguration-provisioningconfiguration-syntax.json"></a>

```
{
  "[LakeFormationConfiguration](#cfn-datazone-environmentblueprintconfiguration-provisioningconfiguration-lakeformationconfiguration)" : {{LakeFormationConfiguration}}
}
```

### YAML
<a name="aws-properties-datazone-environmentblueprintconfiguration-provisioningconfiguration-syntax.yaml"></a>

```
  [LakeFormationConfiguration](#cfn-datazone-environmentblueprintconfiguration-provisioningconfiguration-lakeformationconfiguration): {{
    LakeFormationConfiguration}}
```

## Properties
<a name="aws-properties-datazone-environmentblueprintconfiguration-provisioningconfiguration-properties"></a>

`LakeFormationConfiguration`  <a name="cfn-datazone-environmentblueprintconfiguration-provisioningconfiguration-lakeformationconfiguration"></a>
The Lake Formation configuration of the Data Lake blueprint.
*Required*: Yes
*Type*: [LakeFormationConfiguration](aws-properties-datazone-environmentblueprintconfiguration-lakeformationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
