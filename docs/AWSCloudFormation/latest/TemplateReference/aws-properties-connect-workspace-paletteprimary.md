---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-workspace-paletteprimary.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Workspace PalettePrimary
<a name="aws-properties-connect-workspace-paletteprimary"></a>

Contains primary color configuration for a workspace theme.

## Syntax
<a name="aws-properties-connect-workspace-paletteprimary-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-workspace-paletteprimary-syntax.json"></a>

```
{
  "[Active](#cfn-connect-workspace-paletteprimary-active)" : {{String}},
  "[ContrastText](#cfn-connect-workspace-paletteprimary-contrasttext)" : {{String}},
  "[Default](#cfn-connect-workspace-paletteprimary-default)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-workspace-paletteprimary-syntax.yaml"></a>

```
  [Active](#cfn-connect-workspace-paletteprimary-active): {{String}}
  [ContrastText](#cfn-connect-workspace-paletteprimary-contrasttext): {{String}}
  [Default](#cfn-connect-workspace-paletteprimary-default): {{String}}
```

## Properties
<a name="aws-properties-connect-workspace-paletteprimary-properties"></a>

`Active`  <a name="cfn-connect-workspace-paletteprimary-active"></a>
The primary color used for active states.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContrastText`  <a name="cfn-connect-workspace-paletteprimary-contrasttext"></a>
The text color that contrasts with the primary color for readability.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Default`  <a name="cfn-connect-workspace-paletteprimary-default"></a>
The default primary color used throughout the workspace.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
