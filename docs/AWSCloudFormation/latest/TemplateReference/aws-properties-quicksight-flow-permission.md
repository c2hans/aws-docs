---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-flow-permission.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Flow Permission
<a name="aws-properties-quicksight-flow-permission"></a>

<a name="aws-properties-quicksight-flow-permission-description"></a>The `Permission` property type specifies Property description not available. for an [AWS::QuickSight::Flow](aws-resource-quicksight-flow.md).

## Syntax
<a name="aws-properties-quicksight-flow-permission-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-flow-permission-syntax.json"></a>

```
{
  "[Actions](#cfn-quicksight-flow-permission-actions)" : {{[ String, ... ]}},
  "[Principal](#cfn-quicksight-flow-permission-principal)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-flow-permission-syntax.yaml"></a>

```
  [Actions](#cfn-quicksight-flow-permission-actions): {{
    - String}}
  [Principal](#cfn-quicksight-flow-permission-principal): {{String}}
```

## Properties
<a name="aws-properties-quicksight-flow-permission-properties"></a>

`Actions`  <a name="cfn-quicksight-flow-permission-actions"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Principal`  <a name="cfn-quicksight-flow-permission-principal"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
