---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_SrtCallerStandardSourceEndpointConfiguration.html
---

# SrtCallerStandardSourceEndpointConfiguration
<a name="API_SrtCallerStandardSourceEndpointConfiguration"></a>

The configuration settings for a source endpoint that uses SRT in caller mode.

## Contents
<a name="API_SrtCallerStandardSourceEndpointConfiguration_Contents"></a>

 ** destinationIngestPort **   <a name="mediaconnect-Type-SrtCallerStandardSourceEndpointConfiguration-destinationIngestPort"></a>
The port on which the destination listens for the connection. The valid range is 3000 to 30000.
Type: Integer
Valid Range: Minimum value of 3000. Maximum value of 30000.
Required: Yes

 ** minimumLatencyMilliseconds **   <a name="mediaconnect-Type-SrtCallerStandardSourceEndpointConfiguration-minimumLatencyMilliseconds"></a>
The minimum latency, in milliseconds, for the SRT connection. The valid range is 10 to 10000.
Type: Long
Valid Range: Minimum value of 10. Maximum value of 10000.
Required: Yes

 ** encryptionPassphrase **   <a name="mediaconnect-Type-SrtCallerStandardSourceEndpointConfiguration-encryptionPassphrase"></a>
The configuration for the AWS Secrets Manager secret that holds the key or passphrase used to encrypt an endpoint connection.
Type: [EndpointEncryptionSecretConfiguration](API_EndpointEncryptionSecretConfiguration.md) object
Required: No

## See Also
<a name="API_SrtCallerStandardSourceEndpointConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/SrtCallerStandardSourceEndpointConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/SrtCallerStandardSourceEndpointConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/SrtCallerStandardSourceEndpointConfiguration)
