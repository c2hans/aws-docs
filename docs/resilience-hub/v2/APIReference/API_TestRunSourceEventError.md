---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_TestRunSourceEventError.html
---

# TestRunSourceEventError
<a name="API_TestRunSourceEventError"></a>

Describes an error that prevented event collection from a test run monitoring source.

## Contents
<a name="API_TestRunSourceEventError_Contents"></a>

 ** errorCode **   <a name="ngresiliencehub-Type-TestRunSourceEventError-errorCode"></a>
The error code.
Type: String
Valid Values: `ACCESS_DENIED | INTERNAL_ERROR`
Required: Yes

 ** errorMessage **   <a name="ngresiliencehub-Type-TestRunSourceEventError-errorMessage"></a>
A human-readable description of the error.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: Yes

## See Also
<a name="API_TestRunSourceEventError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/TestRunSourceEventError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/TestRunSourceEventError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/TestRunSourceEventError)
