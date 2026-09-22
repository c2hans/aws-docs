---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-personalize-filter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::Filter
<a name="aws-resource-personalize-filter"></a>

Contains information on a recommendation filter, including its ARN, status, and filter expression.

## Syntax
<a name="aws-resource-personalize-filter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-personalize-filter-syntax.json"></a>

```
{
  "Type" : "AWS::Personalize::Filter",
  "Properties" : {
      "[DatasetGroupArn](#cfn-personalize-filter-datasetgrouparn)" : {{String}},
      "[FilterExpression](#cfn-personalize-filter-filterexpression)" : {{String}},
      "[Name](#cfn-personalize-filter-name)" : {{String}},
      "[Tags](#cfn-personalize-filter-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-personalize-filter-syntax.yaml"></a>

```
Type: AWS::Personalize::Filter
Properties:
  [DatasetGroupArn](#cfn-personalize-filter-datasetgrouparn): {{String}}
  [FilterExpression](#cfn-personalize-filter-filterexpression): {{String}}
  [Name](#cfn-personalize-filter-name): {{String}}
  [Tags](#cfn-personalize-filter-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-personalize-filter-properties"></a>

`DatasetGroupArn`  <a name="cfn-personalize-filter-datasetgrouparn"></a>
The ARN of the dataset group to which the filter belongs.
*Required*: Yes
*Type*: String
*Pattern*: `arn:([a-z\d-]+):personalize:.*:.*:.+`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FilterExpression`  <a name="cfn-personalize-filter-filterexpression"></a>
Specifies the type of item interactions to filter out of recommendation results. The filter expression must follow specific format rules. For information about filter expression structure and syntax, see [Filter expressions](https://docs.aws.amazon.com/personalize/latest/dg/filter-expressions.html).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2500`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-personalize-filter-name"></a>
The name of the filter.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-personalize-filter-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-personalize-filter-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-personalize-filter-return-values"></a>

### Ref
<a name="aws-resource-personalize-filter-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-personalize-filter-return-values-fn--getatt"></a>

####
<a name="aws-resource-personalize-filter-return-values-fn--getatt-fn--getatt"></a>

`CreationDateTime`  <a name="CreationDateTime-fn::getatt"></a>
The time at which the filter was created.

`FilterArn`  <a name="FilterArn-fn::getatt"></a>
The ARN of the filter.

`LastUpdatedDateTime`  <a name="LastUpdatedDateTime-fn::getatt"></a>
The time at which the filter was last updated.

`Status`  <a name="Status-fn::getatt"></a>
The status of the filter.
