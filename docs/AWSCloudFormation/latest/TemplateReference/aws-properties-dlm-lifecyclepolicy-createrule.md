---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dlm-lifecyclepolicy-createrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DLM::LifecyclePolicy CreateRule
<a name="aws-properties-dlm-lifecyclepolicy-createrule"></a>

**[Custom snapshot and AMI policies only]** Specifies when the policy should create snapshots or AMIs.

**Note**
You must specify either **CronExpression**, or **Interval**, **IntervalUnit**, and **Times**.
If you need to specify an [ArchiveRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_ArchiveRule.html) for the schedule, then you must specify a creation frequency of at least 28 days.

## Syntax
<a name="aws-properties-dlm-lifecyclepolicy-createrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dlm-lifecyclepolicy-createrule-syntax.json"></a>

```
{
  "[CronExpression](#cfn-dlm-lifecyclepolicy-createrule-cronexpression)" : {{String}},
  "[Interval](#cfn-dlm-lifecyclepolicy-createrule-interval)" : {{Integer}},
  "[IntervalUnit](#cfn-dlm-lifecyclepolicy-createrule-intervalunit)" : {{String}},
  "[Location](#cfn-dlm-lifecyclepolicy-createrule-location)" : {{String}},
  "[Scripts](#cfn-dlm-lifecyclepolicy-createrule-scripts)" : {{[ Script, ... ]}},
  "[Times](#cfn-dlm-lifecyclepolicy-createrule-times)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-dlm-lifecyclepolicy-createrule-syntax.yaml"></a>

```
  [CronExpression](#cfn-dlm-lifecyclepolicy-createrule-cronexpression): {{String}}
  [Interval](#cfn-dlm-lifecyclepolicy-createrule-interval): {{Integer}}
  [IntervalUnit](#cfn-dlm-lifecyclepolicy-createrule-intervalunit): {{String}}
  [Location](#cfn-dlm-lifecyclepolicy-createrule-location): {{String}}
  [Scripts](#cfn-dlm-lifecyclepolicy-createrule-scripts): {{
    - Script}}
  [Times](#cfn-dlm-lifecyclepolicy-createrule-times): {{
    - String}}
```

## Properties
<a name="aws-properties-dlm-lifecyclepolicy-createrule-properties"></a>

`CronExpression`  <a name="cfn-dlm-lifecyclepolicy-createrule-cronexpression"></a>
The schedule, as a Cron expression. The schedule interval must be between 1 hour and 1 year. For more information, see the [Cron and rate expressions](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-scheduled-rule-pattern.html) in the *Amazon EventBridge User Guide*.
*Required*: No
*Type*: String
*Pattern*: `cron\([^\n]{11,100}\)`
*Minimum*: `17`
*Maximum*: `106`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interval`  <a name="cfn-dlm-lifecyclepolicy-createrule-interval"></a>
The interval between snapshots. The supported values are 1, 2, 3, 4, 6, 8, 12, and 24.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IntervalUnit`  <a name="cfn-dlm-lifecyclepolicy-createrule-intervalunit"></a>
The interval unit.
*Required*: No
*Type*: String
*Allowed values*: `HOURS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Location`  <a name="cfn-dlm-lifecyclepolicy-createrule-location"></a>
**[Custom snapshot policies only]** Specifies the destination for snapshots created by the policy. The allowed destinations depend on the location of the targeted resources.
+ If the policy targets resources in a Region, then you must create snapshots in the same Region as the source resource.
+ If the policy targets resources in a Local Zone, you can create snapshots in the same Local Zone or in its parent Region.
+ If the policy targets resources on an Outpost, then you can create snapshots on the same Outpost or in its parent Region.
Specify one of the following values:
+ To create snapshots in the same Region as the source resource, specify `CLOUD`.
+ To create snapshots in the same Local Zone as the source resource, specify `LOCAL_ZONE`.
+ To create snapshots on the same Outpost as the source resource, specify `OUTPOST_LOCAL`.
Default: `CLOUD`
*Required*: No
*Type*: String
*Allowed values*: `CLOUD | OUTPOST_LOCAL | LOCAL_ZONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scripts`  <a name="cfn-dlm-lifecyclepolicy-createrule-scripts"></a>
**[Custom snapshot policies that target instances only]** Specifies pre and/or post scripts for a snapshot lifecycle policy that targets instances. This is useful for creating application-consistent snapshots, or for performing specific administrative tasks before or after Amazon Data Lifecycle Manager initiates snapshot creation.
For more information, see [Automating application-consistent snapshots with pre and post scripts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/automate-app-consistent-backups.html).
*Required*: No
*Type*: Array of [Script](aws-properties-dlm-lifecyclepolicy-script.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Times`  <a name="cfn-dlm-lifecyclepolicy-createrule-times"></a>
The time, in UTC, to start the operation. The supported format is hh:mm.
The operation occurs within a one-hour window following the specified time. If you do not specify a time, Amazon Data Lifecycle Manager selects a time within the next 24 hours.
*Required*: No
*Type*: Array of String
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
