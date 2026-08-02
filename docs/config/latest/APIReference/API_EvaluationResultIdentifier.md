---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_EvaluationResultIdentifier.html
---

# EvaluationResultIdentifier
<a name="API_EvaluationResultIdentifier"></a>

Uniquely identifies an evaluation result.

## Contents
<a name="API_EvaluationResultIdentifier_Contents"></a>

 ** EvaluationResultQualifier **   <a name="config-Type-EvaluationResultIdentifier-EvaluationResultQualifier"></a>
Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and ID of the evaluated resource.
Type: [EvaluationResultQualifier](API_EvaluationResultQualifier.md) object
Required: No

 ** OrderingTimestamp **   <a name="config-Type-EvaluationResultIdentifier-OrderingTimestamp"></a>
The time of the event that triggered the evaluation of your AWS resources. The time can indicate when AWS Config delivered a configuration item change notification, or it can indicate when AWS Config delivered the configuration snapshot, depending on which event triggered the evaluation.
Type: Timestamp
Required: No

 ** ResourceEvaluationId **   <a name="config-Type-EvaluationResultIdentifier-ResourceEvaluationId"></a>
A Unique ID for an evaluation result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_EvaluationResultIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/EvaluationResultIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/EvaluationResultIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/EvaluationResultIdentifier)
