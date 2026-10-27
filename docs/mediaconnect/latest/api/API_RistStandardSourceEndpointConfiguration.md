---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RistStandardSourceEndpointConfiguration.html
---

# RistStandardSourceEndpointConfiguration
<a name="API_RistStandardSourceEndpointConfiguration"></a>

The configuration settings for a source endpoint that uses the RIST protocol.

## Contents
<a name="API_RistStandardSourceEndpointConfiguration_Contents"></a>

 ** destinationIngestPort **   <a name="mediaconnect-Type-RistStandardSourceEndpointConfiguration-destinationIngestPort"></a>
The port on the destination that receives the content. The valid range is 3000 to 30000.
Type: Integer
Valid Range: Minimum value of 3000. Maximum value of 30000.
Required: Yes

 ** recoveryLatencyMilliseconds **   <a name="mediaconnect-Type-RistStandardSourceEndpointConfiguration-recoveryLatencyMilliseconds"></a>
The amount of time, in milliseconds, that the source endpoint allows for recovering lost packets. The valid range is 10 to 10000.
Type: Long
Valid Range: Minimum value of 10. Maximum value of 10000.
Required: Yes

## See Also
<a name="API_RistStandardSourceEndpointConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RistStandardSourceEndpointConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RistStandardSourceEndpointConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RistStandardSourceEndpointConfiguration)
