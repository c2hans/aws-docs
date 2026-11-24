---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-snapshotpolicy-snapshotpolicyschedule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::SnapshotPolicy SnapshotPolicySchedule

Specifies a schedule for an Amazon FSx for NetApp ONTAP snapshot policy.

## Syntax
<a name="aws-properties-fsx-snapshotpolicy-snapshotpolicyschedule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-snapshotpolicy-snapshotpolicyschedule-syntax.json"></a>

```json
{
  "[Count](#cfn-fsx-snapshotpolicy-snapshotpolicyschedule-count)" : {{Integer}},
  "[Name](#cfn-fsx-snapshotpolicy-snapshotpolicyschedule-name)" : {{String}},
  "[Prefix](#cfn-fsx-snapshotpolicy-snapshotpolicyschedule-prefix)" : {{String}},
  "[RetentionPeriod](#cfn-fsx-snapshotpolicy-snapshotpolicyschedule-retentionperiod)" : {{SnapshotPolicyRetentionPeriod}},
  "[SnapmirrorLabel](#cfn-fsx-snapshotpolicy-snapshotpolicyschedule-snapmirrorlabel)" : {{String}}
}
```

### YAML
<a name="aws-properties-fsx-snapshotpolicy-snapshotpolicyschedule-syntax.yaml"></a>

```yaml
  [Count](#cfn-fsx-snapshotpolicy-snapshotpolicyschedule-count): {{Integer}}
  [Name](#cfn-fsx-snapshotpolicy-snapshotpolicyschedule-name): {{String}}
  [Prefix](#cfn-fsx-snapshotpolicy-snapshotpolicyschedule-prefix): {{String}}
  [RetentionPeriod](#cfn-fsx-snapshotpolicy-snapshotpolicyschedule-retentionperiod): {{
    SnapshotPolicyRetentionPeriod}}
  [SnapmirrorLabel](#cfn-fsx-snapshotpolicy-snapshotpolicyschedule-snapmirrorlabel): {{String}}
```

## Properties
<a name="aws-properties-fsx-snapshotpolicy-snapshotpolicyschedule-properties"></a>

`Count`  <a name="cfn-fsx-snapshotpolicy-snapshotpolicyschedule-count"></a>
The number of snapshots to retain for the schedule.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `1023`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-fsx-snapshotpolicy-snapshotpolicyschedule-name"></a>
The name of the ONTAP schedule that determines when snapshots are created.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Prefix`  <a name="cfn-fsx-snapshotpolicy-snapshotpolicyschedule-prefix"></a>
The prefix for the schedule to use when creating snapshots.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RetentionPeriod`  <a name="cfn-fsx-snapshotpolicy-snapshotpolicyschedule-retentionperiod"></a>
The length of time that the snapshots that the schedule creates are locked. This setting applies only to volumes that have snapshot locking enabled.
*Required*: No
*Type*: [SnapshotPolicyRetentionPeriod](aws-properties-fsx-snapshotpolicy-snapshotpolicyretentionperiod.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SnapmirrorLabel`  <a name="cfn-fsx-snapshotpolicy-snapshotpolicyschedule-snapmirrorlabel"></a>
The SnapMirror label to assign to the snapshots that the schedule creates. SnapMirror policies use labels to select which snapshots to replicate to a destination volume.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `31`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
