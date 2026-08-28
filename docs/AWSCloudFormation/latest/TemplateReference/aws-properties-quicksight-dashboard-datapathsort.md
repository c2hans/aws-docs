---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-datapathsort.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard DataPathSort
<a name="aws-properties-quicksight-dashboard-datapathsort"></a>

Allows data paths to be sorted by a specific data value.

## Syntax
<a name="aws-properties-quicksight-dashboard-datapathsort-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-datapathsort-syntax.json"></a>

```
{
  "[Direction](#cfn-quicksight-dashboard-datapathsort-direction)" : {{String}},
  "[SortPaths](#cfn-quicksight-dashboard-datapathsort-sortpaths)" : {{[ DataPathValue, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-datapathsort-syntax.yaml"></a>

```
  [Direction](#cfn-quicksight-dashboard-datapathsort-direction): {{String}}
  [SortPaths](#cfn-quicksight-dashboard-datapathsort-sortpaths): {{
    - DataPathValue}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-datapathsort-properties"></a>

`Direction`  <a name="cfn-quicksight-dashboard-datapathsort-direction"></a>
Determines the sort direction.
*Required*: Yes
*Type*: String
*Allowed values*: `ASC | DESC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SortPaths`  <a name="cfn-quicksight-dashboard-datapathsort-sortpaths"></a>
The list of data paths that need to be sorted.
*Required*: Yes
*Type*: Array of [DataPathValue](aws-properties-quicksight-dashboard-datapathvalue.md)
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
