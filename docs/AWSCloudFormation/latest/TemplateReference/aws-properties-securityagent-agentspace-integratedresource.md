---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityagent-agentspace-integratedresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityAgent::AgentSpace IntegratedResource
<a name="aws-properties-securityagent-agentspace-integratedresource"></a>

Represents an integrated resource from a third-party provider. This is a union type that contains provider-specific resource information.

## Syntax
<a name="aws-properties-securityagent-agentspace-integratedresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityagent-agentspace-integratedresource-syntax.json"></a>

```
{
  "[Integration](#cfn-securityagent-agentspace-integratedresource-integration)" : {{String}},
  "[ProviderResources](#cfn-securityagent-agentspace-integratedresource-providerresources)" : {{[ ProviderResource, ... ]}}
}
```

### YAML
<a name="aws-properties-securityagent-agentspace-integratedresource-syntax.yaml"></a>

```
  [Integration](#cfn-securityagent-agentspace-integratedresource-integration): {{String}}
  [ProviderResources](#cfn-securityagent-agentspace-integratedresource-providerresources): {{
    - ProviderResource}}
```

## Properties
<a name="aws-properties-securityagent-agentspace-integratedresource-properties"></a>

`Integration`  <a name="cfn-securityagent-agentspace-integratedresource-integration"></a>
The unique identifier of the integration that provides access to the resource.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProviderResources`  <a name="cfn-securityagent-agentspace-integratedresource-providerresources"></a>
The metadata for the integrated resource.
*Required*: Yes
*Type*: Array of [ProviderResource](aws-properties-securityagent-agentspace-providerresource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
