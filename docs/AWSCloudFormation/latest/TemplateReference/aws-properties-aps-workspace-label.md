---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aps-workspace-label.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::Workspace Label
<a name="aws-properties-aps-workspace-label"></a>

A label is a name:value pair used to add context to ingested metrics. This structure defines the name and value for one label that is used in a label set. You can set ingestion limits on time series that match defined label sets, to help prevent a workspace from being overwhelmed with unexpected spikes in time series ingestion.

## Syntax
<a name="aws-properties-aps-workspace-label-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aps-workspace-label-syntax.json"></a>

```
{
  "[Name](#cfn-aps-workspace-label-name)" : {{String}},
  "[Value](#cfn-aps-workspace-label-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-aps-workspace-label-syntax.yaml"></a>

```
  [Name](#cfn-aps-workspace-label-name): {{String}}
  [Value](#cfn-aps-workspace-label-value): {{String}}
```

## Properties
<a name="aws-properties-aps-workspace-label-properties"></a>

`Name`  <a name="cfn-aps-workspace-label-name"></a>
The name for this label.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z_][a-zA-Z0-9_]*$`
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-aps-workspace-label-value"></a>
The value for this label.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
