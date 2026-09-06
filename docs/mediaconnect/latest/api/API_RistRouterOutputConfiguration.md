---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RistRouterOutputConfiguration.html
---

# RistRouterOutputConfiguration
<a name="API_RistRouterOutputConfiguration"></a>

The configuration settings for a router output using the RIST (Reliable Internet Stream Transport) protocol, including the destination address and port.

## Contents
<a name="API_RistRouterOutputConfiguration_Contents"></a>

 ** destinationAddress **   <a name="mediaconnect-Type-RistRouterOutputConfiguration-destinationAddress"></a>
The destination IP address for the RIST protocol in the router output configuration.
Type: String
Required: Yes

 ** destinationPort **   <a name="mediaconnect-Type-RistRouterOutputConfiguration-destinationPort"></a>
The destination port number for the RIST protocol in the router output configuration.
Type: Integer
Valid Range: Minimum value of 1024. Maximum value of 65535.
Required: Yes

## See Also
<a name="API_RistRouterOutputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RistRouterOutputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RistRouterOutputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RistRouterOutputConfiguration)
