---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-transformstep.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet TransformStep
<a name="aws-properties-quicksight-dataset-transformstep"></a>

A step in data preparation that performs a specific operation on the data.

## Syntax
<a name="aws-properties-quicksight-dataset-transformstep-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-transformstep-syntax.json"></a>

```
{
  "[AggregateStep](#cfn-quicksight-dataset-transformstep-aggregatestep)" : {{AggregateOperation}},
  "[AppendStep](#cfn-quicksight-dataset-transformstep-appendstep)" : {{AppendOperation}},
  "[CastColumnTypesStep](#cfn-quicksight-dataset-transformstep-castcolumntypesstep)" : {{CastColumnTypesOperation}},
  "[CreateColumnsStep](#cfn-quicksight-dataset-transformstep-createcolumnsstep)" : {{CreateColumnsOperation}},
  "[FiltersStep](#cfn-quicksight-dataset-transformstep-filtersstep)" : {{FiltersOperation}},
  "[ImportTableStep](#cfn-quicksight-dataset-transformstep-importtablestep)" : {{ImportTableOperation}},
  "[JoinStep](#cfn-quicksight-dataset-transformstep-joinstep)" : {{JoinOperation}},
  "[PivotStep](#cfn-quicksight-dataset-transformstep-pivotstep)" : {{PivotOperation}},
  "[ProjectStep](#cfn-quicksight-dataset-transformstep-projectstep)" : {{ProjectOperation}},
  "[RenameColumnsStep](#cfn-quicksight-dataset-transformstep-renamecolumnsstep)" : {{RenameColumnsOperation}},
  "[UnpivotStep](#cfn-quicksight-dataset-transformstep-unpivotstep)" : {{UnpivotOperation}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-transformstep-syntax.yaml"></a>

```
  [AggregateStep](#cfn-quicksight-dataset-transformstep-aggregatestep): {{
    AggregateOperation}}
  [AppendStep](#cfn-quicksight-dataset-transformstep-appendstep): {{
    AppendOperation}}
  [CastColumnTypesStep](#cfn-quicksight-dataset-transformstep-castcolumntypesstep): {{
    CastColumnTypesOperation}}
  [CreateColumnsStep](#cfn-quicksight-dataset-transformstep-createcolumnsstep): {{
    CreateColumnsOperation}}
  [FiltersStep](#cfn-quicksight-dataset-transformstep-filtersstep): {{
    FiltersOperation}}
  [ImportTableStep](#cfn-quicksight-dataset-transformstep-importtablestep): {{
    ImportTableOperation}}
  [JoinStep](#cfn-quicksight-dataset-transformstep-joinstep): {{
    JoinOperation}}
  [PivotStep](#cfn-quicksight-dataset-transformstep-pivotstep): {{
    PivotOperation}}
  [ProjectStep](#cfn-quicksight-dataset-transformstep-projectstep): {{
    ProjectOperation}}
  [RenameColumnsStep](#cfn-quicksight-dataset-transformstep-renamecolumnsstep): {{
    RenameColumnsOperation}}
  [UnpivotStep](#cfn-quicksight-dataset-transformstep-unpivotstep): {{
    UnpivotOperation}}
```

## Properties
<a name="aws-properties-quicksight-dataset-transformstep-properties"></a>

`AggregateStep`  <a name="cfn-quicksight-dataset-transformstep-aggregatestep"></a>
A transform step that groups data and applies aggregation functions to calculate summary values.
*Required*: No
*Type*: [AggregateOperation](aws-properties-quicksight-dataset-aggregateoperation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AppendStep`  <a name="cfn-quicksight-dataset-transformstep-appendstep"></a>
A transform step that combines rows from multiple sources by stacking them vertically.
*Required*: No
*Type*: [AppendOperation](aws-properties-quicksight-dataset-appendoperation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CastColumnTypesStep`  <a name="cfn-quicksight-dataset-transformstep-castcolumntypesstep"></a>
A transform step that changes the data types of one or more columns.
*Required*: No
*Type*: [CastColumnTypesOperation](aws-properties-quicksight-dataset-castcolumntypesoperation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreateColumnsStep`  <a name="cfn-quicksight-dataset-transformstep-createcolumnsstep"></a>
Property description not available.
*Required*: No
*Type*: [CreateColumnsOperation](aws-properties-quicksight-dataset-createcolumnsoperation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FiltersStep`  <a name="cfn-quicksight-dataset-transformstep-filtersstep"></a>
A transform step that applies filter conditions.
*Required*: No
*Type*: [FiltersOperation](aws-properties-quicksight-dataset-filtersoperation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImportTableStep`  <a name="cfn-quicksight-dataset-transformstep-importtablestep"></a>
A transform step that brings data from a source table.
*Required*: No
*Type*: [ImportTableOperation](aws-properties-quicksight-dataset-importtableoperation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JoinStep`  <a name="cfn-quicksight-dataset-transformstep-joinstep"></a>
A transform step that combines data from two sources based on specified join conditions.
*Required*: No
*Type*: [JoinOperation](aws-properties-quicksight-dataset-joinoperation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PivotStep`  <a name="cfn-quicksight-dataset-transformstep-pivotstep"></a>
A transform step that converts row values into columns to reshape the data structure.
*Required*: No
*Type*: [PivotOperation](aws-properties-quicksight-dataset-pivotoperation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProjectStep`  <a name="cfn-quicksight-dataset-transformstep-projectstep"></a>
Property description not available.
*Required*: No
*Type*: [ProjectOperation](aws-properties-quicksight-dataset-projectoperation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RenameColumnsStep`  <a name="cfn-quicksight-dataset-transformstep-renamecolumnsstep"></a>
A transform step that changes the names of one or more columns.
*Required*: No
*Type*: [RenameColumnsOperation](aws-properties-quicksight-dataset-renamecolumnsoperation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UnpivotStep`  <a name="cfn-quicksight-dataset-transformstep-unpivotstep"></a>
A transform step that converts columns into rows to normalize the data structure.
*Required*: No
*Type*: [UnpivotOperation](aws-properties-quicksight-dataset-unpivotoperation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
