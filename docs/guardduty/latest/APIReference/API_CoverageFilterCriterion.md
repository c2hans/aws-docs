---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CoverageFilterCriterion.html
---

# CoverageFilterCriterion
<a name="API_CoverageFilterCriterion"></a>

Represents a condition that when matched will be added to the response of the operation.

## Contents
<a name="API_CoverageFilterCriterion_Contents"></a>

 ** criterionKey **   <a name="guardduty-Type-CoverageFilterCriterion-criterionKey"></a>
An enum value representing possible filter fields.
Replace the enum value `CLUSTER_NAME` with `EKS_CLUSTER_NAME`. `CLUSTER_NAME` has been deprecated.
Type: String
Valid Values: `ACCOUNT_ID | RESOURCE_TYPE | COVERAGE_STATUS | ADDON_VERSION | CLUSTER_NAME | ECS_CLUSTER_NAME | MANAGEMENT_TYPE | EKS_CLUSTER_NAME | AGENT_VERSION | INSTANCE_ID | CLUSTER_ARN`
Required: No

 ** filterCondition **   <a name="guardduty-Type-CoverageFilterCriterion-filterCondition"></a>
Contains information about the condition.
Type: [CoverageFilterCondition](API_CoverageFilterCondition.md) object
Required: No

## See Also
<a name="API_CoverageFilterCriterion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/CoverageFilterCriterion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/CoverageFilterCriterion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/CoverageFilterCriterion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
