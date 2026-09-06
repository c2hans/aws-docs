---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DateRange.html
---

# DateRange
<a name="API_DateRange"></a>

A date range for the date filter.

## Contents
<a name="API_DateRange_Contents"></a>

 ** Comparison **   <a name="securityhub-Type-DateRange-Comparison"></a>
The condition to apply to a date range filter. If you specify `WITHIN`, Security Hub filters for dates within the specified date range. If you specify `OLDER_THAN`, Security Hub filters for dates before the specified date range. If you don't specify a value, the default is `WITHIN`.
Type: String
Valid Values: `WITHIN | OLDER_THAN`
Required: No

 ** Unit **   <a name="securityhub-Type-DateRange-Unit"></a>
A date range unit for the date filter.
Type: String
Valid Values: `DAYS`
Required: No

 ** Value **   <a name="securityhub-Type-DateRange-Value"></a>
A date range value for the date filter.
Type: Integer
Required: No

## See Also
<a name="API_DateRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/DateRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/DateRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/DateRange)
