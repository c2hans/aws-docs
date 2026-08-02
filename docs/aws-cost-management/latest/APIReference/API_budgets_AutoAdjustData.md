---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_AutoAdjustData.html
---

# AutoAdjustData
<a name="API_budgets_AutoAdjustData"></a>

The parameters that determine the budget amount for an auto-adjusting budget.

## Contents
<a name="API_budgets_AutoAdjustData_Contents"></a>

 ** AutoAdjustType **   <a name="awscostmanagement-Type-budgets_AutoAdjustData-AutoAdjustType"></a>
The string that defines whether your budget auto-adjusts based on historical or forecasted data.
Type: String
Valid Values: `HISTORICAL | FORECAST`
Required: Yes

 ** HistoricalOptions **   <a name="awscostmanagement-Type-budgets_AutoAdjustData-HistoricalOptions"></a>
The parameters that define or describe the historical data that your auto-adjusting budget is based on.
Type: [HistoricalOptions](API_budgets_HistoricalOptions.md) object
Required: No

 ** LastAutoAdjustTime **   <a name="awscostmanagement-Type-budgets_AutoAdjustData-LastAutoAdjustTime"></a>
The last time that your budget was auto-adjusted.
Type: Timestamp
Required: No

## See Also
<a name="API_budgets_AutoAdjustData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/AutoAdjustData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/AutoAdjustData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/AutoAdjustData)
