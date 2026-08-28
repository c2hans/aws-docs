---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_BillingAndCostManagementRecommendedActions_RecommendedAction.html
---

# RecommendedAction
<a name="API_BillingAndCostManagementRecommendedActions_RecommendedAction"></a>

Describes a specific recommended action.

## Contents
<a name="API_BillingAndCostManagementRecommendedActions_RecommendedAction_Contents"></a>

 ** accountId **   <a name="awscostmanagement-Type-BillingAndCostManagementRecommendedActions_RecommendedAction-accountId"></a>
The account that the recommended action is for.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** context **   <a name="awscostmanagement-Type-BillingAndCostManagementRecommendedActions_RecommendedAction-context"></a>
Context that applies to the recommended action.
Type: String to string map
Required: No

 ** feature **   <a name="awscostmanagement-Type-BillingAndCostManagementRecommendedActions_RecommendedAction-feature"></a>
The feature associated with the recommended action.
Type: String
Valid Values: `ACCOUNT | BUDGETS | COST_ANOMALY_DETECTION | COST_OPTIMIZATION_HUB | FREE_TIER | IAM | PAYMENTS | RESERVATIONS | SAVINGS_PLANS | TAX_SETTINGS`
Required: No

 ** id **   <a name="awscostmanagement-Type-BillingAndCostManagementRecommendedActions_RecommendedAction-id"></a>
The ID for the recommended action.
Type: String
Required: No

 ** lastUpdatedTimeStamp **   <a name="awscostmanagement-Type-BillingAndCostManagementRecommendedActions_RecommendedAction-lastUpdatedTimeStamp"></a>
The time when the recommended action status was last updated.
Type: String
Required: No

 ** nextSteps **   <a name="awscostmanagement-Type-BillingAndCostManagementRecommendedActions_RecommendedAction-nextSteps"></a>
The possible next steps to execute the recommended action.
Type: Array of strings
Required: No

 ** severity **   <a name="awscostmanagement-Type-BillingAndCostManagementRecommendedActions_RecommendedAction-severity"></a>
The severity associated with the recommended action.
Type: String
Valid Values: `INFO | WARNING | CRITICAL`
Required: No

 ** type **   <a name="awscostmanagement-Type-BillingAndCostManagementRecommendedActions_RecommendedAction-type"></a>
The type of action you can take by adopting the recommended action.
Type: String
Valid Values: `ADD_ALTERNATE_BILLING_CONTACT | CREATE_ANOMALY_MONITOR | CREATE_BUDGET | ENABLE_COST_OPTIMIZATION_HUB | MIGRATE_TO_GRANULAR_PERMISSIONS | PAYMENTS_DUE | PAYMENTS_PAST_DUE | REVIEW_ANOMALIES | REVIEW_BUDGET_ALERTS | REVIEW_BUDGETS_EXCEEDED | REVIEW_EXPIRING_RI | REVIEW_EXPIRING_SP | REVIEW_FREETIER_USAGE_ALERTS | REVIEW_FREETIER_CREDITS_REMAINING | REVIEW_FREETIER_DAYS_REMAINING | REVIEW_SAVINGS_OPPORTUNITY_RECOMMENDATIONS | UPDATE_EXPIRED_PAYMENT_METHOD | UPDATE_INVALID_PAYMENT_METHOD | UPDATE_TAX_EXEMPTION_CERTIFICATE | UPDATE_TAX_REGISTRATION_NUMBER`
Required: No

## See Also
<a name="API_BillingAndCostManagementRecommendedActions_RecommendedAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-recommended-actions-2024-11-14/RecommendedAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-recommended-actions-2024-11-14/RecommendedAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-recommended-actions-2024-11-14/RecommendedAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
