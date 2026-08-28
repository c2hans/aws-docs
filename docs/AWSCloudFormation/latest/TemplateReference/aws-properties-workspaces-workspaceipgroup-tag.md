---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspaces-workspaceipgroup-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpaces::WorkspaceIpGroup Tag
<a name="aws-properties-workspaces-workspaceipgroup-tag"></a>

Describes a tag.

## Syntax
<a name="aws-properties-workspaces-workspaceipgroup-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspaces-workspaceipgroup-tag-syntax.json"></a>

```
{
  "[Key](#cfn-workspaces-workspaceipgroup-tag-key)" : {{String}},
  "[Value](#cfn-workspaces-workspaceipgroup-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-workspaces-workspaceipgroup-tag-syntax.yaml"></a>

```
  [Key](#cfn-workspaces-workspaceipgroup-tag-key): {{String}}
  [Value](#cfn-workspaces-workspaceipgroup-tag-value): {{String}}
```

## Properties
<a name="aws-properties-workspaces-workspaceipgroup-tag-properties"></a>

`Key`  <a name="cfn-workspaces-workspaceipgroup-tag-key"></a>
The key of the tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-workspaces-workspaceipgroup-tag-value"></a>
The value of the tag.
*Required*: Yes
*Type*: String
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
