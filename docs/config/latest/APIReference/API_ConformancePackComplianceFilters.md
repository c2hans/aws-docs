---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ConformancePackComplianceFilters.html
---

# ConformancePackComplianceFilters
<a name="API_ConformancePackComplianceFilters"></a>

Filters the conformance pack by compliance types and AWS Config rule names.

## Contents
<a name="API_ConformancePackComplianceFilters_Contents"></a>

 ** ComplianceType **   <a name="config-Type-ConformancePackComplianceFilters-ComplianceType"></a>
Filters the results by compliance.
The allowed values are `COMPLIANT` and `NON_COMPLIANT`. `INSUFFICIENT_DATA` is not supported.
Type: String
Valid Values: `COMPLIANT | NON_COMPLIANT | INSUFFICIENT_DATA`
Required: No

 ** ConfigRuleNames **   <a name="config-Type-ConformancePackComplianceFilters-ConfigRuleNames"></a>
Filters the results by AWS Config rule names.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_ConformancePackComplianceFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ConformancePackComplianceFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ConformancePackComplianceFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ConformancePackComplianceFilters)
