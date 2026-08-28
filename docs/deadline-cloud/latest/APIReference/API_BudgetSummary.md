---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_BudgetSummary.html
---

# BudgetSummary
<a name="API_BudgetSummary"></a>

The budget summary.

## Contents
<a name="API_BudgetSummary_Contents"></a>

 ** approximateDollarLimit **   <a name="deadlinecloud-Type-BudgetSummary-approximateDollarLimit"></a>
The approximate dollar limit of the budget.
Type: Float
Valid Range: Minimum value of 0.01.
Required: Yes

 ** budgetId **   <a name="deadlinecloud-Type-BudgetSummary-budgetId"></a>
The budget ID.
Type: String
Pattern: `budget-[0-9a-f]{32}`
Required: Yes

 ** createdAt **   <a name="deadlinecloud-Type-BudgetSummary-createdAt"></a>
The date and time the resource was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="deadlinecloud-Type-BudgetSummary-createdBy"></a>
The user or system that created this resource.
Type: String
Required: Yes

 ** displayName **   <a name="deadlinecloud-Type-BudgetSummary-displayName"></a>
The display name of the budget summary to update.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** status **   <a name="deadlinecloud-Type-BudgetSummary-status"></a>
The status of the budget.
+  `ACTIVE`–The budget is being evaluated.
+  `INACTIVE`–The budget is inactive. This can include Expired, Canceled, or deleted Deleted statuses.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: Yes

 ** usages **   <a name="deadlinecloud-Type-BudgetSummary-usages"></a>
The consumed usage for the budget.
Type: [ConsumedUsages](API_ConsumedUsages.md) object
Required: Yes

 ** usageTrackingResource **   <a name="deadlinecloud-Type-BudgetSummary-usageTrackingResource"></a>
The resource used to track expenditure in the budget.
Type: [UsageTrackingResource](API_UsageTrackingResource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** description **   <a name="deadlinecloud-Type-BudgetSummary-description"></a>
 *This member has been deprecated.*
The description of the budget summary.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: No

 ** updatedAt **   <a name="deadlinecloud-Type-BudgetSummary-updatedAt"></a>
The date and time the resource was updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="deadlinecloud-Type-BudgetSummary-updatedBy"></a>
The user or system that updated this resource.
Type: String
Required: No

## See Also
<a name="API_BudgetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/BudgetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/BudgetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/BudgetSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
