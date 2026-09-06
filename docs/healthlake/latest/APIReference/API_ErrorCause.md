---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ErrorCause.html
---

# ErrorCause
<a name="API_ErrorCause"></a>

The error information for `CreateFHIRDatastore` and `DeleteFHIRDatastore` actions.

## Contents
<a name="API_ErrorCause_Contents"></a>

 ** ErrorCategory **   <a name="HealthLake-Type-ErrorCause-ErrorCategory"></a>
The error category for `ErrorCause`.
Type: String
Valid Values: `RETRYABLE_ERROR | NON_RETRYABLE_ERROR`
Required: No

 ** ErrorMessage **   <a name="HealthLake-Type-ErrorCause-ErrorMessage"></a>
The error message text for `ErrorCause`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## See Also
<a name="API_ErrorCause_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/ErrorCause)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/ErrorCause)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/ErrorCause)
