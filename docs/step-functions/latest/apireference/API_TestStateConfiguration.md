---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_TestStateConfiguration.html
---

# TestStateConfiguration
<a name="API_TestStateConfiguration"></a>

Contains configurations for the tested state.

## Contents
<a name="API_TestStateConfiguration_Contents"></a>

 ** errorCausedByState **   <a name="StepFunctions-Type-TestStateConfiguration-errorCausedByState"></a>
The name of the state from which an error originates when an error is mocked for a Map or Parallel state.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Required: No

 ** mapItemReaderData **   <a name="StepFunctions-Type-TestStateConfiguration-mapItemReaderData"></a>
The data read by ItemReader in Distributed Map states as found in its original source.
Type: String
Length Constraints: Maximum length of 262144.
Required: No

 ** mapIterationFailureCount **   <a name="StepFunctions-Type-TestStateConfiguration-mapIterationFailureCount"></a>
The number of Map state iterations that failed during the Map state invocation.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** retrierRetryCount **   <a name="StepFunctions-Type-TestStateConfiguration-retrierRetryCount"></a>
The number of retry attempts that have occurred for the state's Retry that applies to the mocked error.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_TestStateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/TestStateConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/TestStateConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/TestStateConfiguration)
