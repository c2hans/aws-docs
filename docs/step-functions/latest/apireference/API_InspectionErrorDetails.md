---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_InspectionErrorDetails.html
---

# InspectionErrorDetails
<a name="API_InspectionErrorDetails"></a>

An object containing data about a handled exception in the tested state.

## Contents
<a name="API_InspectionErrorDetails_Contents"></a>

 ** catchIndex **   <a name="StepFunctions-Type-InspectionErrorDetails-catchIndex"></a>
The array index of the Catch which handled the exception.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** retryBackoffIntervalSeconds **   <a name="StepFunctions-Type-InspectionErrorDetails-retryBackoffIntervalSeconds"></a>
The duration in seconds of the backoff for a retry on a failed state invocation.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** retryIndex **   <a name="StepFunctions-Type-InspectionErrorDetails-retryIndex"></a>
The array index of the Retry which handled the exception.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_InspectionErrorDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/InspectionErrorDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/InspectionErrorDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/InspectionErrorDetails)
