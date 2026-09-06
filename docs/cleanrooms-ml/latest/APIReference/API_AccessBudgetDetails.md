---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_AccessBudgetDetails.html
---

# AccessBudgetDetails
<a name="API_AccessBudgetDetails"></a>

The detailed information for a specific budget period, including time boundaries and budget amounts.

## Contents
<a name="API_AccessBudgetDetails_Contents"></a>

 ** budget **   <a name="API-Type-AccessBudgetDetails-budget"></a>
The total budget amount allocated for this period.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** budgetType **   <a name="API-Type-AccessBudgetDetails-budgetType"></a>
The type of budget period. Calendar-based types reset automatically at regular intervals, while LIFETIME budgets never reset.
Type: String
Valid Values: `CALENDAR_DAY | CALENDAR_MONTH | CALENDAR_WEEK | LIFETIME`
Required: Yes

 ** remainingBudget **   <a name="API-Type-AccessBudgetDetails-remainingBudget"></a>
The amount of budget remaining in this period.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** startTime **   <a name="API-Type-AccessBudgetDetails-startTime"></a>
The start time of this budget period.
Type: Timestamp
Required: Yes

 ** autoRefresh **   <a name="API-Type-AccessBudgetDetails-autoRefresh"></a>
Specifies whether this budget automatically refreshes when the current period ends.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** endTime **   <a name="API-Type-AccessBudgetDetails-endTime"></a>
The end time of this budget period. If not specified, the budget period continues indefinitely.
Type: Timestamp
Required: No

## See Also
<a name="API_AccessBudgetDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/AccessBudgetDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/AccessBudgetDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/AccessBudgetDetails)
