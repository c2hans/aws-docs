---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_MetricSource.html
---

# MetricSource
<a name="API_MetricSource"></a>

Identifies the metric source for SLOs on resources other than Application Signals services.

## Contents
<a name="API_MetricSource_Contents"></a>

 ** MetricSourceKeyAttributes **   <a name="applicationsignals-Type-MetricSource-MetricSourceKeyAttributes"></a>
Key attributes that identify the metric source.
Type: String to string map
Map Entries: Maximum number of 4 items.
Key Pattern: `[a-zA-Z]{1,50}`
Value Length Constraints: Minimum length of 1. Maximum length of 1024.
Value Pattern: `[ -~]*[!-~]+[ -~]*`
Required: Yes

 ** MetricSourceAttributes **   <a name="applicationsignals-Type-MetricSource-MetricSourceAttributes"></a>
Additional attributes for the metric source.
Type: String to string map
Map Entries: Maximum number of 4 items.
Key Pattern: `[a-zA-Z]{1,50}`
Value Length Constraints: Minimum length of 1. Maximum length of 1024.
Value Pattern: `[ -~]*[!-~]+[ -~]*`
Required: No

## See Also
<a name="API_MetricSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/MetricSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/MetricSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/MetricSource)
