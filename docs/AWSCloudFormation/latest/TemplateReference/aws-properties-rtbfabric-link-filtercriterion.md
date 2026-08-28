---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rtbfabric-link-filtercriterion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::Link FilterCriterion
<a name="aws-properties-rtbfabric-link-filtercriterion"></a>

Describes the criteria for a filter.

## Syntax
<a name="aws-properties-rtbfabric-link-filtercriterion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rtbfabric-link-filtercriterion-syntax.json"></a>

```
{
  "[Path](#cfn-rtbfabric-link-filtercriterion-path)" : {{String}},
  "[Values](#cfn-rtbfabric-link-filtercriterion-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-rtbfabric-link-filtercriterion-syntax.yaml"></a>

```
  [Path](#cfn-rtbfabric-link-filtercriterion-path): {{String}}
  [Values](#cfn-rtbfabric-link-filtercriterion-values): {{
    - String}}
```

## Properties
<a name="aws-properties-rtbfabric-link-filtercriterion-properties"></a>

`Path`  <a name="cfn-rtbfabric-link-filtercriterion-path"></a>
The path to filter.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-rtbfabric-link-filtercriterion-values"></a>
The value to filter.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
