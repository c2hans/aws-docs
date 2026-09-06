---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_RetryPolicy.html
---

# RetryPolicy
<a name="API_RetryPolicy"></a>

The retry policy to use for a job run.

## Contents
<a name="API_RetryPolicy_Contents"></a>

 ** maxAttempts **   <a name="emrserverless-Type-RetryPolicy-maxAttempts"></a>
Maximum number of attempts for the job run. This parameter is only applicable for `BATCH` mode.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** maxFailedAttemptsPerHour **   <a name="emrserverless-Type-RetryPolicy-maxFailedAttemptsPerHour"></a>
Maximum number of failed attempts per hour. This [arameter is only applicable for `STREAMING` mode.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_RetryPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/RetryPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/RetryPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/RetryPolicy)
