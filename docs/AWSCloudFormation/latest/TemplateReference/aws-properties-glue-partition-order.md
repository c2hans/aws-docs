---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-partition-order.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Partition Order
<a name="aws-properties-glue-partition-order"></a>

Specifies the sort order of a sorted column.

## Syntax
<a name="aws-properties-glue-partition-order-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-partition-order-syntax.json"></a>

```
{
  "[Column](#cfn-glue-partition-order-column)" : {{String}},
  "[SortOrder](#cfn-glue-partition-order-sortorder)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-glue-partition-order-syntax.yaml"></a>

```
  [Column](#cfn-glue-partition-order-column): {{String}}
  [SortOrder](#cfn-glue-partition-order-sortorder): {{Integer}}
```

## Properties
<a name="aws-properties-glue-partition-order-properties"></a>

`Column`  <a name="cfn-glue-partition-order-column"></a>
The name of the column.
*Required*: Yes
*Type*: [String](aws-properties-glue-partition-column.md)
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SortOrder`  <a name="cfn-glue-partition-order-sortorder"></a>
Indicates that the column is sorted in ascending order (`== 1`), or in descending order (`==0`).
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
