---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-gitlabconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association GitLabConfiguration
<a name="aws-properties-devopsagent-association-gitlabconfiguration"></a>

Configuration for GitLab project integration. Defines the numeric project ID, full project path (namespace/project-name), GitLab instance identifier, and webhook update settings required for the Agent Space to access and interact with the GitLab project.

## Syntax
<a name="aws-properties-devopsagent-association-gitlabconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-gitlabconfiguration-syntax.json"></a>

```
{
  "[EnableWebhookUpdates](#cfn-devopsagent-association-gitlabconfiguration-enablewebhookupdates)" : {{Boolean}},
  "[InstanceIdentifier](#cfn-devopsagent-association-gitlabconfiguration-instanceidentifier)" : {{String}},
  "[ProjectId](#cfn-devopsagent-association-gitlabconfiguration-projectid)" : {{String}},
  "[ProjectPath](#cfn-devopsagent-association-gitlabconfiguration-projectpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-gitlabconfiguration-syntax.yaml"></a>

```
  [EnableWebhookUpdates](#cfn-devopsagent-association-gitlabconfiguration-enablewebhookupdates): {{Boolean}}
  [InstanceIdentifier](#cfn-devopsagent-association-gitlabconfiguration-instanceidentifier): {{String}}
  [ProjectId](#cfn-devopsagent-association-gitlabconfiguration-projectid): {{String}}
  [ProjectPath](#cfn-devopsagent-association-gitlabconfiguration-projectpath): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-association-gitlabconfiguration-properties"></a>

`EnableWebhookUpdates`  <a name="cfn-devopsagent-association-gitlabconfiguration-enablewebhookupdates"></a>
When set to true, enables the Agent Space to create and update webhooks for receiving notifications and events from the service.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceIdentifier`  <a name="cfn-devopsagent-association-gitlabconfiguration-instanceidentifier"></a>
The GitLab instance identifier (for example, `gitlab.com`).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProjectId`  <a name="cfn-devopsagent-association-gitlabconfiguration-projectid"></a>
GitLab numeric project ID.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProjectPath`  <a name="cfn-devopsagent-association-gitlabconfiguration-projectpath"></a>
The full GitLab project path (for example, `namespace/project-name`).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
