---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_SrtCallerStandardDestinationEndpointConfiguration.html
---

# SrtCallerStandardDestinationEndpointConfiguration
<a name="API_SrtCallerStandardDestinationEndpointConfiguration"></a>

The configuration settings for a destination endpoint that uses SRT in caller mode.

## Contents
<a name="API_SrtCallerStandardDestinationEndpointConfiguration_Contents"></a>

 ** minimumLatencyMilliseconds **   <a name="mediaconnect-Type-SrtCallerStandardDestinationEndpointConfiguration-minimumLatencyMilliseconds"></a>
The minimum latency, in milliseconds, for the SRT connection. The valid range is 10 to 10000.
Type: Long
Valid Range: Minimum value of 10. Maximum value of 10000.
Required: Yes

 ** sourceListenerPort **   <a name="mediaconnect-Type-SrtCallerStandardDestinationEndpointConfiguration-sourceListenerPort"></a>
The port on which the source listens for the connection. The valid range is 3000 to 30000.
Type: Integer
Valid Range: Minimum value of 3000. Maximum value of 30000.
Required: Yes

 ** encryptionPassphrase **   <a name="mediaconnect-Type-SrtCallerStandardDestinationEndpointConfiguration-encryptionPassphrase"></a>
The configuration for the AWS Secrets Manager secret that holds the key or passphrase used to encrypt an endpoint connection.
Type: [EndpointEncryptionSecretConfiguration](API_EndpointEncryptionSecretConfiguration.md) object
Required: No

## See Also
<a name="API_SrtCallerStandardDestinationEndpointConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/SrtCallerStandardDestinationEndpointConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/SrtCallerStandardDestinationEndpointConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/SrtCallerStandardDestinationEndpointConfiguration)
