---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instanceeventwindow.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::InstanceEventWindow
<a name="aws-resource-ec2-instanceeventwindow"></a>

The event window.

## Syntax
<a name="aws-resource-ec2-instanceeventwindow-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-instanceeventwindow-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::InstanceEventWindow",
  "Properties" : {
      "[CronExpression](#cfn-ec2-instanceeventwindow-cronexpression)" : {{String}},
      "[Name](#cfn-ec2-instanceeventwindow-name)" : {{String}},
      "[Tags](#cfn-ec2-instanceeventwindow-tags)" : {{[ Tag, ... ]}},
      "[TimeRanges](#cfn-ec2-instanceeventwindow-timeranges)" : {{[ TimeRange, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ec2-instanceeventwindow-syntax.yaml"></a>

```
Type: AWS::EC2::InstanceEventWindow
Properties:
  [CronExpression](#cfn-ec2-instanceeventwindow-cronexpression): {{String}}
  [Name](#cfn-ec2-instanceeventwindow-name): {{String}}
  [Tags](#cfn-ec2-instanceeventwindow-tags): {{
    - Tag}}
  [TimeRanges](#cfn-ec2-instanceeventwindow-timeranges): {{
    - TimeRange}}
```

## Properties
<a name="aws-resource-ec2-instanceeventwindow-properties"></a>

`CronExpression`  <a name="cfn-ec2-instanceeventwindow-cronexpression"></a>
The cron expression defined for the event window.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-ec2-instanceeventwindow-name"></a>
The name of the event window.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ec2-instanceeventwindow-tags"></a>
The instance tags associated with the event window.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-instanceeventwindow-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeRanges`  <a name="cfn-ec2-instanceeventwindow-timeranges"></a>
One or more time ranges defined for the event window.
*Required*: No
*Type*: Array of [TimeRange](aws-properties-ec2-instanceeventwindow-timerange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-instanceeventwindow-return-values"></a>

### Ref
<a name="aws-resource-ec2-instanceeventwindow-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ec2-instanceeventwindow-return-values-fn--getatt"></a>

####
<a name="aws-resource-ec2-instanceeventwindow-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`InstanceEventWindowId`  <a name="InstanceEventWindowId-fn::getatt"></a>
The ID of the event window.

`State`  <a name="State-fn::getatt"></a>
The current state of the event window.
