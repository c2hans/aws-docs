---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-releasemanagementconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association ReleaseManagementConfiguration
<a name="aws-properties-devopsagent-association-releasemanagementconfiguration"></a>

<a name="aws-properties-devopsagent-association-releasemanagementconfiguration-description"></a>The `ReleaseManagementConfiguration` property type specifies Property description not available. for an [AWS::DevOpsAgent::Association](aws-resource-devopsagent-association.md).

## Syntax
<a name="aws-properties-devopsagent-association-releasemanagementconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-releasemanagementconfiguration-syntax.json"></a>

```
{
  "[Name](#cfn-devopsagent-association-releasemanagementconfiguration-name)" : {{String}},
  "[NetworkAccess](#cfn-devopsagent-association-releasemanagementconfiguration-networkaccess)" : {{NetworkAccessConfiguration}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-releasemanagementconfiguration-syntax.yaml"></a>

```
  [Name](#cfn-devopsagent-association-releasemanagementconfiguration-name): {{String}}
  [NetworkAccess](#cfn-devopsagent-association-releasemanagementconfiguration-networkaccess): {{
    NetworkAccessConfiguration}}
```

## Properties
<a name="aws-properties-devopsagent-association-releasemanagementconfiguration-properties"></a>

`Name`  <a name="cfn-devopsagent-association-releasemanagementconfiguration-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[\p{L}\p{N}\p{P}\p{S}\p{Z}]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkAccess`  <a name="cfn-devopsagent-association-releasemanagementconfiguration-networkaccess"></a>
Property description not available.
*Required*: Yes
*Type*: [NetworkAccessConfiguration](aws-properties-devopsagent-association-networkaccessconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
