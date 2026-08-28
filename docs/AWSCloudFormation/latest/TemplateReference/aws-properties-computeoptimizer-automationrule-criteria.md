---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-computeoptimizer-automationrule-criteria.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ComputeOptimizer::AutomationRule Criteria
<a name="aws-properties-computeoptimizer-automationrule-criteria"></a>

 A set of conditions that specify which recommended action qualify for implementation. When a rule is active and a recommended action matches these criteria, Compute Optimizer implements the action at the scheduled run time. You can specify up to 20 conditions per filter criteria and 20 values per condition.

## Syntax
<a name="aws-properties-computeoptimizer-automationrule-criteria-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-computeoptimizer-automationrule-criteria-syntax.json"></a>

```
{
  "[EbsVolumeSizeInGib](#cfn-computeoptimizer-automationrule-criteria-ebsvolumesizeingib)" : {{[ IntegerCriteriaCondition, ... ]}},
  "[EbsVolumeType](#cfn-computeoptimizer-automationrule-criteria-ebsvolumetype)" : {{[ StringCriteriaCondition, ... ]}},
  "[EstimatedMonthlySavings](#cfn-computeoptimizer-automationrule-criteria-estimatedmonthlysavings)" : {{[ DoubleCriteriaCondition, ... ]}},
  "[LookBackPeriodInDays](#cfn-computeoptimizer-automationrule-criteria-lookbackperiodindays)" : {{[ IntegerCriteriaCondition, ... ]}},
  "[Region](#cfn-computeoptimizer-automationrule-criteria-region)" : {{[ StringCriteriaCondition, ... ]}},
  "[ResourceArn](#cfn-computeoptimizer-automationrule-criteria-resourcearn)" : {{[ StringCriteriaCondition, ... ]}},
  "[ResourceTag](#cfn-computeoptimizer-automationrule-criteria-resourcetag)" : {{[ ResourceTagsCriteriaCondition, ... ]}},
  "[RestartNeeded](#cfn-computeoptimizer-automationrule-criteria-restartneeded)" : {{[ StringCriteriaCondition, ... ]}}
}
```

### YAML
<a name="aws-properties-computeoptimizer-automationrule-criteria-syntax.yaml"></a>

```
  [EbsVolumeSizeInGib](#cfn-computeoptimizer-automationrule-criteria-ebsvolumesizeingib): {{
    - IntegerCriteriaCondition}}
  [EbsVolumeType](#cfn-computeoptimizer-automationrule-criteria-ebsvolumetype): {{
    - StringCriteriaCondition}}
  [EstimatedMonthlySavings](#cfn-computeoptimizer-automationrule-criteria-estimatedmonthlysavings): {{
    - DoubleCriteriaCondition}}
  [LookBackPeriodInDays](#cfn-computeoptimizer-automationrule-criteria-lookbackperiodindays): {{
    - IntegerCriteriaCondition}}
  [Region](#cfn-computeoptimizer-automationrule-criteria-region): {{
    - StringCriteriaCondition}}
  [ResourceArn](#cfn-computeoptimizer-automationrule-criteria-resourcearn): {{
    - StringCriteriaCondition}}
  [ResourceTag](#cfn-computeoptimizer-automationrule-criteria-resourcetag): {{
    - ResourceTagsCriteriaCondition}}
  [RestartNeeded](#cfn-computeoptimizer-automationrule-criteria-restartneeded): {{
    - StringCriteriaCondition}}
```

## Properties
<a name="aws-properties-computeoptimizer-automationrule-criteria-properties"></a>

`EbsVolumeSizeInGib`  <a name="cfn-computeoptimizer-automationrule-criteria-ebsvolumesizeingib"></a>
Filter criteria for EBS volume sizes in gibibytes (GiB).
*Required*: No
*Type*: Array of [IntegerCriteriaCondition](aws-properties-computeoptimizer-automationrule-integercriteriacondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EbsVolumeType`  <a name="cfn-computeoptimizer-automationrule-criteria-ebsvolumetype"></a>
Filter criteria for EBS volume types, such as gp2, gp3, io1, io2, st1, or sc1.
*Required*: No
*Type*: Array of [StringCriteriaCondition](aws-properties-computeoptimizer-automationrule-stringcriteriacondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EstimatedMonthlySavings`  <a name="cfn-computeoptimizer-automationrule-criteria-estimatedmonthlysavings"></a>
Filter criteria for estimated monthly cost savings from the recommended action.
*Required*: No
*Type*: Array of [DoubleCriteriaCondition](aws-properties-computeoptimizer-automationrule-doublecriteriacondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LookBackPeriodInDays`  <a name="cfn-computeoptimizer-automationrule-criteria-lookbackperiodindays"></a>
Filter criteria for the lookback period in days used to analyze resource utilization.
*Required*: No
*Type*: Array of [IntegerCriteriaCondition](aws-properties-computeoptimizer-automationrule-integercriteriacondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Region`  <a name="cfn-computeoptimizer-automationrule-criteria-region"></a>
Filter criteria for AWS regions where resources must be located.
*Required*: No
*Type*: Array of [StringCriteriaCondition](aws-properties-computeoptimizer-automationrule-stringcriteriacondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceArn`  <a name="cfn-computeoptimizer-automationrule-criteria-resourcearn"></a>
Filter criteria for specific resource ARNs to include or exclude.
*Required*: No
*Type*: Array of [StringCriteriaCondition](aws-properties-computeoptimizer-automationrule-stringcriteriacondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceTag`  <a name="cfn-computeoptimizer-automationrule-criteria-resourcetag"></a>
Filter criteria for resource tags, allowing filtering by tag key and value combinations.
*Required*: No
*Type*: Array of [ResourceTagsCriteriaCondition](aws-properties-computeoptimizer-automationrule-resourcetagscriteriacondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RestartNeeded`  <a name="cfn-computeoptimizer-automationrule-criteria-restartneeded"></a>
Filter criteria indicating whether the recommended action requires a resource restart.
*Required*: No
*Type*: Array of [StringCriteriaCondition](aws-properties-computeoptimizer-automationrule-stringcriteriacondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
