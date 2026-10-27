---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_SrtListenerStandardDestinationEndpointConfiguration.html
---

# SrtListenerStandardDestinationEndpointConfiguration
<a name="API_SrtListenerStandardDestinationEndpointConfiguration"></a>

The configuration settings for a destination endpoint that uses SRT in listener mode.

## Contents
<a name="API_SrtListenerStandardDestinationEndpointConfiguration_Contents"></a>

 ** destinationAddress **   <a name="mediaconnect-Type-SrtListenerStandardDestinationEndpointConfiguration-destinationAddress"></a>
The IP address on which the destination endpoint listens for incoming connections.
Type: String
Required: Yes

 ** destinationIngestPort **   <a name="mediaconnect-Type-SrtListenerStandardDestinationEndpointConfiguration-destinationIngestPort"></a>
The port on which the destination endpoint listens for incoming connections. The valid range is 0 to 65531.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65531.
Required: Yes

 ** minimumLatencyMilliseconds **   <a name="mediaconnect-Type-SrtListenerStandardDestinationEndpointConfiguration-minimumLatencyMilliseconds"></a>
The minimum latency, in milliseconds, for the SRT connection. The valid range is 10 to 10000.
Type: Long
Valid Range: Minimum value of 10. Maximum value of 10000.
Required: Yes

 ** encryptionPassphrase **   <a name="mediaconnect-Type-SrtListenerStandardDestinationEndpointConfiguration-encryptionPassphrase"></a>
The configuration for the AWS Secrets Manager secret that holds the key or passphrase used to encrypt an endpoint connection.
Type: [EndpointEncryptionSecretConfiguration](API_EndpointEncryptionSecretConfiguration.md) object
Required: No

 ** streamId **   <a name="mediaconnect-Type-SrtListenerStandardDestinationEndpointConfiguration-streamId"></a>
The stream ID that identifies the content for the SRT connection.
Type: String
Required: No

## See Also
<a name="API_SrtListenerStandardDestinationEndpointConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/SrtListenerStandardDestinationEndpointConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/SrtListenerStandardDestinationEndpointConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/SrtListenerStandardDestinationEndpointConfiguration)
