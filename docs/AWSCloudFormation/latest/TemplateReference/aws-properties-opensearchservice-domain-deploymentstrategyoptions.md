---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchservice-domain-deploymentstrategyoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchService::Domain DeploymentStrategyOptions
<a name="aws-properties-opensearchservice-domain-deploymentstrategyoptions"></a>

Specifies the deployment strategy options for the domain.

## Syntax
<a name="aws-properties-opensearchservice-domain-deploymentstrategyoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchservice-domain-deploymentstrategyoptions-syntax.json"></a>

```
{
  "[DeploymentStrategy](#cfn-opensearchservice-domain-deploymentstrategyoptions-deploymentstrategy)" : {{String}}
}
```

### YAML
<a name="aws-properties-opensearchservice-domain-deploymentstrategyoptions-syntax.yaml"></a>

```
  [DeploymentStrategy](#cfn-opensearchservice-domain-deploymentstrategyoptions-deploymentstrategy): {{String}}
```

## Properties
<a name="aws-properties-opensearchservice-domain-deploymentstrategyoptions-properties"></a>

`DeploymentStrategy`  <a name="cfn-opensearchservice-domain-deploymentstrategyoptions-deploymentstrategy"></a>
Specifies the deployment strategy for the domain. Valid values are `Default` and `CapacityOptimized`.
*Required*: No
*Type*: String
*Allowed values*: `Default | CapacityOptimized`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
