---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_TransformProcessingConfig.html
---

# TransformProcessingConfig
<a name="API_TransformProcessingConfig"></a>

The processing configuration for the given transform property. You can configure transforms to be kept at the edge or forwarded to the AWS Cloud. You can also configure transforms to be computed at the edge or in the cloud.

## Contents
<a name="API_TransformProcessingConfig_Contents"></a>

 ** computeLocation **   <a name="iotsitewise-Type-TransformProcessingConfig-computeLocation"></a>
The compute location for the given transform property.
Type: String
Valid Values: `EDGE | CLOUD`
Required: Yes

 ** forwardingConfig **   <a name="iotsitewise-Type-TransformProcessingConfig-forwardingConfig"></a>
The forwarding configuration for a given property.
Type: [ForwardingConfig](API_ForwardingConfig.md) object
Required: No

## See Also
<a name="API_TransformProcessingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/TransformProcessingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/TransformProcessingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/TransformProcessingConfig)
