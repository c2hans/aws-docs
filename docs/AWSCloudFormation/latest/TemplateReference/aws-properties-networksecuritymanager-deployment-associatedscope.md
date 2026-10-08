---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networksecuritymanager-deployment-associatedscope.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkSecurityManager::Deployment AssociatedScope
<a name="aws-properties-networksecuritymanager-deployment-associatedscope"></a>

References the scope that a deployment protects. Use the `AssociatedScopeList` property of the `AWS::NetworkSecurityManager::Deployment` resource to associate a scope with a deployment.

## Syntax
<a name="aws-properties-networksecuritymanager-deployment-associatedscope-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networksecuritymanager-deployment-associatedscope-syntax.json"></a>

```
{
  "[ScopeArn](#cfn-networksecuritymanager-deployment-associatedscope-scopearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-networksecuritymanager-deployment-associatedscope-syntax.yaml"></a>

```
  [ScopeArn](#cfn-networksecuritymanager-deployment-associatedscope-scopearn): {{String}}
```

## Properties
<a name="aws-properties-networksecuritymanager-deployment-associatedscope-properties"></a>

`ScopeArn`  <a name="cfn-networksecuritymanager-deployment-associatedscope-scopearn"></a>
The Amazon Resource Name (ARN) of the scope that selects the accounts and resources to protect. For example: `arn:aws:network-security-manager:us-east-1:123456789012:scope:a1b2c3d4e5f6`.
To get this value from a scope defined in the same template, use `Fn::GetAtt` with the [AWS::NetworkSecurityManager::Scope](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networksecuritymanager-scope.html) resource.
*Required*: Yes
*Type*: String
*Pattern*: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:(.+)`
*Minimum*: `20`
*Maximum*: `1010`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
