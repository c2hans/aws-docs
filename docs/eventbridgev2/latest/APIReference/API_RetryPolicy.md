---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_RetryPolicy.html
---

# RetryPolicy
<a name="API_RetryPolicy"></a>

Retry policy for a subscriber.

## Contents
<a name="API_RetryPolicy_Contents"></a>

 ** MaxEventAgeInSeconds **   <a name="eventbridgev2-Type-RetryPolicy-MaxEventAgeInSeconds"></a>
Maximum age of an event in seconds before it is discarded (60-86400, default: 300).
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 86400.
Required: No

 ** MaxRetryAttempts **   <a name="eventbridgev2-Type-RetryPolicy-MaxRetryAttempts"></a>
Maximum number of retry attempts (0-185, default: 5).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 185.
Required: No

 ** RetryStrategy **   <a name="eventbridgev2-Type-RetryPolicy-RetryStrategy"></a>
Strategy for determining which exceptions are retried. Default: ALL.
Type: String
Valid Values: `ALL`
Required: No

## See Also
<a name="API_RetryPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/RetryPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/RetryPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/RetryPolicy)
