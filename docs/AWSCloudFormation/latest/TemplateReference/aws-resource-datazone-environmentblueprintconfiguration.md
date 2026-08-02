---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datazone-environmentblueprintconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::EnvironmentBlueprintConfiguration
<a name="aws-resource-datazone-environmentblueprintconfiguration"></a>

The configuration details of an environment blueprint.

## Syntax
<a name="aws-resource-datazone-environmentblueprintconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-datazone-environmentblueprintconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::DataZone::EnvironmentBlueprintConfiguration",
  "Properties" : {
      "[DomainIdentifier](#cfn-datazone-environmentblueprintconfiguration-domainidentifier)" : {{String}},
      "[EnabledRegions](#cfn-datazone-environmentblueprintconfiguration-enabledregions)" : {{[ String, ... ]}},
      "[EnvironmentBlueprintIdentifier](#cfn-datazone-environmentblueprintconfiguration-environmentblueprintidentifier)" : {{String}},
      "[EnvironmentRolePermissionBoundary](#cfn-datazone-environmentblueprintconfiguration-environmentrolepermissionboundary)" : {{String}},
      "[GlobalParameters](#cfn-datazone-environmentblueprintconfiguration-globalparameters)" : {{{{{Key}}: {{Value}}, ...}}},
      "[ManageAccessRoleArn](#cfn-datazone-environmentblueprintconfiguration-manageaccessrolearn)" : {{String}},
      "[ProvisioningConfigurations](#cfn-datazone-environmentblueprintconfiguration-provisioningconfigurations)" : {{[ ProvisioningConfiguration, ... ]}},
      "[ProvisioningRoleArn](#cfn-datazone-environmentblueprintconfiguration-provisioningrolearn)" : {{String}},
      "[RegionalParameters](#cfn-datazone-environmentblueprintconfiguration-regionalparameters)" : {{[ RegionalParameter, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-datazone-environmentblueprintconfiguration-syntax.yaml"></a>

```
Type: AWS::DataZone::EnvironmentBlueprintConfiguration
Properties:
  [DomainIdentifier](#cfn-datazone-environmentblueprintconfiguration-domainidentifier): {{String}}
  [EnabledRegions](#cfn-datazone-environmentblueprintconfiguration-enabledregions): {{
    - String}}
  [EnvironmentBlueprintIdentifier](#cfn-datazone-environmentblueprintconfiguration-environmentblueprintidentifier): {{String}}
  [EnvironmentRolePermissionBoundary](#cfn-datazone-environmentblueprintconfiguration-environmentrolepermissionboundary): {{String}}
  [GlobalParameters](#cfn-datazone-environmentblueprintconfiguration-globalparameters): {{
    {{Key}}: {{Value}}}}
  [ManageAccessRoleArn](#cfn-datazone-environmentblueprintconfiguration-manageaccessrolearn): {{String}}
  [ProvisioningConfigurations](#cfn-datazone-environmentblueprintconfiguration-provisioningconfigurations): {{
    - ProvisioningConfiguration}}
  [ProvisioningRoleArn](#cfn-datazone-environmentblueprintconfiguration-provisioningrolearn): {{String}}
  [RegionalParameters](#cfn-datazone-environmentblueprintconfiguration-regionalparameters): {{
    - RegionalParameter}}
```

## Properties
<a name="aws-resource-datazone-environmentblueprintconfiguration-properties"></a>

`DomainIdentifier`  <a name="cfn-datazone-environmentblueprintconfiguration-domainidentifier"></a>
The identifier of the Amazon DataZone domain in which an environment blueprint exists.
*Required*: Yes
*Type*: String
*Pattern*: `^dzd[-_][a-zA-Z0-9_-]{1,36}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnabledRegions`  <a name="cfn-datazone-environmentblueprintconfiguration-enabledregions"></a>
The enabled AWS Regions specified in a blueprint configuration.
*Required*: Yes
*Type*: Array of String
*Maximum*: `16`
*Minimum*: `4 | 0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvironmentBlueprintIdentifier`  <a name="cfn-datazone-environmentblueprintconfiguration-environmentblueprintidentifier"></a>
The identifier of the environment blueprint.
In the current release, only the following values are supported: `DefaultDataLake` and `DefaultDataWarehouse`.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]{1,36}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnvironmentRolePermissionBoundary`  <a name="cfn-datazone-environmentblueprintconfiguration-environmentrolepermissionboundary"></a>
The environment role permission boundary.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[^:]*:iam::(aws|\d{12}):policy/[\w+=,.@-]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GlobalParameters`  <a name="cfn-datazone-environmentblueprintconfiguration-globalparameters"></a>
Region-agnostic environment blueprint parameters.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManageAccessRoleArn`  <a name="cfn-datazone-environmentblueprintconfiguration-manageaccessrolearn"></a>
The ARN of the manage access role.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProvisioningConfigurations`  <a name="cfn-datazone-environmentblueprintconfiguration-provisioningconfigurations"></a>
The provisioning configuration of a blueprint.
*Required*: No
*Type*: Array of [ProvisioningConfiguration](aws-properties-datazone-environmentblueprintconfiguration-provisioningconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProvisioningRoleArn`  <a name="cfn-datazone-environmentblueprintconfiguration-provisioningrolearn"></a>
The ARN of the provisioning role.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RegionalParameters`  <a name="cfn-datazone-environmentblueprintconfiguration-regionalparameters"></a>
The regional parameters of the environment blueprint.
*Required*: No
*Type*: Array of [RegionalParameter](aws-properties-datazone-environmentblueprintconfiguration-regionalparameter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-datazone-environmentblueprintconfiguration-return-values"></a>

### Ref
<a name="aws-resource-datazone-environmentblueprintconfiguration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a string containing pipe-separated `DomainId` and the `EnvironmentBlueprintId`, which uniquely identifies the environment blueprint configuration. For example: `{ "Ref": "MyBlueprintConfiguration" }` for the resource with the logical ID `MyBlueprintConfiguration`, `Ref` returns `DomainId|BlueprintConfigurationId`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-datazone-environmentblueprintconfiguration-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-datazone-environmentblueprintconfiguration-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp of when an environment blueprint was created.

`DomainId`  <a name="DomainId-fn::getatt"></a>
The identifier of the Amazon DataZone domain in which an environment blueprint exists.

`EnvironmentBlueprintId`  <a name="EnvironmentBlueprintId-fn::getatt"></a>
The identifier of the environment blueprint. This identifier should be used when creating environment profiles.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp of when the environment blueprint was updated.
