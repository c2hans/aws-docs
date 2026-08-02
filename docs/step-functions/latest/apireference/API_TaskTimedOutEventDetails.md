---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_TaskTimedOutEventDetails.html
---

# TaskTimedOutEventDetails
<a name="API_TaskTimedOutEventDetails"></a>

Contains details about a resource timeout that occurred during an execution.

## Contents
<a name="API_TaskTimedOutEventDetails_Contents"></a>

 ** resource **   <a name="StepFunctions-Type-TaskTimedOutEventDetails-resource"></a>
The action of the resource called by a task state.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Required: Yes

 ** resourceType **   <a name="StepFunctions-Type-TaskTimedOutEventDetails-resourceType"></a>
The service name of the resource in a task state.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Required: Yes

 ** cause **   <a name="StepFunctions-Type-TaskTimedOutEventDetails-cause"></a>
A more detailed explanation of the cause of the failure.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32768.
Required: No

 ** error **   <a name="StepFunctions-Type-TaskTimedOutEventDetails-error"></a>
The error code of the failure.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_TaskTimedOutEventDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/TaskTimedOutEventDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/TaskTimedOutEventDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/TaskTimedOutEventDetails)
