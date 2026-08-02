---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityagent-agentspace-providerresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityAgent::AgentSpace ProviderResource
<a name="aws-properties-securityagent-agentspace-providerresource"></a>

Represents an integrated resource from a third-party provider. This is a union type that contains provider-specific resource information.

## Syntax
<a name="aws-properties-securityagent-agentspace-providerresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityagent-agentspace-providerresource-syntax.json"></a>

```
{
  "[BitbucketCapabilities](#cfn-securityagent-agentspace-providerresource-bitbucketcapabilities)" : {{BitbucketCapabilitiesResource}},
  "[BitbucketRepository](#cfn-securityagent-agentspace-providerresource-bitbucketrepository)" : {{BitbucketRepositoryResource}},
  "[ConfluenceCapabilities](#cfn-securityagent-agentspace-providerresource-confluencecapabilities)" : {{ConfluenceCapabilitiesResource}},
  "[ConfluenceDocument](#cfn-securityagent-agentspace-providerresource-confluencedocument)" : {{ConfluenceDocumentResource}},
  "[GitHubCapabilities](#cfn-securityagent-agentspace-providerresource-githubcapabilities)" : {{GitHubCapabilitiesResource}},
  "[GitHubRepository](#cfn-securityagent-agentspace-providerresource-githubrepository)" : {{GitHubRepositoryResource}},
  "[GitLabCapabilities](#cfn-securityagent-agentspace-providerresource-gitlabcapabilities)" : {{GitLabCapabilitiesResource}},
  "[GitLabRepository](#cfn-securityagent-agentspace-providerresource-gitlabrepository)" : {{GitLabRepositoryResource}}
}
```

### YAML
<a name="aws-properties-securityagent-agentspace-providerresource-syntax.yaml"></a>

```
  [BitbucketCapabilities](#cfn-securityagent-agentspace-providerresource-bitbucketcapabilities): {{
    BitbucketCapabilitiesResource}}
  [BitbucketRepository](#cfn-securityagent-agentspace-providerresource-bitbucketrepository): {{
    BitbucketRepositoryResource}}
  [ConfluenceCapabilities](#cfn-securityagent-agentspace-providerresource-confluencecapabilities): {{
    ConfluenceCapabilitiesResource}}
  [ConfluenceDocument](#cfn-securityagent-agentspace-providerresource-confluencedocument): {{
    ConfluenceDocumentResource}}
  [GitHubCapabilities](#cfn-securityagent-agentspace-providerresource-githubcapabilities): {{
    GitHubCapabilitiesResource}}
  [GitHubRepository](#cfn-securityagent-agentspace-providerresource-githubrepository): {{
    GitHubRepositoryResource}}
  [GitLabCapabilities](#cfn-securityagent-agentspace-providerresource-gitlabcapabilities): {{
    GitLabCapabilitiesResource}}
  [GitLabRepository](#cfn-securityagent-agentspace-providerresource-gitlabrepository): {{
    GitLabRepositoryResource}}
```

## Properties
<a name="aws-properties-securityagent-agentspace-providerresource-properties"></a>

`BitbucketCapabilities`  <a name="cfn-securityagent-agentspace-providerresource-bitbucketcapabilities"></a>
Property description not available.
*Required*: No
*Type*: [BitbucketCapabilitiesResource](aws-properties-securityagent-agentspace-bitbucketcapabilitiesresource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BitbucketRepository`  <a name="cfn-securityagent-agentspace-providerresource-bitbucketrepository"></a>
Property description not available.
*Required*: No
*Type*: [BitbucketRepositoryResource](aws-properties-securityagent-agentspace-bitbucketrepositoryresource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConfluenceCapabilities`  <a name="cfn-securityagent-agentspace-providerresource-confluencecapabilities"></a>
Property description not available.
*Required*: No
*Type*: [ConfluenceCapabilitiesResource](aws-properties-securityagent-agentspace-confluencecapabilitiesresource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConfluenceDocument`  <a name="cfn-securityagent-agentspace-providerresource-confluencedocument"></a>
Property description not available.
*Required*: No
*Type*: [ConfluenceDocumentResource](aws-properties-securityagent-agentspace-confluencedocumentresource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GitHubCapabilities`  <a name="cfn-securityagent-agentspace-providerresource-githubcapabilities"></a>
The capabilities enabled for a GitHub resource integration.
*Required*: No
*Type*: [GitHubCapabilitiesResource](aws-properties-securityagent-agentspace-githubcapabilitiesresource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GitHubRepository`  <a name="cfn-securityagent-agentspace-providerresource-githubrepository"></a>
Represents a GitHub repository resource used in an integration.
*Required*: No
*Type*: [GitHubRepositoryResource](aws-properties-securityagent-agentspace-githubrepositoryresource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GitLabCapabilities`  <a name="cfn-securityagent-agentspace-providerresource-gitlabcapabilities"></a>
Property description not available.
*Required*: No
*Type*: [GitLabCapabilitiesResource](aws-properties-securityagent-agentspace-gitlabcapabilitiesresource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GitLabRepository`  <a name="cfn-securityagent-agentspace-providerresource-gitlabrepository"></a>
Property description not available.
*Required*: No
*Type*: [GitLabRepositoryResource](aws-properties-securityagent-agentspace-gitlabrepositoryresource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
