---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshift-snapshotschedule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Redshift::SnapshotSchedule
<a name="aws-resource-redshift-snapshotschedule"></a>

Describes a snapshot schedule. You can set a regular interval for creating snapshots of a cluster. You can also schedule snapshots for specific dates.

## Syntax
<a name="aws-resource-redshift-snapshotschedule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-redshift-snapshotschedule-syntax.json"></a>

```
{
  "Type" : "AWS::Redshift::SnapshotSchedule",
  "Properties" : {
      "[ScheduleDefinitions](#cfn-redshift-snapshotschedule-scheduledefinitions)" : {{[ String, ... ]}},
      "[ScheduleDescription](#cfn-redshift-snapshotschedule-scheduledescription)" : {{String}},
      "[ScheduleIdentifier](#cfn-redshift-snapshotschedule-scheduleidentifier)" : {{String}},
      "[Tags](#cfn-redshift-snapshotschedule-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-redshift-snapshotschedule-syntax.yaml"></a>

```
Type: AWS::Redshift::SnapshotSchedule
Properties:
  [ScheduleDefinitions](#cfn-redshift-snapshotschedule-scheduledefinitions): {{
    - String}}
  [ScheduleDescription](#cfn-redshift-snapshotschedule-scheduledescription): {{String}}
  [ScheduleIdentifier](#cfn-redshift-snapshotschedule-scheduleidentifier): {{String}}
  [Tags](#cfn-redshift-snapshotschedule-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-redshift-snapshotschedule-properties"></a>

`ScheduleDefinitions`  <a name="cfn-redshift-snapshotschedule-scheduledefinitions"></a>
A list of ScheduleDefinitions.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScheduleDescription`  <a name="cfn-redshift-snapshotschedule-scheduledescription"></a>
The description of the schedule.
*Required*: No
*Type*: String
*Maximum*: `2147483647`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ScheduleIdentifier`  <a name="cfn-redshift-snapshotschedule-scheduleidentifier"></a>
A unique identifier for the schedule.
*Required*: Yes
*Type*: String
*Maximum*: `2147483647`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-redshift-snapshotschedule-tags"></a>
An optional set of tags describing the schedule.
*Required*: No
*Type*: Array of [Tag](aws-properties-redshift-snapshotschedule-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-redshift-snapshotschedule-return-values"></a>

### Ref
<a name="aws-resource-redshift-snapshotschedule-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-redshift-snapshotschedule-return-values-fn--getatt"></a>

####
<a name="aws-resource-redshift-snapshotschedule-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`AssociatedClusterCount`  <a name="AssociatedClusterCount-fn::getatt"></a>
The number of clusters associated with the schedule.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
