---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RtpStandardSourceEndpointConfiguration.html
---

# RtpStandardSourceEndpointConfiguration
<a name="API_RtpStandardSourceEndpointConfiguration"></a>

The configuration settings for a source endpoint that uses the RTP protocol.

## Contents
<a name="API_RtpStandardSourceEndpointConfiguration_Contents"></a>

 ** destinationIngestPort **   <a name="mediaconnect-Type-RtpStandardSourceEndpointConfiguration-destinationIngestPort"></a>
The port on the destination that receives the content. The valid range is 3000 to 30000.
Type: Integer
Valid Range: Minimum value of 3000. Maximum value of 30000.
Required: Yes

 ** forwardErrorCorrectionState **   <a name="mediaconnect-Type-RtpStandardSourceEndpointConfiguration-forwardErrorCorrectionState"></a>
Indicates whether forward error correction (FEC) is enabled for the source endpoint.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

## See Also
<a name="API_RtpStandardSourceEndpointConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RtpStandardSourceEndpointConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RtpStandardSourceEndpointConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RtpStandardSourceEndpointConfiguration)
