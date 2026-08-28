---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_Criteria.html
---

# Criteria
<a name="API_automation_Criteria"></a>

 A set of conditions that specify which recommended action qualify for implementation. When a rule is active and a recommended action matches these criteria, Compute Optimizer implements the action at the scheduled run time. You can specify up to 20 conditions per filter criteria and 20 values per condition.

## Contents
<a name="API_automation_Criteria_Contents"></a>

 ** ebsVolumeSizeInGib **   <a name="computeoptimizer-Type-automation_Criteria-ebsVolumeSizeInGib"></a>
Filter criteria for EBS volume sizes in gibibytes (GiB).
Type: Array of [IntegerCriteriaCondition](API_automation_IntegerCriteriaCondition.md) objects
Required: No

 ** ebsVolumeType **   <a name="computeoptimizer-Type-automation_Criteria-ebsVolumeType"></a>
Filter criteria for EBS volume types, such as gp2, gp3, io1, io2, st1, or sc1.
Type: Array of [StringCriteriaCondition](API_automation_StringCriteriaCondition.md) objects
Required: No

 ** estimatedMonthlySavings **   <a name="computeoptimizer-Type-automation_Criteria-estimatedMonthlySavings"></a>
Filter criteria for estimated monthly cost savings from the recommended action.
Type: Array of [DoubleCriteriaCondition](API_automation_DoubleCriteriaCondition.md) objects
Required: No

 ** lookBackPeriodInDays **   <a name="computeoptimizer-Type-automation_Criteria-lookBackPeriodInDays"></a>
Filter criteria for the lookback period in days used to analyze resource utilization.
Type: Array of [IntegerCriteriaCondition](API_automation_IntegerCriteriaCondition.md) objects
Required: No

 ** region **   <a name="computeoptimizer-Type-automation_Criteria-region"></a>
Filter criteria for AWS regions where resources must be located.
Type: Array of [StringCriteriaCondition](API_automation_StringCriteriaCondition.md) objects
Required: No

 ** resourceArn **   <a name="computeoptimizer-Type-automation_Criteria-resourceArn"></a>
Filter criteria for specific resource ARNs to include or exclude.
Type: Array of [StringCriteriaCondition](API_automation_StringCriteriaCondition.md) objects
Required: No

 ** resourceTag **   <a name="computeoptimizer-Type-automation_Criteria-resourceTag"></a>
Filter criteria for resource tags, allowing filtering by tag key and value combinations.
Type: Array of [ResourceTagsCriteriaCondition](API_automation_ResourceTagsCriteriaCondition.md) objects
Required: No

 ** restartNeeded **   <a name="computeoptimizer-Type-automation_Criteria-restartNeeded"></a>
Filter criteria indicating whether the recommended action requires a resource restart.
Type: Array of [StringCriteriaCondition](API_automation_StringCriteriaCondition.md) objects
Required: No

## See Also
<a name="API_automation_Criteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/Criteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/Criteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/Criteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
