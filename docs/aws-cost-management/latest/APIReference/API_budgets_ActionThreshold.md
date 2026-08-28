---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_ActionThreshold.html
---

# ActionThreshold
<a name="API_budgets_ActionThreshold"></a>

The trigger threshold of the action.

## Contents
<a name="API_budgets_ActionThreshold_Contents"></a>

 ** ActionThresholdType **   <a name="awscostmanagement-Type-budgets_ActionThreshold-ActionThresholdType"></a>
 The type of threshold for a notification.
Type: String
Valid Values: `PERCENTAGE | ABSOLUTE_VALUE`
Required: Yes

 ** ActionThresholdValue **   <a name="awscostmanagement-Type-budgets_ActionThreshold-ActionThresholdValue"></a>
 The threshold of a notification.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 15000000000000.
Required: Yes

## See Also
<a name="API_budgets_ActionThreshold_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/ActionThreshold)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/ActionThreshold)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/ActionThreshold)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
