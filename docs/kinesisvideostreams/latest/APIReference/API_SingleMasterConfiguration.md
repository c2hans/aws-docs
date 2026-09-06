---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_SingleMasterConfiguration.html
---

# SingleMasterConfiguration
<a name="API_SingleMasterConfiguration"></a>

A structure that contains the configuration for the `SINGLE_MASTER` channel type.

## Contents
<a name="API_SingleMasterConfiguration_Contents"></a>

 ** MessageTtlSeconds **   <a name="KinesisVideo-Type-SingleMasterConfiguration-MessageTtlSeconds"></a>
The period of time (in seconds) a signaling channel retains undelivered messages before they are discarded. Use [UpdateSignalingChannel](API_UpdateSignalingChannel.md) to update this value.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 120.
Required: No

## See Also
<a name="API_SingleMasterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisvideo-2017-09-30/SingleMasterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisvideo-2017-09-30/SingleMasterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisvideo-2017-09-30/SingleMasterConfiguration)
