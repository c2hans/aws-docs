---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_StateEnteredEventDetails.html
---

# StateEnteredEventDetails
<a name="API_StateEnteredEventDetails"></a>

Contains details about a state entered during an execution.

## Contents
<a name="API_StateEnteredEventDetails_Contents"></a>

 ** name **   <a name="StepFunctions-Type-StateEnteredEventDetails-name"></a>
The name of the state.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Required: Yes

 ** input **   <a name="StepFunctions-Type-StateEnteredEventDetails-input"></a>
The string that contains the JSON input data for the state. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.
Type: String
Length Constraints: Maximum length of 262144.
Required: No

 ** inputDetails **   <a name="StepFunctions-Type-StateEnteredEventDetails-inputDetails"></a>
Contains details about the input for an execution history event.
Type: [HistoryEventExecutionDataDetails](API_HistoryEventExecutionDataDetails.md) object
Required: No

## See Also
<a name="API_StateEnteredEventDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/StateEnteredEventDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/StateEnteredEventDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/StateEnteredEventDetails)
