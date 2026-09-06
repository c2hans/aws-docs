---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_TimePeriod.html
---

# TimePeriod
<a name="API_budgets_TimePeriod"></a>

The period of time that's covered by a budget. The period has a start date and an end date. The start date must come before the end date. There are no restrictions on the end date.

## Contents
<a name="API_budgets_TimePeriod_Contents"></a>

 ** End **   <a name="awscostmanagement-Type-budgets_TimePeriod-End"></a>
The end date for a budget. If you didn't specify an end date, AWS set your end date to `06/15/87 00:00 UTC`. The defaults are the same for the AWS Billing and Cost Management console and the API.
After the end date, AWS deletes the budget and all the associated notifications and subscribers. You can change your end date with the `UpdateBudget` operation.
Type: Timestamp
Required: No

 ** Start **   <a name="awscostmanagement-Type-budgets_TimePeriod-Start"></a>
The start date for a budget. If you created your budget and didn't specify a start date, AWS defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, ANNUALLY, or CUSTOM). For example, if you created your budget on January 24, 2018, chose `DAILY`, and didn't set a start date, AWS set your start date to `01/24/18 00:00 UTC`. If you chose `MONTHLY`, AWS set your start date to `01/01/18 00:00 UTC`. The defaults are the same for the AWS Billing and Cost Management console and the API.
You can change your start date with the `UpdateBudget` operation.
Type: Timestamp
Required: No

## See Also
<a name="API_budgets_TimePeriod_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/TimePeriod)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/TimePeriod)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/TimePeriod)
