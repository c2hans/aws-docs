---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lakeformation-datacellsfilter-rowfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LakeFormation::DataCellsFilter RowFilter
<a name="aws-properties-lakeformation-datacellsfilter-rowfilter"></a>

A PartiQL predicate.

## Syntax
<a name="aws-properties-lakeformation-datacellsfilter-rowfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lakeformation-datacellsfilter-rowfilter-syntax.json"></a>

```
{
  "[AllRowsWildcard](#cfn-lakeformation-datacellsfilter-rowfilter-allrowswildcard)" : {{Json}},
  "[FilterExpression](#cfn-lakeformation-datacellsfilter-rowfilter-filterexpression)" : {{String}}
}
```

### YAML
<a name="aws-properties-lakeformation-datacellsfilter-rowfilter-syntax.yaml"></a>

```
  [AllRowsWildcard](#cfn-lakeformation-datacellsfilter-rowfilter-allrowswildcard): {{Json}}
  [FilterExpression](#cfn-lakeformation-datacellsfilter-rowfilter-filterexpression): {{String}}
```

## Properties
<a name="aws-properties-lakeformation-datacellsfilter-rowfilter-properties"></a>

`AllRowsWildcard`  <a name="cfn-lakeformation-datacellsfilter-rowfilter-allrowswildcard"></a>
A wildcard for all rows.
*Required*: No
*Type*: Json
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FilterExpression`  <a name="cfn-lakeformation-datacellsfilter-rowfilter-filterexpression"></a>
A filter expression.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
