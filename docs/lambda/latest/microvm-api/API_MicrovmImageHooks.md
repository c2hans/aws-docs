---
source_url: https://docs.aws.amazon.com/lambda/latest/microvm-api/API_MicrovmImageHooks.html
---

# MicrovmImageHooks
<a name="API_MicrovmImageHooks"></a>

Configuration for hooks invoked during MicroVM image build events such as ready and validate.

## Contents
<a name="API_MicrovmImageHooks_Contents"></a>

 ** ready **   <a name="lambdamicrovm-Type-MicrovmImageHooks-ready"></a>
The path of the hook invoked when the MicroVM image build is ready.
Type: String
Valid Values: `DISABLED | ENABLED`
Required: No

 ** readyTimeoutInSeconds **   <a name="lambdamicrovm-Type-MicrovmImageHooks-readyTimeoutInSeconds"></a>
The maximum time in seconds for the ready hook to complete.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 3600.
Required: No

 ** validate **   <a name="lambdamicrovm-Type-MicrovmImageHooks-validate"></a>
The path of the hook invoked to validate the MicroVM image build.
Type: String
Valid Values: `DISABLED | ENABLED`
Required: No

 ** validateTimeoutInSeconds **   <a name="lambdamicrovm-Type-MicrovmImageHooks-validateTimeoutInSeconds"></a>
The maximum time in seconds for the validate hook to complete.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 3600.
Required: No

## See Also
<a name="API_MicrovmImageHooks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-microvms-2025-09-09/MicrovmImageHooks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-microvms-2025-09-09/MicrovmImageHooks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-microvms-2025-09-09/MicrovmImageHooks)
