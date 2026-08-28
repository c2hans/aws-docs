---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codebuild-project-scopeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeBuild::Project ScopeConfiguration
<a name="aws-properties-codebuild-project-scopeconfiguration"></a>

Contains configuration information about the scope for a webhook.

## Syntax
<a name="aws-properties-codebuild-project-scopeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codebuild-project-scopeconfiguration-syntax.json"></a>

```
{
  "[Domain](#cfn-codebuild-project-scopeconfiguration-domain)" : {{String}},
  "[Name](#cfn-codebuild-project-scopeconfiguration-name)" : {{String}},
  "[Scope](#cfn-codebuild-project-scopeconfiguration-scope)" : {{String}}
}
```

### YAML
<a name="aws-properties-codebuild-project-scopeconfiguration-syntax.yaml"></a>

```
  [Domain](#cfn-codebuild-project-scopeconfiguration-domain): {{String}}
  [Name](#cfn-codebuild-project-scopeconfiguration-name): {{String}}
  [Scope](#cfn-codebuild-project-scopeconfiguration-scope): {{String}}
```

## Properties
<a name="aws-properties-codebuild-project-scopeconfiguration-properties"></a>

`Domain`  <a name="cfn-codebuild-project-scopeconfiguration-domain"></a>
The domain of the GitHub Enterprise organization or the GitLab Self Managed group. Note that this parameter is only required if your project's source type is GITHUB\_ENTERPRISE or GITLAB\_SELF\_MANAGED.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-codebuild-project-scopeconfiguration-name"></a>
The name of either the enterprise or organization that will send webhook events to CodeBuild, depending on if the webhook is a global or organization webhook respectively.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scope`  <a name="cfn-codebuild-project-scopeconfiguration-scope"></a>
The type of scope for a GitHub or GitLab webhook. The scope default is GITHUB\_ORGANIZATION.
*Required*: No
*Type*: String
*Allowed values*: `GITHUB_ORGANIZATION | GITHUB_GLOBAL | GITLAB_GROUP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
