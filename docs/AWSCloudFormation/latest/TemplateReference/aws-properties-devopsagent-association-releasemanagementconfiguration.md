---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-releasemanagementconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association ReleaseManagementConfiguration
<a name="aws-properties-devopsagent-association-releasemanagementconfiguration"></a>

The configuration for a release management environment. A release management environment defines how AWS DevOps Agent reaches your application. GitHub and GitLab associations reference it through `ReleaseManagementAssociationId` to run automated verification testing against that application.

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
The name of this release management environment.
*Required*: Yes
*Type*: String
*Pattern*: `^[\p{L}\p{N}\p{P}\p{S}\p{Z}]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkAccess`  <a name="cfn-devopsagent-association-releasemanagementconfiguration-networkaccess"></a>
Specifies how AWS DevOps Agent reaches your application through this release management environment.
*Required*: Yes
*Type*: [NetworkAccessConfiguration](aws-properties-devopsagent-association-networkaccessconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
