---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-entity.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard Entity
<a name="aws-properties-quicksight-dashboard-entity"></a>

An object, structure, or sub-structure of an analysis, template, or dashboard.

## Syntax
<a name="aws-properties-quicksight-dashboard-entity-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-entity-syntax.json"></a>

```
{
  "[Path](#cfn-quicksight-dashboard-entity-path)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-entity-syntax.yaml"></a>

```
  [Path](#cfn-quicksight-dashboard-entity-path): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-entity-properties"></a>

`Path`  <a name="cfn-quicksight-dashboard-entity-path"></a>
The hierarchical path of the entity within the analysis, template, or dashboard definition tree.
*Required*: No
*Type*: String
*Pattern*: `\S`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
