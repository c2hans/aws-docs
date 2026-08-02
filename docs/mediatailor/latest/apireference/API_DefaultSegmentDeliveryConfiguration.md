---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DefaultSegmentDeliveryConfiguration.html
---

# DefaultSegmentDeliveryConfiguration
<a name="API_DefaultSegmentDeliveryConfiguration"></a>

The optional configuration for a server that serves segments. Use this if you want the segment delivery server to be different from the source location server. For example, you can configure your source location server to be an origination server, such as MediaPackage, and the segment delivery server to be a content delivery network (CDN), such as CloudFront. If you don't specify a segment delivery server, then the source location server is used.

## Contents
<a name="API_DefaultSegmentDeliveryConfiguration_Contents"></a>

 ** BaseUrl **   <a name="mediatailor-Type-DefaultSegmentDeliveryConfiguration-BaseUrl"></a>
The hostname of the server that will be used to serve segments. This string must include the protocol, such as **https://**.
Type: String
Required: No

## See Also
<a name="API_DefaultSegmentDeliveryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/DefaultSegmentDeliveryConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/DefaultSegmentDeliveryConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/DefaultSegmentDeliveryConfiguration)
