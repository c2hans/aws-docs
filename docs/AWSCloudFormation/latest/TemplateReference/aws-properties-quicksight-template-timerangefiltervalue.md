---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-timerangefiltervalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template TimeRangeFilterValue
<a name="aws-properties-quicksight-template-timerangefiltervalue"></a>

The value of a time range filter.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Syntax
<a name="aws-properties-quicksight-template-timerangefiltervalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-timerangefiltervalue-syntax.json"></a>

```
{
  "[Parameter](#cfn-quicksight-template-timerangefiltervalue-parameter)" : {{String}},
  "[RollingDate](#cfn-quicksight-template-timerangefiltervalue-rollingdate)" : {{RollingDateConfiguration}},
  "[StaticValue](#cfn-quicksight-template-timerangefiltervalue-staticvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-timerangefiltervalue-syntax.yaml"></a>

```
  [Parameter](#cfn-quicksight-template-timerangefiltervalue-parameter): {{String}}
  [RollingDate](#cfn-quicksight-template-timerangefiltervalue-rollingdate): {{
    RollingDateConfiguration}}
  [StaticValue](#cfn-quicksight-template-timerangefiltervalue-staticvalue): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-timerangefiltervalue-properties"></a>

`Parameter`  <a name="cfn-quicksight-template-timerangefiltervalue-parameter"></a>
The parameter type input value.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RollingDate`  <a name="cfn-quicksight-template-timerangefiltervalue-rollingdate"></a>
The rolling date input value.
*Required*: No
*Type*: [RollingDateConfiguration](aws-properties-quicksight-template-rollingdateconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StaticValue`  <a name="cfn-quicksight-template-timerangefiltervalue-staticvalue"></a>
The static input value.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
