---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RtpStandardDestinationEndpointConfiguration.html
---

# RtpStandardDestinationEndpointConfiguration
<a name="API_RtpStandardDestinationEndpointConfiguration"></a>

The configuration settings for a destination endpoint that uses the RTP protocol.

## Contents
<a name="API_RtpStandardDestinationEndpointConfiguration_Contents"></a>

 ** destinationAddress **   <a name="mediaconnect-Type-RtpStandardDestinationEndpointConfiguration-destinationAddress"></a>
The IP address on which the destination endpoint receives content.
Type: String
Required: Yes

 ** destinationIngestPort **   <a name="mediaconnect-Type-RtpStandardDestinationEndpointConfiguration-destinationIngestPort"></a>
The port on which the destination endpoint receives content. The valid range is 1024 to 65531.
Type: Integer
Valid Range: Minimum value of 1024. Maximum value of 65531.
Required: Yes

 ** forwardErrorCorrectionState **   <a name="mediaconnect-Type-RtpStandardDestinationEndpointConfiguration-forwardErrorCorrectionState"></a>
Indicates whether forward error correction (FEC) is enabled for the destination endpoint.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

## See Also
<a name="API_RtpStandardDestinationEndpointConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RtpStandardDestinationEndpointConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RtpStandardDestinationEndpointConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RtpStandardDestinationEndpointConfiguration)
