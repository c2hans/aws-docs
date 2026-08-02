---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_EvaluationStatus.html
---

# EvaluationStatus
<a name="API_EvaluationStatus"></a>

Returns status details of an evaluation.

## Contents
<a name="API_EvaluationStatus_Contents"></a>

 ** Status **   <a name="config-Type-EvaluationStatus-Status"></a>
The status of an execution. The valid values are In\_Progress, Succeeded or Failed.
Type: String
Valid Values: `IN_PROGRESS | FAILED | SUCCEEDED`
Required: Yes

 ** FailureReason **   <a name="config-Type-EvaluationStatus-FailureReason"></a>
An explanation for failed execution status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_EvaluationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/EvaluationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/EvaluationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/EvaluationStatus)
