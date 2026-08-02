---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_TaskStartFailedEventDetails.html
---

# TaskStartFailedEventDetails
<a name="API_TaskStartFailedEventDetails"></a>

Contains details about a task that failed to start during an execution.

## Contents
<a name="API_TaskStartFailedEventDetails_Contents"></a>

 ** resource **   <a name="StepFunctions-Type-TaskStartFailedEventDetails-resource"></a>
The action of the resource called by a task state.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Required: Yes

 ** resourceType **   <a name="StepFunctions-Type-TaskStartFailedEventDetails-resourceType"></a>
The service name of the resource in a task state.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Required: Yes

 ** cause **   <a name="StepFunctions-Type-TaskStartFailedEventDetails-cause"></a>
A more detailed explanation of the cause of the failure.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32768.
Required: No

 ** error **   <a name="StepFunctions-Type-TaskStartFailedEventDetails-error"></a>
The error code of the failure.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_TaskStartFailedEventDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/TaskStartFailedEventDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/TaskStartFailedEventDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/TaskStartFailedEventDetails)
