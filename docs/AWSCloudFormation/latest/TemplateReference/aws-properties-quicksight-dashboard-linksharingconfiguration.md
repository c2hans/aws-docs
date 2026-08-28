---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-linksharingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard LinkSharingConfiguration
<a name="aws-properties-quicksight-dashboard-linksharingconfiguration"></a>

A structure that contains the configuration of a shareable link to the dashboard.

## Syntax
<a name="aws-properties-quicksight-dashboard-linksharingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-linksharingconfiguration-syntax.json"></a>

```
{
  "[Permissions](#cfn-quicksight-dashboard-linksharingconfiguration-permissions)" : {{[ ResourcePermission, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-linksharingconfiguration-syntax.yaml"></a>

```
  [Permissions](#cfn-quicksight-dashboard-linksharingconfiguration-permissions): {{
    - ResourcePermission}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-linksharingconfiguration-properties"></a>

`Permissions`  <a name="cfn-quicksight-dashboard-linksharingconfiguration-permissions"></a>
A structure that contains the permissions of a shareable link.
*Required*: No
*Type*: Array of [ResourcePermission](aws-properties-quicksight-dashboard-resourcepermission.md)
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
