---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dlm-lifecyclepolicy-crossregioncopydeprecaterule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DLM::LifecyclePolicy CrossRegionCopyDeprecateRule
<a name="aws-properties-dlm-lifecyclepolicy-crossregioncopydeprecaterule"></a>

**[Custom AMI policies only]** Specifies an AMI deprecation rule for cross-Region AMI copies created by an AMI policy.

## Syntax
<a name="aws-properties-dlm-lifecyclepolicy-crossregioncopydeprecaterule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dlm-lifecyclepolicy-crossregioncopydeprecaterule-syntax.json"></a>

```
{
  "[Interval](#cfn-dlm-lifecyclepolicy-crossregioncopydeprecaterule-interval)" : {{Integer}},
  "[IntervalUnit](#cfn-dlm-lifecyclepolicy-crossregioncopydeprecaterule-intervalunit)" : {{String}}
}
```

### YAML
<a name="aws-properties-dlm-lifecyclepolicy-crossregioncopydeprecaterule-syntax.yaml"></a>

```
  [Interval](#cfn-dlm-lifecyclepolicy-crossregioncopydeprecaterule-interval): {{Integer}}
  [IntervalUnit](#cfn-dlm-lifecyclepolicy-crossregioncopydeprecaterule-intervalunit): {{String}}
```

## Properties
<a name="aws-properties-dlm-lifecyclepolicy-crossregioncopydeprecaterule-properties"></a>

`Interval`  <a name="cfn-dlm-lifecyclepolicy-crossregioncopydeprecaterule-interval"></a>
The period after which to deprecate the cross-Region AMI copies. The period must be less than or equal to the cross-Region AMI copy retention period, and it can't be greater than 10 years. This is equivalent to 120 months, 520 weeks, or 3650 days.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IntervalUnit`  <a name="cfn-dlm-lifecyclepolicy-crossregioncopydeprecaterule-intervalunit"></a>
The unit of time in which to measure the **Interval**. For example, to deprecate a cross-Region AMI copy after 3 months, specify `Interval=3` and `IntervalUnit=MONTHS`.
*Required*: Yes
*Type*: String
*Allowed values*: `DAYS | WEEKS | MONTHS | YEARS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
