---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-workspace-workspacetheme.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Workspace WorkspaceTheme
<a name="aws-properties-connect-workspace-workspacetheme"></a>

Contains theme configuration for a workspace, supporting both light and dark modes.

## Syntax
<a name="aws-properties-connect-workspace-workspacetheme-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-workspace-workspacetheme-syntax.json"></a>

```
{
  "[Dark](#cfn-connect-workspace-workspacetheme-dark)" : {{WorkspaceThemeConfig}},
  "[Light](#cfn-connect-workspace-workspacetheme-light)" : {{WorkspaceThemeConfig}}
}
```

### YAML
<a name="aws-properties-connect-workspace-workspacetheme-syntax.yaml"></a>

```
  [Dark](#cfn-connect-workspace-workspacetheme-dark): {{
    WorkspaceThemeConfig}}
  [Light](#cfn-connect-workspace-workspacetheme-light): {{
    WorkspaceThemeConfig}}
```

## Properties
<a name="aws-properties-connect-workspace-workspacetheme-properties"></a>

`Dark`  <a name="cfn-connect-workspace-workspacetheme-dark"></a>
The theme configuration for dark mode.
*Required*: No
*Type*: [WorkspaceThemeConfig](aws-properties-connect-workspace-workspacethemeconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Light`  <a name="cfn-connect-workspace-workspacetheme-light"></a>
The theme configuration for light mode.
*Required*: No
*Type*: [WorkspaceThemeConfig](aws-properties-connect-workspace-workspacethemeconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
