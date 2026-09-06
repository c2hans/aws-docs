---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ConformancePackEvaluationFilters.html
---

# ConformancePackEvaluationFilters
<a name="API_ConformancePackEvaluationFilters"></a>

Filters a conformance pack by AWS Config rule names, compliance types, AWS resource types, and resource IDs.

## Contents
<a name="API_ConformancePackEvaluationFilters_Contents"></a>

 ** ComplianceType **   <a name="config-Type-ConformancePackEvaluationFilters-ComplianceType"></a>
Filters the results by compliance.
The allowed values are `COMPLIANT` and `NON_COMPLIANT`. `INSUFFICIENT_DATA` is not supported.
Type: String
Valid Values: `COMPLIANT | NON_COMPLIANT | INSUFFICIENT_DATA`
Required: No

 ** ConfigRuleNames **   <a name="config-Type-ConformancePackEvaluationFilters-ConfigRuleNames"></a>
Filters the results by AWS Config rule names.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** ResourceIds **   <a name="config-Type-ConformancePackEvaluationFilters-ResourceIds"></a>
Filters the results by resource IDs.
This is valid only when you provide resource type. If there is no resource type, you will see an error.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** ResourceType **   <a name="config-Type-ConformancePackEvaluationFilters-ResourceType"></a>
Filters the results by the resource type (for example, `"AWS::EC2::Instance"`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_ConformancePackEvaluationFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ConformancePackEvaluationFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ConformancePackEvaluationFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ConformancePackEvaluationFilters)
