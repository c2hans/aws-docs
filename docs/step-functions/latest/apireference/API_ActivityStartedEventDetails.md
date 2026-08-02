---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_ActivityStartedEventDetails.html
---

# ActivityStartedEventDetails
<a name="API_ActivityStartedEventDetails"></a>

Contains details about the start of an activity during an execution.

## Contents
<a name="API_ActivityStartedEventDetails_Contents"></a>

 ** workerName **   <a name="StepFunctions-Type-ActivityStartedEventDetails-workerName"></a>
The name of the worker that the task is assigned to. These names are provided by the workers when calling [GetActivityTask](API_GetActivityTask.md).
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_ActivityStartedEventDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/ActivityStartedEventDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/ActivityStartedEventDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/ActivityStartedEventDetails)
