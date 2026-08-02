---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-rowlevelpermissiontagrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet RowLevelPermissionTagRule
<a name="aws-properties-quicksight-dataset-rowlevelpermissiontagrule"></a>

A set of rules associated with a tag.

## Syntax
<a name="aws-properties-quicksight-dataset-rowlevelpermissiontagrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-rowlevelpermissiontagrule-syntax.json"></a>

```
{
  "[ColumnName](#cfn-quicksight-dataset-rowlevelpermissiontagrule-columnname)" : {{String}},
  "[MatchAllValue](#cfn-quicksight-dataset-rowlevelpermissiontagrule-matchallvalue)" : {{String}},
  "[TagKey](#cfn-quicksight-dataset-rowlevelpermissiontagrule-tagkey)" : {{String}},
  "[TagMultiValueDelimiter](#cfn-quicksight-dataset-rowlevelpermissiontagrule-tagmultivaluedelimiter)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-rowlevelpermissiontagrule-syntax.yaml"></a>

```
  [ColumnName](#cfn-quicksight-dataset-rowlevelpermissiontagrule-columnname): {{String}}
  [MatchAllValue](#cfn-quicksight-dataset-rowlevelpermissiontagrule-matchallvalue): {{String}}
  [TagKey](#cfn-quicksight-dataset-rowlevelpermissiontagrule-tagkey): {{String}}
  [TagMultiValueDelimiter](#cfn-quicksight-dataset-rowlevelpermissiontagrule-tagmultivaluedelimiter): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-rowlevelpermissiontagrule-properties"></a>

`ColumnName`  <a name="cfn-quicksight-dataset-rowlevelpermissiontagrule-columnname"></a>
The column name that a tag key is assigned to.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchAllValue`  <a name="cfn-quicksight-dataset-rowlevelpermissiontagrule-matchallvalue"></a>
A string that you want to use to filter by all the values in a column in the dataset and don’t want to list the values one by one. For example, you can use an asterisk as your match all value.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TagKey`  <a name="cfn-quicksight-dataset-rowlevelpermissiontagrule-tagkey"></a>
The unique key for a tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TagMultiValueDelimiter`  <a name="cfn-quicksight-dataset-rowlevelpermissiontagrule-tagmultivaluedelimiter"></a>
A string that you want to use to delimit the values when you pass the values at run time. For example, you can delimit the values with a comma.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
