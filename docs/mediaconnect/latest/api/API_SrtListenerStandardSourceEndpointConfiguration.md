---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_SrtListenerStandardSourceEndpointConfiguration.html
---

# SrtListenerStandardSourceEndpointConfiguration
<a name="API_SrtListenerStandardSourceEndpointConfiguration"></a>

The configuration settings for a source endpoint that uses SRT in listener mode.

## Contents
<a name="API_SrtListenerStandardSourceEndpointConfiguration_Contents"></a>

 ** minimumLatencyMilliseconds **   <a name="mediaconnect-Type-SrtListenerStandardSourceEndpointConfiguration-minimumLatencyMilliseconds"></a>
The minimum latency, in milliseconds, for the SRT connection. The valid range is 10 to 10000.
Type: Long
Valid Range: Minimum value of 10. Maximum value of 10000.
Required: Yes

 ** sourceAddress **   <a name="mediaconnect-Type-SrtListenerStandardSourceEndpointConfiguration-sourceAddress"></a>
The IP address that the source endpoint listens on for incoming connections.
Type: String
Required: Yes

 ** sourceListenerPort **   <a name="mediaconnect-Type-SrtListenerStandardSourceEndpointConfiguration-sourceListenerPort"></a>
The port that the source endpoint listens on for incoming connections. The valid range is 1024 to 65535.
Type: Integer
Valid Range: Minimum value of 1024. Maximum value of 65535.
Required: Yes

 ** encryptionPassphrase **   <a name="mediaconnect-Type-SrtListenerStandardSourceEndpointConfiguration-encryptionPassphrase"></a>
The configuration for the AWS Secrets Manager secret that holds the key or passphrase used to encrypt an endpoint connection.
Type: [EndpointEncryptionSecretConfiguration](API_EndpointEncryptionSecretConfiguration.md) object
Required: No

 ** streamId **   <a name="mediaconnect-Type-SrtListenerStandardSourceEndpointConfiguration-streamId"></a>
The stream ID that identifies the content for the SRT connection.
Type: String
Required: No

## See Also
<a name="API_SrtListenerStandardSourceEndpointConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/SrtListenerStandardSourceEndpointConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/SrtListenerStandardSourceEndpointConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/SrtListenerStandardSourceEndpointConfiguration)
