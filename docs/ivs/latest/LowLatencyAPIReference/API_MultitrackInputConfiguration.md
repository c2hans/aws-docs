---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_MultitrackInputConfiguration.html
---

# MultitrackInputConfiguration
<a name="API_MultitrackInputConfiguration"></a>

A complex type that specifies multitrack input configuration.

## Contents
<a name="API_MultitrackInputConfiguration_Contents"></a>

 ** enabled **   <a name="ivs-Type-MultitrackInputConfiguration-enabled"></a>
Indicates whether multitrack input is enabled. Can be set to `true` only if channel type is `STANDARD`. Setting `enabled` to `true` with any other channel type will cause an exception. If `true`, then `policy`, `maximumResolution`, and `containerFormat` are required, and `containerFormat` must be set to `FRAGMENTED_MP4`. Default: `false`.
Type: Boolean
Required: No

 ** maximumResolution **   <a name="ivs-Type-MultitrackInputConfiguration-maximumResolution"></a>
Maximum resolution for multitrack input. Required if `enabled` is `true`.
Type: String
Valid Values: `SD | HD | FULL_HD`
Required: No

 ** policy **   <a name="ivs-Type-MultitrackInputConfiguration-policy"></a>
Indicates whether multitrack input is allowed or required. Required if `enabled` is `true`.
Type: String
Valid Values: `ALLOW | REQUIRE`
Required: No

## See Also
<a name="API_MultitrackInputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/MultitrackInputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/MultitrackInputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/MultitrackInputConfiguration)
