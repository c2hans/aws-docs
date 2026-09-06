---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_HttpEndpointRequestConfiguration.html
---

# HttpEndpointRequestConfiguration
<a name="API_HttpEndpointRequestConfiguration"></a>

The configuration of the HTTP endpoint request.

## Contents
<a name="API_HttpEndpointRequestConfiguration_Contents"></a>

 ** CommonAttributes **   <a name="Firehose-Type-HttpEndpointRequestConfiguration-CommonAttributes"></a>
Describes the metadata sent to the HTTP endpoint destination.
Type: Array of [HttpEndpointCommonAttribute](API_HttpEndpointCommonAttribute.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** ContentEncoding **   <a name="Firehose-Type-HttpEndpointRequestConfiguration-ContentEncoding"></a>
Firehose uses the content encoding to compress the body of a request before sending the request to the destination. For more information, see [Content-Encoding](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Encoding) in MDN Web Docs, the official Mozilla documentation.
Type: String
Valid Values: `NONE | GZIP`
Required: No

## See Also
<a name="API_HttpEndpointRequestConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/HttpEndpointRequestConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/HttpEndpointRequestConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/HttpEndpointRequestConfiguration)
