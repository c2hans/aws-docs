---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RistRouterInputConfiguration.html
---

# RistRouterInputConfiguration
<a name="API_RistRouterInputConfiguration"></a>

The configuration settings for a router input using the RIST (Reliable Internet Stream Transport) protocol, including the port and recovery latency.

## Contents
<a name="API_RistRouterInputConfiguration_Contents"></a>

 ** port **   <a name="mediaconnect-Type-RistRouterInputConfiguration-port"></a>
The port number used for the RIST protocol in the router input configuration.
Type: Integer
Valid Range: Minimum value of 3000. Maximum value of 30000.
Required: Yes

 ** recoveryLatencyMilliseconds **   <a name="mediaconnect-Type-RistRouterInputConfiguration-recoveryLatencyMilliseconds"></a>
The recovery latency in milliseconds for the RIST protocol in the router input configuration.
Type: Long
Valid Range: Minimum value of 10. Maximum value of 10000.
Required: Yes

## See Also
<a name="API_RistRouterInputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RistRouterInputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RistRouterInputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RistRouterInputConfiguration)
