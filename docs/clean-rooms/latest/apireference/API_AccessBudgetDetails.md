---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_AccessBudgetDetails.html
---

# AccessBudgetDetails
<a name="API_AccessBudgetDetails"></a>

Detailed information about an access budget including time bounds, budget allocation, and configuration settings.

## Contents
<a name="API_AccessBudgetDetails_Contents"></a>

 ** budget **   <a name="API-Type-AccessBudgetDetails-budget"></a>
The total budget allocation amount for this access budget.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000000.
Required: Yes

 ** budgetType **   <a name="API-Type-AccessBudgetDetails-budgetType"></a>
Specifies the time period for limiting table usage in queries and jobs. For calendar-based periods, the budget can renew if auto refresh is enabled. For lifetime budgets, the limit applies to the total usage throughout the collaboration. Valid values are:
 `CALENDAR_DAY` - Limit table usage per day.
 `CALENDAR_WEEK` - Limit table usage per week.
 `CALENDAR_MONTH` - Limit table usage per month.
 `LIFETIME` - Limit total table usage for the collaboration duration.
Type: String
Valid Values: `CALENDAR_DAY | CALENDAR_MONTH | CALENDAR_WEEK | LIFETIME`
Required: Yes

 ** remainingBudget **   <a name="API-Type-AccessBudgetDetails-remainingBudget"></a>
The remaining budget amount available for use within this access budget.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** startTime **   <a name="API-Type-AccessBudgetDetails-startTime"></a>
The start time for the access budget period.
Type: Timestamp
Required: Yes

 ** autoRefresh **   <a name="API-Type-AccessBudgetDetails-autoRefresh"></a>
Indicates whether the budget automatically refreshes for each time period specified in `budgetType`. Valid values are:
 `ENABLED` - The budget refreshes automatically at the start of each period.
 `DISABLED` - The budget must be refreshed manually.
 `NULL` - The value is null when `budgetType` is set to `LIFETIME`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** endTime **   <a name="API-Type-AccessBudgetDetails-endTime"></a>
The end time for the access budget period.
Type: Timestamp
Required: No

## See Also
<a name="API_AccessBudgetDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/AccessBudgetDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/AccessBudgetDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/AccessBudgetDetails)
