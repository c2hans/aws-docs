---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_SegmentDeliveryConfiguration.html
---

# SegmentDeliveryConfiguration
<a name="API_SegmentDeliveryConfiguration"></a>

The segment delivery configuration settings.

## Contents
<a name="API_SegmentDeliveryConfiguration_Contents"></a>

 ** BaseUrl **   <a name="mediatailor-Type-SegmentDeliveryConfiguration-BaseUrl"></a>
The base URL of the host or path of the segment delivery server that you're using to serve segments. This is typically a content delivery network (CDN). The URL can be absolute or relative. To use an absolute URL include the protocol, such as `https://example.com/some/path`. To use a relative URL specify the relative path, such as `/some/path*`.
Type: String
Required: No

 ** Name **   <a name="mediatailor-Type-SegmentDeliveryConfiguration-Name"></a>
A unique identifier used to distinguish between multiple segment delivery configurations in a source location.
Type: String
Required: No

## See Also
<a name="API_SegmentDeliveryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/SegmentDeliveryConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/SegmentDeliveryConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/SegmentDeliveryConfiguration)
