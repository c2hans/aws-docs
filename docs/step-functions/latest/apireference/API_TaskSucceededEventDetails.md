---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_TaskSucceededEventDetails.html
---

# TaskSucceededEventDetails
<a name="API_TaskSucceededEventDetails"></a>

Contains details about the successful completion of a task state.

## Contents
<a name="API_TaskSucceededEventDetails_Contents"></a>

 ** resource **   <a name="StepFunctions-Type-TaskSucceededEventDetails-resource"></a>
The action of the resource called by a task state.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Required: Yes

 ** resourceType **   <a name="StepFunctions-Type-TaskSucceededEventDetails-resourceType"></a>
The service name of the resource in a task state.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Required: Yes

 ** output **   <a name="StepFunctions-Type-TaskSucceededEventDetails-output"></a>
The full JSON response from a resource when a task has succeeded. This response becomes the output of the related task. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.
Type: String
Length Constraints: Maximum length of 262144.
Required: No

 ** outputDetails **   <a name="StepFunctions-Type-TaskSucceededEventDetails-outputDetails"></a>
Contains details about the output of an execution history event.
Type: [HistoryEventExecutionDataDetails](API_HistoryEventExecutionDataDetails.md) object
Required: No

## See Also
<a name="API_TaskSucceededEventDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/TaskSucceededEventDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/TaskSucceededEventDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/TaskSucceededEventDetails)
