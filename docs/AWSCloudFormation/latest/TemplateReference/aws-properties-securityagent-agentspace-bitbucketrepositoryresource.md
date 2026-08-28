---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityagent-agentspace-bitbucketrepositoryresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityAgent::AgentSpace BitbucketRepositoryResource
<a name="aws-properties-securityagent-agentspace-bitbucketrepositoryresource"></a>

A Bitbucket repository integrated as a resource.

## Syntax
<a name="aws-properties-securityagent-agentspace-bitbucketrepositoryresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityagent-agentspace-bitbucketrepositoryresource-syntax.json"></a>

```
{
  "[Name](#cfn-securityagent-agentspace-bitbucketrepositoryresource-name)" : {{String}},
  "[Workspace](#cfn-securityagent-agentspace-bitbucketrepositoryresource-workspace)" : {{String}}
}
```

### YAML
<a name="aws-properties-securityagent-agentspace-bitbucketrepositoryresource-syntax.yaml"></a>

```
  [Name](#cfn-securityagent-agentspace-bitbucketrepositoryresource-name): {{String}}
  [Workspace](#cfn-securityagent-agentspace-bitbucketrepositoryresource-workspace): {{String}}
```

## Properties
<a name="aws-properties-securityagent-agentspace-bitbucketrepositoryresource-properties"></a>

`Name`  <a name="cfn-securityagent-agentspace-bitbucketrepositoryresource-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Workspace`  <a name="cfn-securityagent-agentspace-bitbucketrepositoryresource-workspace"></a>
The workspace slug that owns the repository.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
