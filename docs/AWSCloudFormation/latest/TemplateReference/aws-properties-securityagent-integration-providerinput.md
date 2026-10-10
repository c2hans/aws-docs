---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityagent-integration-providerinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityAgent::Integration ProviderInput
<a name="aws-properties-securityagent-integration-providerinput"></a>

The provider-specific input for creating an integration. This is a union type that contains provider-specific configuration.

## Syntax
<a name="aws-properties-securityagent-integration-providerinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityagent-integration-providerinput-syntax.json"></a>

```
{
  "[Bitbucket](#cfn-securityagent-integration-providerinput-bitbucket)" : {{BitbucketInput}},
  "[Confluence](#cfn-securityagent-integration-providerinput-confluence)" : {{ConfluenceInput}},
  "[Github](#cfn-securityagent-integration-providerinput-github)" : {{GitHubInput}},
  "[Gitlab](#cfn-securityagent-integration-providerinput-gitlab)" : {{GitLabInput}}
}
```

### YAML
<a name="aws-properties-securityagent-integration-providerinput-syntax.yaml"></a>

```
  [Bitbucket](#cfn-securityagent-integration-providerinput-bitbucket): {{
    BitbucketInput}}
  [Confluence](#cfn-securityagent-integration-providerinput-confluence): {{
    ConfluenceInput}}
  [Github](#cfn-securityagent-integration-providerinput-github): {{
    GitHubInput}}
  [Gitlab](#cfn-securityagent-integration-providerinput-gitlab): {{
    GitLabInput}}
```

## Properties
<a name="aws-properties-securityagent-integration-providerinput-properties"></a>

`Bitbucket`  <a name="cfn-securityagent-integration-providerinput-bitbucket"></a>
The configuration for a Bitbucket integration.
*Required*: No
*Type*: [BitbucketInput](aws-properties-securityagent-integration-bitbucketinput.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Confluence`  <a name="cfn-securityagent-integration-providerinput-confluence"></a>
The configuration for a Confluence integration.
*Required*: No
*Type*: [ConfluenceInput](aws-properties-securityagent-integration-confluenceinput.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Github`  <a name="cfn-securityagent-integration-providerinput-github"></a>
The GitHub-specific input for creating an integration.
*Required*: No
*Type*: [GitHubInput](aws-properties-securityagent-integration-githubinput.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Gitlab`  <a name="cfn-securityagent-integration-providerinput-gitlab"></a>
The configuration for a GitLab integration.
*Required*: No
*Type*: [GitLabInput](aws-properties-securityagent-integration-gitlabinput.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
