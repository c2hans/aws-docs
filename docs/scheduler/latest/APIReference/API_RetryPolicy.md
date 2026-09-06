---
source_url: https://docs.aws.amazon.com/scheduler/latest/APIReference/API_RetryPolicy.html
---

# RetryPolicy
<a name="API_RetryPolicy"></a>

A `RetryPolicy` object that includes information about the retry policy settings, including the maximum age of an event, and the maximum number of times EventBridge Scheduler will try to deliver the event to a target.

## Contents
<a name="API_RetryPolicy_Contents"></a>

 ** MaximumEventAgeInSeconds **   <a name="scheduler-Type-RetryPolicy-MaximumEventAgeInSeconds"></a>
The maximum amount of time, in seconds, to continue to make retry attempts.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 86400.
Required: No

 ** MaximumRetryAttempts **   <a name="scheduler-Type-RetryPolicy-MaximumRetryAttempts"></a>
The maximum number of retry attempts to make before the request fails. Retry attempts with exponential backoff continue until either the maximum number of attempts is made or until the duration of the `MaximumEventAgeInSeconds` is reached.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 185.
Required: No

## See Also
<a name="API_RetryPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/scheduler-2021-06-30/RetryPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/scheduler-2021-06-30/RetryPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/scheduler-2021-06-30/RetryPolicy)
