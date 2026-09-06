---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-topic-rangeconstant.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Topic RangeConstant
<a name="aws-properties-quicksight-topic-rangeconstant"></a>

The value of the constant that is used to specify the endpoints of a range filter.

## Syntax
<a name="aws-properties-quicksight-topic-rangeconstant-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-topic-rangeconstant-syntax.json"></a>

```
{
  "[Maximum](#cfn-quicksight-topic-rangeconstant-maximum)" : {{String}},
  "[Minimum](#cfn-quicksight-topic-rangeconstant-minimum)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-topic-rangeconstant-syntax.yaml"></a>

```
  [Maximum](#cfn-quicksight-topic-rangeconstant-maximum): {{String}}
  [Minimum](#cfn-quicksight-topic-rangeconstant-minimum): {{String}}
```

## Properties
<a name="aws-properties-quicksight-topic-rangeconstant-properties"></a>

`Maximum`  <a name="cfn-quicksight-topic-rangeconstant-maximum"></a>
The maximum value for a range constant.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Minimum`  <a name="cfn-quicksight-topic-rangeconstant-minimum"></a>
The minimum value for a range constant.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
