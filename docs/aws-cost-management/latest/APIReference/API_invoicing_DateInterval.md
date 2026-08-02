---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_DateInterval.html
---

# DateInterval
<a name="API_invoicing_DateInterval"></a>

 The time period that you want invoice-related documents for.

## Contents
<a name="API_invoicing_DateInterval_Contents"></a>

 ** EndDate **   <a name="awscostmanagement-Type-invoicing_DateInterval-EndDate"></a>
 The end of the time period that you want invoice-related documents for. The end date is exclusive. For example, if `end` is `2019-01-10`, AWS retrieves invoice-related documents from the start date up to, but not including, `2018-01-10`.
Type: Timestamp
Required: Yes

 ** StartDate **   <a name="awscostmanagement-Type-invoicing_DateInterval-StartDate"></a>
 The beginning of the time period that you want invoice-related documents for. The start date is inclusive. For example, if `start` is `2019-01-01`, AWS retrieves invoices starting at `2019-01-01` up to the end date.
Type: Timestamp
Required: Yes

## See Also
<a name="API_invoicing_DateInterval_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/DateInterval)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/DateInterval)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/DateInterval)
