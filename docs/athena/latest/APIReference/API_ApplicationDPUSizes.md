---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_ApplicationDPUSizes.html
---

# ApplicationDPUSizes
<a name="API_ApplicationDPUSizes"></a>

Contains the application runtime IDs and their supported DPU sizes.

## Contents
<a name="API_ApplicationDPUSizes_Contents"></a>

 ** ApplicationRuntimeId **   <a name="athena-Type-ApplicationDPUSizes-ApplicationRuntimeId"></a>
The name of the supported application runtime (for example, `Athena notebook version 1`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** SupportedDPUSizes **   <a name="athena-Type-ApplicationDPUSizes-SupportedDPUSizes"></a>
A list of the supported DPU sizes that the application runtime supports.
Type: Array of integers
Required: No

## See Also
<a name="API_ApplicationDPUSizes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/ApplicationDPUSizes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/ApplicationDPUSizes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/ApplicationDPUSizes)
