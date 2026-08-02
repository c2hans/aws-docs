---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityagent-agentspace-githubrepositoryresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityAgent::AgentSpace GitHubRepositoryResource
<a name="aws-properties-securityagent-agentspace-githubrepositoryresource"></a>

Represents a GitHub repository resource used in an integration.

## Syntax
<a name="aws-properties-securityagent-agentspace-githubrepositoryresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityagent-agentspace-githubrepositoryresource-syntax.json"></a>

```
{
  "[Name](#cfn-securityagent-agentspace-githubrepositoryresource-name)" : {{String}},
  "[Owner](#cfn-securityagent-agentspace-githubrepositoryresource-owner)" : {{String}}
}
```

### YAML
<a name="aws-properties-securityagent-agentspace-githubrepositoryresource-syntax.yaml"></a>

```
  [Name](#cfn-securityagent-agentspace-githubrepositoryresource-name): {{String}}
  [Owner](#cfn-securityagent-agentspace-githubrepositoryresource-owner): {{String}}
```

## Properties
<a name="aws-properties-securityagent-agentspace-githubrepositoryresource-properties"></a>

`Name`  <a name="cfn-securityagent-agentspace-githubrepositoryresource-name"></a>
The name of the GitHub repository.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Owner`  <a name="cfn-securityagent-agentspace-githubrepositoryresource-owner"></a>
The owner of the GitHub repository.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
