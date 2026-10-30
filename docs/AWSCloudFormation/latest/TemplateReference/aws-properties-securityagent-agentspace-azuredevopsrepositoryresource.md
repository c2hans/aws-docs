---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityagent-agentspace-azuredevopsrepositoryresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityAgent::AgentSpace AzureDevOpsRepositoryResource
<a name="aws-properties-securityagent-agentspace-azuredevopsrepositoryresource"></a>

An Azure DevOps repository integrated as a resource.

## Syntax
<a name="aws-properties-securityagent-agentspace-azuredevopsrepositoryresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityagent-agentspace-azuredevopsrepositoryresource-syntax.json"></a>

```
{
  "[Name](#cfn-securityagent-agentspace-azuredevopsrepositoryresource-name)" : {{String}},
  "[Organization](#cfn-securityagent-agentspace-azuredevopsrepositoryresource-organization)" : {{String}},
  "[Project](#cfn-securityagent-agentspace-azuredevopsrepositoryresource-project)" : {{String}}
}
```

### YAML
<a name="aws-properties-securityagent-agentspace-azuredevopsrepositoryresource-syntax.yaml"></a>

```
  [Name](#cfn-securityagent-agentspace-azuredevopsrepositoryresource-name): {{String}}
  [Organization](#cfn-securityagent-agentspace-azuredevopsrepositoryresource-organization): {{String}}
  [Project](#cfn-securityagent-agentspace-azuredevopsrepositoryresource-project): {{String}}
```

## Properties
<a name="aws-properties-securityagent-agentspace-azuredevopsrepositoryresource-properties"></a>

`Name`  <a name="cfn-securityagent-agentspace-azuredevopsrepositoryresource-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Organization`  <a name="cfn-securityagent-agentspace-azuredevopsrepositoryresource-organization"></a>
The name of the Azure DevOps organization that owns the repository.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Project`  <a name="cfn-securityagent-agentspace-azuredevopsrepositoryresource-project"></a>
The name of the Azure DevOps project that contains the repository.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
