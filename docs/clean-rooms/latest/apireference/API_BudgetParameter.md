---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_BudgetParameter.html
---

# BudgetParameter
<a name="API_BudgetParameter"></a>

Individual budget parameter configuration that defines specific budget allocation settings for access budgets.

## Contents
<a name="API_BudgetParameter_Contents"></a>

 ** budget **   <a name="API-Type-BudgetParameter-budget"></a>
The budget allocation amount for this specific parameter.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000000.
Required: Yes

 ** type **   <a name="API-Type-BudgetParameter-type"></a>
The type of budget parameter being configured.
Type: String
Valid Values: `CALENDAR_DAY | CALENDAR_MONTH | CALENDAR_WEEK | LIFETIME`
Required: Yes

 ** autoRefresh **   <a name="API-Type-BudgetParameter-autoRefresh"></a>
Whether this individual budget parameter automatically refreshes when the budget period resets.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_BudgetParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/BudgetParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/BudgetParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/BudgetParameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
