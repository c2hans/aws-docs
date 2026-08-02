---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-gradientstop.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis GradientStop
<a name="aws-properties-quicksight-analysis-gradientstop"></a>

Determines the gradient stop configuration.

## Syntax
<a name="aws-properties-quicksight-analysis-gradientstop-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-gradientstop-syntax.json"></a>

```
{
  "[Color](#cfn-quicksight-analysis-gradientstop-color)" : {{String}},
  "[DataValue](#cfn-quicksight-analysis-gradientstop-datavalue)" : {{Number}},
  "[GradientOffset](#cfn-quicksight-analysis-gradientstop-gradientoffset)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-gradientstop-syntax.yaml"></a>

```
  [Color](#cfn-quicksight-analysis-gradientstop-color): {{String}}
  [DataValue](#cfn-quicksight-analysis-gradientstop-datavalue): {{Number}}
  [GradientOffset](#cfn-quicksight-analysis-gradientstop-gradientoffset): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-analysis-gradientstop-properties"></a>

`Color`  <a name="cfn-quicksight-analysis-gradientstop-color"></a>
Determines the color.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataValue`  <a name="cfn-quicksight-analysis-gradientstop-datavalue"></a>
Determines the data value.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GradientOffset`  <a name="cfn-quicksight-analysis-gradientstop-gradientoffset"></a>
Determines gradient offset value.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
