---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-columnsemantictype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet ColumnSemanticType
<a name="aws-properties-quicksight-dataset-columnsemantictype"></a>

The semantic type information for a column in the new data preparation experience.

## Syntax
<a name="aws-properties-quicksight-dataset-columnsemantictype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-columnsemantictype-syntax.json"></a>

```
{
  "[GeographicalRole](#cfn-quicksight-dataset-columnsemantictype-geographicalrole)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-columnsemantictype-syntax.yaml"></a>

```
  [GeographicalRole](#cfn-quicksight-dataset-columnsemantictype-geographicalrole): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-columnsemantictype-properties"></a>

`GeographicalRole`  <a name="cfn-quicksight-dataset-columnsemantictype-geographicalrole"></a>
The geographical role of the column in the new data preparation experience.
*Required*: No
*Type*: String
*Allowed values*: `COUNTRY | STATE | COUNTY | CITY | POSTCODE | LONGITUDE | LATITUDE | POLITICAL1 | CENSUS_TRACT | CENSUS_BLOCK_GROUP | CENSUS_BLOCK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
