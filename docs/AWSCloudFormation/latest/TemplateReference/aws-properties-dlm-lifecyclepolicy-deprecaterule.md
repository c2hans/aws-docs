---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dlm-lifecyclepolicy-deprecaterule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DLM::LifecyclePolicy DeprecateRule
<a name="aws-properties-dlm-lifecyclepolicy-deprecaterule"></a>

**[Custom AMI policies only]** Specifies an AMI deprecation rule for AMIs created by an AMI lifecycle policy.

For age-based schedules, you must specify **Interval** and **IntervalUnit**. For count-based schedules, you must specify **Count**.

## Syntax
<a name="aws-properties-dlm-lifecyclepolicy-deprecaterule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dlm-lifecyclepolicy-deprecaterule-syntax.json"></a>

```
{
  "[Count](#cfn-dlm-lifecyclepolicy-deprecaterule-count)" : {{Integer}},
  "[Interval](#cfn-dlm-lifecyclepolicy-deprecaterule-interval)" : {{Integer}},
  "[IntervalUnit](#cfn-dlm-lifecyclepolicy-deprecaterule-intervalunit)" : {{String}}
}
```

### YAML
<a name="aws-properties-dlm-lifecyclepolicy-deprecaterule-syntax.yaml"></a>

```
  [Count](#cfn-dlm-lifecyclepolicy-deprecaterule-count): {{Integer}}
  [Interval](#cfn-dlm-lifecyclepolicy-deprecaterule-interval): {{Integer}}
  [IntervalUnit](#cfn-dlm-lifecyclepolicy-deprecaterule-intervalunit): {{String}}
```

## Properties
<a name="aws-properties-dlm-lifecyclepolicy-deprecaterule-properties"></a>

`Count`  <a name="cfn-dlm-lifecyclepolicy-deprecaterule-count"></a>
If the schedule has a count-based retention rule, this parameter specifies the number of oldest AMIs to deprecate. The count must be less than or equal to the schedule's retention count, and it can't be greater than 1000.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interval`  <a name="cfn-dlm-lifecyclepolicy-deprecaterule-interval"></a>
If the schedule has an age-based retention rule, this parameter specifies the period after which to deprecate AMIs created by the schedule. The period must be less than or equal to the schedule's retention period, and it can't be greater than 10 years. This is equivalent to 120 months, 520 weeks, or 3650 days.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IntervalUnit`  <a name="cfn-dlm-lifecyclepolicy-deprecaterule-intervalunit"></a>
The unit of time in which to measure the **Interval**.
*Required*: No
*Type*: String
*Allowed values*: `DAYS | WEEKS | MONTHS | YEARS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
