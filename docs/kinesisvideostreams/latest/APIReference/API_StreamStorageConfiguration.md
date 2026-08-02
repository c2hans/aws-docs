---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_StreamStorageConfiguration.html
---

# StreamStorageConfiguration
<a name="API_StreamStorageConfiguration"></a>

The configuration for stream storage, including the default storage tier for stream data. This configuration determines how stream data is stored and accessed, with different tiers offering varying levels of performance and cost optimization.

## Contents
<a name="API_StreamStorageConfiguration_Contents"></a>

 ** DefaultStorageTier **   <a name="KinesisVideo-Type-StreamStorageConfiguration-DefaultStorageTier"></a>
The default storage tier for the stream data. This setting determines the storage class used for stream data, affecting both performance characteristics and storage costs.
Available storage tiers:
+  `HOT` - Optimized for frequent access with the lowest latency and highest performance. Ideal for real-time applications and frequently accessed data.
+  `WARM` - Balanced performance and cost for moderately accessed data. Suitable for data that is accessed regularly but not continuously.
Type: String
Valid Values: `HOT | WARM`
Required: Yes

## See Also
<a name="API_StreamStorageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisvideo-2017-09-30/StreamStorageConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisvideo-2017-09-30/StreamStorageConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisvideo-2017-09-30/StreamStorageConfiguration)
