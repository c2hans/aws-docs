---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-workspace-workspacethemetypography.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Workspace WorkspaceThemeTypography
<a name="aws-properties-connect-workspace-workspacethemetypography"></a>

Contains typography configuration for a workspace theme.

## Syntax
<a name="aws-properties-connect-workspace-workspacethemetypography-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-workspace-workspacethemetypography-syntax.json"></a>

```
{
  "[FontFamily](#cfn-connect-workspace-workspacethemetypography-fontfamily)" : {{FontFamily}}
}
```

### YAML
<a name="aws-properties-connect-workspace-workspacethemetypography-syntax.yaml"></a>

```
  [FontFamily](#cfn-connect-workspace-workspacethemetypography-fontfamily): {{
    FontFamily}}
```

## Properties
<a name="aws-properties-connect-workspace-workspacethemetypography-properties"></a>

`FontFamily`  <a name="cfn-connect-workspace-workspacethemetypography-fontfamily"></a>
The font family configuration for text in the workspace.
*Required*: No
*Type*: [FontFamily](aws-properties-connect-workspace-fontfamily.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
