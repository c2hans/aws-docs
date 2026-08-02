---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ReportFrequency.html
---

# ReportFrequency
<a name="API_ReportFrequency"></a>

Details about how frequently reports are generated.

## Contents
<a name="API_ReportFrequency_Contents"></a>

 ** period **   <a name="licensemanager-Type-ReportFrequency-period"></a>
Time period between each report. The period can be daily, weekly, or monthly.
Type: String
Valid Values: `DAY | WEEK | MONTH | ONE_TIME`
Required: No

 ** value **   <a name="licensemanager-Type-ReportFrequency-value"></a>
Number of times within the frequency period that a report is generated. The only supported value is `1`.
Type: Integer
Required: No

## See Also
<a name="API_ReportFrequency_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/ReportFrequency)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/ReportFrequency)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/ReportFrequency)
