---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-environmentblueprintconfiguration-lakeformationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::EnvironmentBlueprintConfiguration LakeFormationConfiguration
<a name="aws-properties-datazone-environmentblueprintconfiguration-lakeformationconfiguration"></a>

The Lake Formation configuration of the Data Lake blueprint.

## Syntax
<a name="aws-properties-datazone-environmentblueprintconfiguration-lakeformationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-environmentblueprintconfiguration-lakeformationconfiguration-syntax.json"></a>

```
{
  "[LocationRegistrationExcludeS3Locations](#cfn-datazone-environmentblueprintconfiguration-lakeformationconfiguration-locationregistrationexcludes3locations)" : {{[ String, ... ]}},
  "[LocationRegistrationRole](#cfn-datazone-environmentblueprintconfiguration-lakeformationconfiguration-locationregistrationrole)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-environmentblueprintconfiguration-lakeformationconfiguration-syntax.yaml"></a>

```
  [LocationRegistrationExcludeS3Locations](#cfn-datazone-environmentblueprintconfiguration-lakeformationconfiguration-locationregistrationexcludes3locations): {{
    - String}}
  [LocationRegistrationRole](#cfn-datazone-environmentblueprintconfiguration-lakeformationconfiguration-locationregistrationrole): {{String}}
```

## Properties
<a name="aws-properties-datazone-environmentblueprintconfiguration-lakeformationconfiguration-properties"></a>

`LocationRegistrationExcludeS3Locations`  <a name="cfn-datazone-environmentblueprintconfiguration-lakeformationconfiguration-locationregistrationexcludes3locations"></a>
Specifies certain Amazon S3 locations if you do not want Amazon DataZone to automatically register them in hybrid mode.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `1024 | 20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocationRegistrationRole`  <a name="cfn-datazone-environmentblueprintconfiguration-lakeformationconfiguration-locationregistrationrole"></a>
The role that is used to manage read/write access to the chosen Amazon S3 bucket(s) for Data Lake using AWS Lake Formation hybrid access mode.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
