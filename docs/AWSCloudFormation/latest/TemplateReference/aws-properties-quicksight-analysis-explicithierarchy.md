---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-explicithierarchy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis ExplicitHierarchy
<a name="aws-properties-quicksight-analysis-explicithierarchy"></a>

The option that determines the hierarchy of the fields that are built within a visual's field wells. These fields can't be duplicated to other visuals.

## Syntax
<a name="aws-properties-quicksight-analysis-explicithierarchy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-explicithierarchy-syntax.json"></a>

```
{
  "[Columns](#cfn-quicksight-analysis-explicithierarchy-columns)" : {{[ ColumnIdentifier, ... ]}},
  "[DrillDownFilters](#cfn-quicksight-analysis-explicithierarchy-drilldownfilters)" : {{[ DrillDownFilter, ... ]}},
  "[HierarchyId](#cfn-quicksight-analysis-explicithierarchy-hierarchyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-explicithierarchy-syntax.yaml"></a>

```
  [Columns](#cfn-quicksight-analysis-explicithierarchy-columns): {{
    - ColumnIdentifier}}
  [DrillDownFilters](#cfn-quicksight-analysis-explicithierarchy-drilldownfilters): {{
    - DrillDownFilter}}
  [HierarchyId](#cfn-quicksight-analysis-explicithierarchy-hierarchyid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-explicithierarchy-properties"></a>

`Columns`  <a name="cfn-quicksight-analysis-explicithierarchy-columns"></a>
The list of columns that define the explicit hierarchy.
*Required*: Yes
*Type*: Array of [ColumnIdentifier](aws-properties-quicksight-analysis-columnidentifier.md)
*Minimum*: `2`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DrillDownFilters`  <a name="cfn-quicksight-analysis-explicithierarchy-drilldownfilters"></a>
The option that determines the drill down filters for the explicit hierarchy.
*Required*: No
*Type*: Array of [DrillDownFilter](aws-properties-quicksight-analysis-drilldownfilter.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HierarchyId`  <a name="cfn-quicksight-analysis-explicithierarchy-hierarchyid"></a>
The hierarchy ID of the explicit hierarchy.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
