---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-scheduler-schedulegroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Scheduler::ScheduleGroup
<a name="aws-resource-scheduler-schedulegroup"></a>

 A *schedule group* is an Amazon EventBridge Scheduler resource you use to organize your schedules.

 Your AWS account comes with a `default` scheduler group. You associate a new schedule with the `default` group or with schedule groups that you create and manage. You can create up to [500 schedule groups](https://docs.aws.amazon.com/scheduler/latest/UserGuide/scheduler-quotas.html) in your AWS account. With EventBridge Scheduler, you apply [tags](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) to schedule groups, not to individual schedules to organize your resources.

 For more information about managing schedule groups, see [Managing a schedule group](https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-schedule-group.html) in the *EventBridge Scheduler User Guide*.

## Syntax
<a name="aws-resource-scheduler-schedulegroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-scheduler-schedulegroup-syntax.json"></a>

```
{
  "Type" : "AWS::Scheduler::ScheduleGroup",
  "Properties" : {
      "[Name](#cfn-scheduler-schedulegroup-name)" : {{String}},
      "[Tags](#cfn-scheduler-schedulegroup-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-scheduler-schedulegroup-syntax.yaml"></a>

```
Type: AWS::Scheduler::ScheduleGroup
Properties:
  [Name](#cfn-scheduler-schedulegroup-name): {{String}}
  [Tags](#cfn-scheduler-schedulegroup-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-scheduler-schedulegroup-properties"></a>

`Name`  <a name="cfn-scheduler-schedulegroup-name"></a>
The name of the schedule group.
*Required*: No
*Type*: String
*Pattern*: `^[0-9a-zA-Z-_.]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-scheduler-schedulegroup-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-scheduler-schedulegroup-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-scheduler-schedulegroup-return-values"></a>

### Ref
<a name="aws-resource-scheduler-schedulegroup-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `Name` attribute of the schedule group.

### Fn::GetAtt
<a name="aws-resource-scheduler-schedulegroup-return-values-fn--getatt"></a>

 The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes that `Fn::GetAtt` returns. For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-scheduler-schedulegroup-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the schedule group.

`CreationDate`  <a name="CreationDate-fn::getatt"></a>
The date and time at which the schedule group was created.

`LastModificationDate`  <a name="LastModificationDate-fn::getatt"></a>
 The time at which the schedule group was last modified.

`State`  <a name="State-fn::getatt"></a>
Specifies the state of the schedule group.
*Allowed Values*: `ACTIVE` \| `DELETING`
