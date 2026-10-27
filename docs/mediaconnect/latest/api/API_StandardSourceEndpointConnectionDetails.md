---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_StandardSourceEndpointConnectionDetails.html
---

# StandardSourceEndpointConnectionDetails
<a name="API_StandardSourceEndpointConnectionDetails"></a>

The connection details for a standard source endpoint.

## Contents
<a name="API_StandardSourceEndpointConnectionDetails_Contents"></a>

 ** destinationDecryptionConfiguration **   <a name="mediaconnect-Type-StandardSourceEndpointConnectionDetails-destinationDecryptionConfiguration"></a>
The encryption settings for an endpoint connection. This is a union type, so exactly one of its members is set: `secretsManager` when you store the encryption key or passphrase in AWS Secrets Manager, or `automatic` when you let MediaConnect determine the encryption key when the endpoint connects.
Type: [EndpointEncryptionConfiguration](API_EndpointEncryptionConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** destinationDecryptionType **   <a name="mediaconnect-Type-StandardSourceEndpointConnectionDetails-destinationDecryptionType"></a>
The type of decryption that the destination uses for the connection.
Type: String
Valid Values: `SECRETS_MANAGER | AUTOMATIC`
Required: No

 ** destinationEndpointType **   <a name="mediaconnect-Type-StandardSourceEndpointConnectionDetails-destinationEndpointType"></a>
The type of the connected destination endpoint.
Type: String
Valid Values: `STANDARD | ROUTER_INPUT`
Required: No

 ** destinationIngestPort **   <a name="mediaconnect-Type-StandardSourceEndpointConnectionDetails-destinationIngestPort"></a>
The port on the destination that receives the content.
Type: Integer
Required: No

 ** destinationIpAddress **   <a name="mediaconnect-Type-StandardSourceEndpointConnectionDetails-destinationIpAddress"></a>
The IP address of the destination that receives the content.
Type: String
Required: No

## See Also
<a name="API_StandardSourceEndpointConnectionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/StandardSourceEndpointConnectionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/StandardSourceEndpointConnectionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/StandardSourceEndpointConnectionDetails)
