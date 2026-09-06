---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-azureconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association AzureConfiguration
<a name="aws-properties-devopsagent-association-azureconfiguration"></a>

Configuration for Azure subscription integration. Specifies the subscription ID to enable the Agent Space to discover and investigate resources in your Azure environment.

## Syntax
<a name="aws-properties-devopsagent-association-azureconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-azureconfiguration-syntax.json"></a>

```
{
  "[SubscriptionId](#cfn-devopsagent-association-azureconfiguration-subscriptionid)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-azureconfiguration-syntax.yaml"></a>

```
  [SubscriptionId](#cfn-devopsagent-association-azureconfiguration-subscriptionid): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-association-azureconfiguration-properties"></a>

`SubscriptionId`  <a name="cfn-devopsagent-association-azureconfiguration-subscriptionid"></a>
The Azure subscription ID corresponding to the provided resources.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
