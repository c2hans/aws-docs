---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DateFilter.html
---

# DateFilter
<a name="API_DateFilter"></a>

A date filter for querying findings.

## Contents
<a name="API_DateFilter_Contents"></a>

 ** DateRange **   <a name="securityhub-Type-DateFilter-DateRange"></a>
A date range for the date filter.
Type: [DateRange](API_DateRange.md) object
Required: No

 ** End **   <a name="securityhub-Type-DateFilter-End"></a>
A timestamp that provides the end date for the date filter.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** Start **   <a name="securityhub-Type-DateFilter-Start"></a>
A timestamp that provides the start date for the date filter.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_DateFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/DateFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/DateFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/DateFilter)
