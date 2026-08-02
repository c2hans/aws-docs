---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_EvaluationFailedEventDetails.html
---

# EvaluationFailedEventDetails
<a name="API_EvaluationFailedEventDetails"></a>

Contains details about an evaluation failure that occurred while processing a state, for example, when a JSONata expression throws an error. This event will only be present in state machines that have ** QueryLanguage** set to JSONata, or individual states set to JSONata.

## Contents
<a name="API_EvaluationFailedEventDetails_Contents"></a>

 ** state **   <a name="StepFunctions-Type-EvaluationFailedEventDetails-state"></a>
The name of the state in which the evaluation error occurred.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Required: Yes

 ** cause **   <a name="StepFunctions-Type-EvaluationFailedEventDetails-cause"></a>
A more detailed explanation of the cause of the failure.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32768.
Required: No

 ** error **   <a name="StepFunctions-Type-EvaluationFailedEventDetails-error"></a>
The error code of the failure.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** location **   <a name="StepFunctions-Type-EvaluationFailedEventDetails-location"></a>
The location of the field in the state in which the evaluation error occurred.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_EvaluationFailedEventDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/EvaluationFailedEventDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/EvaluationFailedEventDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/EvaluationFailedEventDetails)
