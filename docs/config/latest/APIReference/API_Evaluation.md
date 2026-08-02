---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_Evaluation.html
---

# Evaluation
<a name="API_Evaluation"></a>

Identifies an AWS resource and indicates whether it complies with the AWS Config rule that it was evaluated against.

## Contents
<a name="API_Evaluation_Contents"></a>

 ** ComplianceResourceId **   <a name="config-Type-Evaluation-ComplianceResourceId"></a>
The ID of the AWS resource that was evaluated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 768.
Required: Yes

 ** ComplianceResourceType **   <a name="config-Type-Evaluation-ComplianceResourceType"></a>
The type of AWS resource that was evaluated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** ComplianceType **   <a name="config-Type-Evaluation-ComplianceType"></a>
Indicates whether the AWS resource complies with the AWS Config rule that it was evaluated against.
For the `Evaluation` data type, AWS Config supports only the `COMPLIANT`, `NON_COMPLIANT`, and `NOT_APPLICABLE` values. AWS Config does not support the `INSUFFICIENT_DATA` value for this data type.
Similarly, AWS Config does not accept `INSUFFICIENT_DATA` as the value for `ComplianceType` from a `PutEvaluations` request. For example, an AWS Lambda function for a custom AWS Config rule cannot pass an `INSUFFICIENT_DATA` value to AWS Config.
Type: String
Valid Values: `COMPLIANT | NON_COMPLIANT | NOT_APPLICABLE | INSUFFICIENT_DATA`
Required: Yes

 ** OrderingTimestamp **   <a name="config-Type-Evaluation-OrderingTimestamp"></a>
The time of the event in AWS Config that triggered the evaluation. For event-based evaluations, the time indicates when AWS Config created the configuration item that triggered the evaluation. For periodic evaluations, the time indicates when AWS Config triggered the evaluation at the frequency that you specified (for example, every 24 hours).
Type: Timestamp
Required: Yes

 ** Annotation **   <a name="config-Type-Evaluation-Annotation"></a>
Supplementary information about how the evaluation determined the compliance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_Evaluation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/Evaluation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/Evaluation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/Evaluation)
