---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-githubconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association GitHubConfiguration
<a name="aws-properties-devopsagent-association-githubconfiguration"></a>

Configuration for GitHub repository integration. Defines the repository name, numeric repository ID, owner name, and owner type (user or organization) required for the Agent Space to access and interact with the GitHub repository.

## Syntax
<a name="aws-properties-devopsagent-association-githubconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-githubconfiguration-syntax.json"></a>

```
{
  "[Owner](#cfn-devopsagent-association-githubconfiguration-owner)" : {{String}},
  "[OwnerType](#cfn-devopsagent-association-githubconfiguration-ownertype)" : {{String}},
  "[RepoId](#cfn-devopsagent-association-githubconfiguration-repoid)" : {{String}},
  "[RepoName](#cfn-devopsagent-association-githubconfiguration-reponame)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-githubconfiguration-syntax.yaml"></a>

```
  [Owner](#cfn-devopsagent-association-githubconfiguration-owner): {{String}}
  [OwnerType](#cfn-devopsagent-association-githubconfiguration-ownertype): {{String}}
  [RepoId](#cfn-devopsagent-association-githubconfiguration-repoid): {{String}}
  [RepoName](#cfn-devopsagent-association-githubconfiguration-reponame): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-association-githubconfiguration-properties"></a>

`Owner`  <a name="cfn-devopsagent-association-githubconfiguration-owner"></a>
Repository owner.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OwnerType`  <a name="cfn-devopsagent-association-githubconfiguration-ownertype"></a>
The type of repository owner.
*Allowed Values*: `organization` \| `user`
*Required*: Yes
*Type*: String
*Allowed values*: `organization | user`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RepoId`  <a name="cfn-devopsagent-association-githubconfiguration-repoid"></a>
Associated Github repo ID.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RepoName`  <a name="cfn-devopsagent-association-githubconfiguration-reponame"></a>
Associated Github repo name.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
