---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-redshiftserverless-workgroup-performancetarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RedshiftServerless::Workgroup PerformanceTarget
<a name="aws-properties-redshiftserverless-workgroup-performancetarget"></a>

An object that represents the price performance target settings for the workgroup.

## Syntax
<a name="aws-properties-redshiftserverless-workgroup-performancetarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-redshiftserverless-workgroup-performancetarget-syntax.json"></a>

```
{
  "[Level](#cfn-redshiftserverless-workgroup-performancetarget-level)" : {{Integer}},
  "[Status](#cfn-redshiftserverless-workgroup-performancetarget-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-redshiftserverless-workgroup-performancetarget-syntax.yaml"></a>

```
  [Level](#cfn-redshiftserverless-workgroup-performancetarget-level): {{Integer}}
  [Status](#cfn-redshiftserverless-workgroup-performancetarget-status): {{String}}
```

## Properties
<a name="aws-properties-redshiftserverless-workgroup-performancetarget-properties"></a>

`Level`  <a name="cfn-redshiftserverless-workgroup-performancetarget-level"></a>
The target price performance level for the workgroup. Valid values include 1, 25, 50, 75, and 100. These correspond to the price performance levels LOW\_COST, ECONOMICAL, BALANCED, RESOURCEFUL, and HIGH\_PERFORMANCE.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-redshiftserverless-workgroup-performancetarget-status"></a>
Whether the price performance target is enabled for the workgroup.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
