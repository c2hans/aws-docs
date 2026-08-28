---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dlm-lifecyclepolicy-retainrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DLM::LifecyclePolicy RetainRule
<a name="aws-properties-dlm-lifecyclepolicy-retainrule"></a>

**[Custom snapshot and AMI policies only]** Specifies a retention rule for snapshots created by snapshot policies, or for AMIs created by AMI policies.

**Note**
For snapshot policies that have an [ArchiveRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_ArchiveRule.html), this retention rule applies to standard tier retention. When the retention threshold is met, snapshots are moved from the standard to the archive tier.
For snapshot policies that do not have an **ArchiveRule**, snapshots are permanently deleted when this retention threshold is met.

You can retain snapshots based on either a count or a time interval.
+  **Count-based retention**

  You must specify **Count**. If you specify an [ArchiveRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_ArchiveRule.html) for the schedule, then you can specify a retention count of `0` to archive snapshots immediately after creation. If you specify a [FastRestoreRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_FastRestoreRule.html), [ShareRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_ShareRule.html), or a [CrossRegionCopyRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_CrossRegionCopyRule.html), then you must specify a retention count of `1` or more.
+  **Age-based retention**

  You must specify **Interval** and **IntervalUnit**. If you specify an [ArchiveRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_ArchiveRule.html) for the schedule, then you can specify a retention interval of `0` days to archive snapshots immediately after creation. If you specify a [FastRestoreRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_FastRestoreRule.html), [ShareRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_ShareRule.html), or a [CrossRegionCopyRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_CrossRegionCopyRule.html), then you must specify a retention interval of `1` day or more.

## Syntax
<a name="aws-properties-dlm-lifecyclepolicy-retainrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dlm-lifecyclepolicy-retainrule-syntax.json"></a>

```
{
  "[Count](#cfn-dlm-lifecyclepolicy-retainrule-count)" : {{Integer}},
  "[Interval](#cfn-dlm-lifecyclepolicy-retainrule-interval)" : {{Integer}},
  "[IntervalUnit](#cfn-dlm-lifecyclepolicy-retainrule-intervalunit)" : {{String}}
}
```

### YAML
<a name="aws-properties-dlm-lifecyclepolicy-retainrule-syntax.yaml"></a>

```
  [Count](#cfn-dlm-lifecyclepolicy-retainrule-count): {{Integer}}
  [Interval](#cfn-dlm-lifecyclepolicy-retainrule-interval): {{Integer}}
  [IntervalUnit](#cfn-dlm-lifecyclepolicy-retainrule-intervalunit): {{String}}
```

## Properties
<a name="aws-properties-dlm-lifecyclepolicy-retainrule-properties"></a>

`Count`  <a name="cfn-dlm-lifecyclepolicy-retainrule-count"></a>
The number of snapshots to retain for each volume, up to a maximum of 1000. For example if you want to retain a maximum of three snapshots, specify `3`. When the fourth snapshot is created, the oldest retained snapshot is deleted, or it is moved to the archive tier if you have specified an [ArchiveRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_ArchiveRule.html).
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interval`  <a name="cfn-dlm-lifecyclepolicy-retainrule-interval"></a>
The amount of time to retain each snapshot. The maximum is 100 years. This is equivalent to 1200 months, 5200 weeks, or 36500 days.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IntervalUnit`  <a name="cfn-dlm-lifecyclepolicy-retainrule-intervalunit"></a>
The unit of time for time-based retention. For example, to retain snapshots for 3 months, specify `Interval=3` and `IntervalUnit=MONTHS`. Once the snapshot has been retained for 3 months, it is deleted, or it is moved to the archive tier if you have specified an [ArchiveRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_ArchiveRule.html).
*Required*: No
*Type*: String
*Allowed values*: `DAYS | WEEKS | MONTHS | YEARS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
