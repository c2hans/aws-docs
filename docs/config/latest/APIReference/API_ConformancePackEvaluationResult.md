---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ConformancePackEvaluationResult.html
---

# ConformancePackEvaluationResult
<a name="API_ConformancePackEvaluationResult"></a>

The details of a conformance pack evaluation. Provides AWS Config rule and AWS resource type that was evaluated, the compliance of the conformance pack, related time stamps, and supplementary information.

## Contents
<a name="API_ConformancePackEvaluationResult_Contents"></a>

 ** ComplianceType **   <a name="config-Type-ConformancePackEvaluationResult-ComplianceType"></a>
The compliance type. The allowed values are `COMPLIANT` and `NON_COMPLIANT`. `INSUFFICIENT_DATA` is not supported.
Type: String
Valid Values: `COMPLIANT | NON_COMPLIANT | INSUFFICIENT_DATA`
Required: Yes

 ** ConfigRuleInvokedTime **   <a name="config-Type-ConformancePackEvaluationResult-ConfigRuleInvokedTime"></a>
The time when AWS Config rule evaluated AWS resource.
Type: Timestamp
Required: Yes

 ** EvaluationResultIdentifier **   <a name="config-Type-ConformancePackEvaluationResult-EvaluationResultIdentifier"></a>
Uniquely identifies an evaluation result.
Type: [EvaluationResultIdentifier](API_EvaluationResultIdentifier.md) object
Required: Yes

 ** ResultRecordedTime **   <a name="config-Type-ConformancePackEvaluationResult-ResultRecordedTime"></a>
The time when AWS Config recorded the evaluation result.
Type: Timestamp
Required: Yes

 ** Annotation **   <a name="config-Type-ConformancePackEvaluationResult-Annotation"></a>
Supplementary information about how the evaluation determined the compliance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_ConformancePackEvaluationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ConformancePackEvaluationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ConformancePackEvaluationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ConformancePackEvaluationResult)
