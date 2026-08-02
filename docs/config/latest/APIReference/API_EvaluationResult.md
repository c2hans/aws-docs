---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_EvaluationResult.html
---

# EvaluationResult
<a name="API_EvaluationResult"></a>

The details of an AWS Config evaluation. Provides the AWS resource that was evaluated, the compliance of the resource, related time stamps, and supplementary information.

## Contents
<a name="API_EvaluationResult_Contents"></a>

 ** Annotation **   <a name="config-Type-EvaluationResult-Annotation"></a>
Supplementary information about how the evaluation determined the compliance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** ComplianceType **   <a name="config-Type-EvaluationResult-ComplianceType"></a>
Indicates whether the AWS resource complies with the AWS Config rule that evaluated it.
For the `EvaluationResult` data type, AWS Config supports only the `COMPLIANT`, `NON_COMPLIANT`, and `NOT_APPLICABLE` values. AWS Config does not support the `INSUFFICIENT_DATA` value for the `EvaluationResult` data type.
Type: String
Valid Values: `COMPLIANT | NON_COMPLIANT | NOT_APPLICABLE | INSUFFICIENT_DATA`
Required: No

 ** ConfigRuleInvokedTime **   <a name="config-Type-EvaluationResult-ConfigRuleInvokedTime"></a>
The time when the AWS Config rule evaluated the AWS resource.
Type: Timestamp
Required: No

 ** EvaluationResultIdentifier **   <a name="config-Type-EvaluationResult-EvaluationResultIdentifier"></a>
Uniquely identifies the evaluation result.
Type: [EvaluationResultIdentifier](API_EvaluationResultIdentifier.md) object
Required: No

 ** ResultRecordedTime **   <a name="config-Type-EvaluationResult-ResultRecordedTime"></a>
The time when AWS Config recorded the evaluation result.
Type: Timestamp
Required: No

 ** ResultToken **   <a name="config-Type-EvaluationResult-ResultToken"></a>
An encrypted token that associates an evaluation with an AWS Config rule. The token identifies the rule, the AWS resource being evaluated, and the event that triggered the evaluation.
Type: String
Required: No

## See Also
<a name="API_EvaluationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/EvaluationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/EvaluationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/EvaluationResult)
