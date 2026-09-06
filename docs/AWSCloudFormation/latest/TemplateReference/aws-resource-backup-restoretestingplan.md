---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-backup-restoretestingplan.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Backup::RestoreTestingPlan
<a name="aws-resource-backup-restoretestingplan"></a>

Creates a restore testing plan.

The first of two steps to create a restore testing plan. After this request is successful, finish the procedure using CreateRestoreTestingSelection.

## Syntax
<a name="aws-resource-backup-restoretestingplan-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-backup-restoretestingplan-syntax.json"></a>

```
{
  "Type" : "AWS::Backup::RestoreTestingPlan",
  "Properties" : {
      "[RecoveryPointSelection](#cfn-backup-restoretestingplan-recoverypointselection)" : {{RestoreTestingRecoveryPointSelection}},
      "[RestoreTestingPlanName](#cfn-backup-restoretestingplan-restoretestingplanname)" : {{String}},
      "[ScheduleExpression](#cfn-backup-restoretestingplan-scheduleexpression)" : {{String}},
      "[ScheduleExpressionTimezone](#cfn-backup-restoretestingplan-scheduleexpressiontimezone)" : {{String}},
      "[StartWindowHours](#cfn-backup-restoretestingplan-startwindowhours)" : {{Integer}},
      "[Tags](#cfn-backup-restoretestingplan-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-backup-restoretestingplan-syntax.yaml"></a>

```
Type: AWS::Backup::RestoreTestingPlan
Properties:
  [RecoveryPointSelection](#cfn-backup-restoretestingplan-recoverypointselection): {{
    RestoreTestingRecoveryPointSelection}}
  [RestoreTestingPlanName](#cfn-backup-restoretestingplan-restoretestingplanname): {{String}}
  [ScheduleExpression](#cfn-backup-restoretestingplan-scheduleexpression): {{String}}
  [ScheduleExpressionTimezone](#cfn-backup-restoretestingplan-scheduleexpressiontimezone): {{String}}
  [StartWindowHours](#cfn-backup-restoretestingplan-startwindowhours): {{Integer}}
  [Tags](#cfn-backup-restoretestingplan-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-backup-restoretestingplan-properties"></a>

`RecoveryPointSelection`  <a name="cfn-backup-restoretestingplan-recoverypointselection"></a>
The specified criteria to assign a set of resources, such as recovery point types or backup vaults.
*Required*: Yes
*Type*: [RestoreTestingRecoveryPointSelection](aws-properties-backup-restoretestingplan-restoretestingrecoverypointselection.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RestoreTestingPlanName`  <a name="cfn-backup-restoretestingplan-restoretestingplanname"></a>
The RestoreTestingPlanName is a unique string that is the name of the restore testing plan. This cannot be changed after creation, and it must consist of only alphanumeric characters and underscores.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ScheduleExpression`  <a name="cfn-backup-restoretestingplan-scheduleexpression"></a>
A CRON expression in specified timezone when a restore testing plan is executed. When no CRON expression is provided, AWS Backup will use the default expression `cron(0 5 ? * * *)`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScheduleExpressionTimezone`  <a name="cfn-backup-restoretestingplan-scheduleexpressiontimezone"></a>
Optional. This is the timezone in which the schedule expression is set. By default, ScheduleExpressions are in UTC. You can modify this to a specified timezone.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartWindowHours`  <a name="cfn-backup-restoretestingplan-startwindowhours"></a>
Defaults to 24 hours.
A value in hours after a restore test is scheduled before a job will be canceled if it doesn't start successfully. This value is optional. If this value is included, this parameter has a maximum value of 168 hours (one week).
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-backup-restoretestingplan-tags"></a>
Optional tags to include. A tag is a key-value pair you can use to manage, filter, and search for your resources. Allowed characters include UTF-8 letters,numbers, spaces, and the following characters: `+ - = . _ : /.`
*Required*: No
*Type*: Array of [Tag](aws-properties-backup-restoretestingplan-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-backup-restoretestingplan-return-values"></a>

### Ref
<a name="aws-resource-backup-restoretestingplan-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-backup-restoretestingplan-return-values-fn--getatt"></a>

####
<a name="aws-resource-backup-restoretestingplan-return-values-fn--getatt-fn--getatt"></a>

`RestoreTestingPlanArn`  <a name="RestoreTestingPlanArn-fn::getatt"></a>
An Amazon Resource Name (ARN) that uniquely identifies a restore testing plan.
