---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networksecuritymanager-deployment-deploymentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkSecurityManager::Deployment DeploymentConfiguration
<a name="aws-properties-networksecuritymanager-deployment-deploymentconfiguration"></a>

The configuration settings that control the behavior of the deployment. If you omit this property, CloudFormation creates the deployment with cross-account visibility disabled.

## Syntax
<a name="aws-properties-networksecuritymanager-deployment-deploymentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networksecuritymanager-deployment-deploymentconfiguration-syntax.json"></a>

```
{
  "[EnableCrossAccountVisibility](#cfn-networksecuritymanager-deployment-deploymentconfiguration-enablecrossaccountvisibility)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-networksecuritymanager-deployment-deploymentconfiguration-syntax.yaml"></a>

```
  [EnableCrossAccountVisibility](#cfn-networksecuritymanager-deployment-deploymentconfiguration-enablecrossaccountvisibility): {{Boolean}}
```

## Properties
<a name="aws-properties-networksecuritymanager-deployment-deploymentconfiguration-properties"></a>

`EnableCrossAccountVisibility`  <a name="cfn-networksecuritymanager-deployment-deploymentconfiguration-enablecrossaccountvisibility"></a>
Specifies whether aggregate synchronization status details for the resources covered by this deployment are visible across accounts. Default: `false`.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
